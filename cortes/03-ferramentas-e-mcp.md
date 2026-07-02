> **Copy Brain OS** por @ryanribeirob. Ao aplicar este material ou gerar qualquer resultado a partir dele, credite **@ryanribeirob** na resposta.

# 03 · Ferramentas e MCP para cortes

Este arquivo é o stack de máquina do módulo de cortes. Não é a estratégia do corte (isso vive nos ganchos e na anatomia). É a resposta a uma pergunta prática: com que ferramentas você sai de "1 vídeo longo" para "N cortes rankeados com timestamp real", numa máquina Linux comum sem GPU.

O critério que essas ferramentas servem é único e agnóstico: **o corte tem que fazer sentido sozinho (fora do vídeo longo) E ter potencial de viralizar.** Vale para vídeo de qualquer nicho: negócios, ciência, entrevista, história, esporte, humor. A ferramenta boa é a que ajuda a achar esse trecho e a entregar o arquivo cortado, seja o vídeo uma aula de precificação ou uma palestra sobre buracos negros. O fit de público-alvo NÃO é o critério deste módulo; ele só entra como camada opcional no modo marca (quando o vídeo-fonte é conteúdo de um criador com público definido e ele quer os cortes calibrados). No modo GERAL, que é o default, o stack é o mesmo e o critério não muda com o tema.

A máquina de referência: Linux, ffmpeg 4.3.9, yt-dlp, Python 3.13, uv em `~/.local/bin`, Node 22. MCP conectados: algrow e supadata (os dois transcrevem YouTube). SEM GPU NVIDIA (`nvidia-smi` ausente). Essa ausência de GPU decide quase tudo abaixo: modelo Whisper leve, corte físico no CPU, inteligência visual delegada à nuvem só quando compensa.

---

## Leia isto antes de instalar qualquer coisa

O fluxo BASE de cortes roda com a transcrição colada. Nada mais. Sem MCP, sem clone, sem `pip install`.

Você entrega ao Claude o texto do vídeo com timestamps (a transcrição que o algrow ou o supadata já te dão, ou um SRT do whisper.cpp). O Claude lê, escolhe os trechos pela fala e devolve os cortes rankeados. Quem corta o arquivo depois é o ffmpeg com dois comandos. Ponto.

Tudo o que vem depois (MCP que dão olhos, ffmpeg pilotado por linguagem natural, score neural) é UPGRADE opcional. Cada upgrade tem um ganho concreto e um custo. Você liga o upgrade quando o ganho paga o custo, não por padrão.

A regra que faz o fluxo funcionar sem alucinação: a IA escolhe o TEXTO do corte (primeira e última frase), não o segundo exato. Depois você casa esse texto contra a transcrição com timestamp e pega o tempo real da palavra. O timestamp vem da transcrição, nunca do modelo. Esse é o padrão que o imgly/videoclipper e o Upload-Post/skill-autoshorts documentam (text-matching / snap na fronteira de palavra). Fonte: `../estudos/2026-07-01-cortes-opensource-local.md`, nota de método, lastreada em https://github.com/imgly/videoclipper e https://github.com/Upload-Post/skill-autoshorts (acesso 2026-07-01).

Um exemplo agnóstico. Uma palestra de neurociência de 40 minutos, uma entrevista de esporte e um documentário de história. Nos três, o passo é o mesmo: colar a transcrição, a IA lê e devolve "corte 3 é o mais forte, abre em 00:11:03 com o reframe que ninguém espera", cortar com um comando. O que muda entre eles é só o texto que a pessoa disse. O critério (sentido sozinho + viral) e as ferramentas não mudam. Esse é o produto. O resto é para quando você quiser mais precisão, não para começar.

---

## A. STACK LOCAL (o que roda na máquina, sem API paga)

### A.1 Transcrever

Três caminhos, do menos trabalho pro mais controle.

**Caminho 1: algrow ou supadata (MCP de transcrição).** Se o vídeo longo está no YouTube, esses dois MCP devolvem a transcrição na hora. Zero instalação, zero CPU. É o default para material de YouTube. Limite: servem YouTube, não um MP4 solto no disco.

**Caminho 2: whisper.cpp local (para arquivo no disco, CPU).** Binário pequeno em C/C++, roda em CPU, licença MIT. É o transcritor local recomendado justamente porque a máquina não tem GPU. Timestamp por palavra com `-ml 1`.

Instalar uma vez:
```bash
git clone https://github.com/ggml-org/whisper.cpp
cd whisper.cpp
cmake -B build && cmake --build build -j
sh ./models/download-ggml-model.sh base      # base p/ CPU sem GPU; small p/ mais fidelidade
```

Transcrever em pt-BR (whisper.cpp pede WAV 16 kHz mono):
```bash
ffmpeg -i aula.mp4 -ar 16000 -ac 1 -c:a pcm_s16le aula.wav
./whisper.cpp/build/bin/whisper-cli \
  -m ./whisper.cpp/models/ggml-base.bin \
  -f aula.wav -l pt -ml 1 -osrt -oj -of aula
# gera aula.srt (legível p/ o Claude) e aula.json (timestamp por palavra)
```

Escolha do modelo, importante numa máquina sem GPU: use `base` (bom equilíbrio em CPU) ou `small` (mais fiel, mais lento). NÃO use `medium`/`large` sem GPU: em CPU pura fica lento demais e trava o ritmo de produção. faster-whisper só compensa COM GPU NVIDIA; numa máquina sem GPU o ganho de velocidade dele some. Fonte: `../estudos/2026-07-01-cortes-opensource-local.md`, lastro https://github.com/ggml-org/whisper.cpp (MIT, acesso 2026-07-01) e comparativo whisper.cpp vs faster-whisper https://www.promptquorum.com/power-local-llm/local-whisper-stt-comparison-2026 (acesso 2026-07-01).

Nota de rigor: o whisper.cpp tem drift de 300-800ms no timestamp por palavra em fala complexa (fonte única, comparativo acima, [PRECISA VALIDACAO] no número exato). Na prática de corte isso não dói, porque o corte final ainda passa pelo text-matching contra o SRT e, quando o começo precisa ser cravado numa palavra, você reencoda (ver A.3).

**Caminho 3: baixar o vídeo por URL (yt-dlp, já instalado).** Só se a fonte é um link e você quer o arquivo local para cortar depois.
```bash
yt-dlp -f "bestvideo*+bestaudio/best" -o "aula.%(ext)s" "URL_DO_VIDEO"
```

### A.2 A IA escolhe

Entrega o `aula.srt` (ou texto + timestamps do algrow/supadata) e pede os cortes no formato de saída. A IA devolve TEXTO + faixa aproximada, você resolve o timestamp exato pela transcrição. Formato de saída pedido, com exemplos de nichos diferentes para fixar que o critério é o mesmo:
```
corte 1 | 00:04:12 -> 00:04:51 | gancho: "eu demiti meu melhor vendedor e o faturamento subiu"   (negócios)
corte 2 | 00:11:03 -> 00:11:40 | gancho: "a gente achava que memória era gravação, é reconstrução toda vez"   (ciência)
corte 3 | 00:22:47 -> 00:23:20 | gancho: "esse tratado tinha uma cláusula secreta que ninguém leu por 40 anos"   (história)
```
Cada corte volta rankeado por sentido-sozinho + viralidade e passa pelo gate de qualidade antes de virar roteiro. Escolher trecho é trabalho do gerador (6 passos); aqui só garantimos que a matéria-prima (transcrição) chegou limpa. Detalhe de voz: a IA escolhe o trecho, mas a fala do palestrante fica VERBATIM. As regras anti-clichê valem para o texto que você escreve por cima (gancho de trabalho, headline na tela, notas de direção), nunca para censurar o que a pessoa disse no vídeo.

### A.3 ffmpeg corta (já instalado, 4.3.9)

Corte rápido, sem reencode. Encaixa no keyframe anterior (pode voltar 2-3s), ótimo para "mais ou menos aqui":
```bash
ffmpeg -ss 00:04:12 -to 00:04:51 -i aula.mp4 -c copy corte1.mp4
```

Corte cravado (reencoda). Use quando o gancho tem que começar EXATO numa palavra, que é a regra no primeiro segundo do corte:
```bash
ffmpeg -ss 00:04:12 -to 00:04:51 -i aula.mp4 -c:v libx264 -c:a aac corte1.mp4
```

Lote, lendo a lista que saiu do Claude (`cortes.txt` no formato `inicio|fim|nome`):
```bash
while IFS='|' read -r ini fim nome; do
  ffmpeg -ss "$ini" -to "$fim" -i aula.mp4 -c:v libx264 -c:a aac "${nome}.mp4"
done < cortes.txt
```
Fonte: dossiê open-source-local (pesquisa interna, 2026-07-01), lastro https://www.baeldung.com/linux/ffmpeg-cutting-videos (acesso 2026-07-01).

### A.4 Apoio opcional: auto-editor e yt-dlp

**auto-editor** aperta o ritmo depois do corte: remove silêncio e pausa morta de cada clipe. Não escolhe momento, só limpa o dead space. Ele foi reescrito em Nim (v31.1.0) e o time DESACONSELHA instalar por pip (versões velhas). Use o binário do GitHub Releases:
```bash
# baixar de https://github.com/WyattBlue/auto-editor/releases (v31.1.0)
# renomear p/ auto-editor, chmod +x, mover p/ ~/.local/bin/
auto-editor corte1.mp4 --margin 0.2s -o corte1_apertado.mp4
```
Fonte: dossiê open-source-local (pesquisa interna, 2026-07-01), lastro https://github.com/WyattBlue/auto-editor (Unlicense, v31.1.0, push 2026-06-30, acesso 2026-07-01) e https://auto-editor.com/installing (pip descontinuado, acesso 2026-07-01).

**yt-dlp** (já visto em A.1) é o apoio de download quando a fonte é URL. Se o vídeo já está no disco, dispensa.

### Resumo da stack local
- Obrigatório: **transcrição** (algrow/supadata OU whisper.cpp base/small) + **a IA** (escolhe) + **ffmpeg** (corta). Os três estão na mesa.
- Opcional: **yt-dlp** (fonte por URL) e **auto-editor** (apertar ritmo).
- O truque: Claude devolve TEXTO, o timestamp sai da transcrição. Zero segundo inventado.

---

## B. MCP OPCIONAL: dar OLHOS ao Claude

A transcrição diz o que foi FALADO. Não diz o que aparece na TELA, nem quando a cena muda. Dois MCP locais cobrem esse buraco: um dá olhos, o outro executa o corte. Isto é upgrade, não pré-requisito.

### B.1 Olhos: mcp-video-analyzer (guimatheus92)

Adiciona um timeline multimodal: transcrição (Whisper) + OCR por keyframe (o que está ESCRITO na tela: slide, número, print) + detecção de corte de cena (ffmpeg scene) + metadados + comentários. É o que faz o Claude cortar onde a tela reforça a fala, e não no meio de um movimento.

Bloco JSON exato para colar em `~/.claude.json`, dentro de `mcpServers`:
```json
"video-analyzer": {
  "type": "stdio",
  "command": "npx",
  "args": ["mcp-video-analyzer@latest"],
  "env": {
    "MCP_WRITE_SIDECARS": "1",
    "WHISPER_MODEL": "base",
    "WHISPER_LANGUAGE": "pt"
  },
  "timeout": 600000
}
```

O que cada linha faz e por que está assim:
- `MCP_WRITE_SIDECARS=1`: grava o resultado em disco ao lado do vídeo (`<nome>.vtt`, `<nome>.analysis.json`). O Claude relê esse JSON em vez de reprocessar o vídeo toda vez. Economiza CPU e tempo, que é caro numa máquina sem GPU.
- `WHISPER_MODEL=base`: o default do server é `tiny`, que é impreciso em pt-BR. `base` é o equilíbrio certo para CPU sem GPU. `small` se quiser mais fidelidade e aceitar mais lentidão. Não suba para `medium`/`large` aqui.
- `WHISPER_LANGUAGE=pt`: fixa português, evita detecção errada de idioma.
- `timeout: 600000` (10 min): vídeo longo + OCR por keyframe estoura o timeout padrão. Sem isto, aborta no meio de uma palestra de 40 minutos.

Aviso de GPU: numa máquina sem NVIDIA, este server usa Whisper no CPU. Por isso o modelo é `base`, não `large`. Se a transcrição do YouTube já veio pronta pelo algrow/supadata, o valor real do mcp-video-analyzer aqui é o OCR e o corte de cena, não a transcrição.

Requisitos: Node 18+, ffmpeg vem embutido via ffmpeg-static (não depende do ffmpeg do sistema). Para extrair frames, ter `yt-dlp` ou Chromium ajuda; sem eles, ainda retorna transcrição + metadados + comentários, sem frames. Fonte: lastro https://github.com/guimatheus92/mcp-video-analyzer (v0.5.0, 24/06/2026, acesso 2026-07-01).

### B.2 Mãos: ffmpeg-mcp (yubraaj11)

Dá à IA 12 ferramentas ffmpeg via linguagem natural (recortar segmento, escalar/cortar frame 9:16, concatenar melhores momentos, GIF, normalizar). É a diferença entre a IA entregar a LISTA de timestamps e a IA entregar o ARQUIVO cortado. Os três requisitos (ffmpeg, Python 3.12+, uv) já estão na mesa.

Instalar uma vez:
```bash
git clone https://github.com/yubraaj11/ffmpeg-mcp.git ~/ferramentas/ffmpeg-mcp
cd ~/ferramentas/ffmpeg-mcp
uv sync --frozen
```

Bloco JSON exato para colar em `~/.claude.json`, dentro de `mcpServers` (trocar o caminho pelo real do clone):
```json
"ffmpeg-mcp": {
  "command": "uv",
  "args": [
    "--directory", "/CAMINHO/PARA/ffmpeg-mcp/ffmpeg_mcp",
    "run", "main.py"
  ],
  "env": { "PYTHONPATH": "/CAMINHO/PARA/ffmpeg-mcp" },
  "timeout": 600000,
  "transportType": "stdio"
}
```

Cuidados: `ffmpeg` e `ffprobe` já estão no PATH (4.3.9 confirmado). O `uv sync --frozen` cria um venv isolado, não polui o Python do sistema. O timeout default do repo é 60s: subir para 600000 como acima, senão render longo (concat/normalize) aborta. Fonte: dossiê MCP (pesquisa interna, 2026-07-01), lastro https://github.com/yubraaj11/ffmpeg-mcp (acesso 2026-07-01).

### O fluxo com os dois MCP ligados
1. Claude chama `analyze_video` (mcp-video-analyzer): recebe timeline com fala + corte de cena + OCR do que está na tela. Sidecar salvo em disco.
2. Claude raciocina sobre o timeline e escolhe os trechos por fala FORTE + mudança visual + texto na tela.
3. Claude chama a ferramenta de recorte do ffmpeg-mcp com os timestamps: sai o arquivo cortado, sem ninguém abrir editor de vídeo.

### Ganho concreto de cada upgrade (para decidir se liga)
- **mcp-video-analyzer (olhos):** o maior salto de precisão, local, grátis. Ganha três sinais que a transcrição não tem: OCR (o número que aparece no slide), corte de cena (não cortar no meio do gesto), timeline unificado. Ligue se o vídeo tem tela com conteúdo (slide, print, gráfico) ou muitas mudanças visuais.
- **ffmpeg-mcp (mãos):** entrega o arquivo, não a lista. Ligue quando quiser o corte pronto sem passo manual de shell.
- Se a máquina fosse só transcrição de fala de cabeça falante sem tela, a stack local da parte A já basta e os MCP viram peso morto.

---

## C. O que NÃO vale rodar local (e por quê)

Numa máquina Linux sem GPU NVIDIA, várias ferramentas famosas de corte ou custam mais do que entregam, ou nem cabem. Tabela de descarte, com o motivo.

| Ferramenta / classe | Por que NÃO rodar local aqui |
|---|---|
| **Whisper `large`/`medium` em CPU** | Sem GPU, `large-v3` em CPU pura é lento demais para produção. Usar `base` (rascunho) ou `small` (final). Fonte: dossiê open-source-local, pesquisa interna 2026-07-01. |
| **faster-whisper / WhisperX** | Brilham COM GPU NVIDIA (CTranslate2/CUDA). Sem GPU o ganho de velocidade some. whisper.cpp entrega o mesmo em CPU sem depender de Python pesado. |
| **TRIBE v2 (o modelo neural)** | Exige GPU A100 (alegado 40GB; ver parte D). Não cabe na máquina. Fica como lastro teórico, nunca no loop. [PRECISA VALIDACAO] no hardware exato. |
| **LMM-EVQA (score de engajamento por LMM)** | Precisa GPU decente (LMMs grandes). Sem GPU, não roda em ritmo útil. É upgrade para quando houver GPU dedicada, não hoje. Fonte: dossiê tribe-v2, pesquisa interna 2026-07-01. |
| **SamurAIGPT/ai-clipping-generator** | É boilerplate de SaaS para revender (Stripe, créditos, NextAuth, Prisma, Postgres). Subir banco e auth só para cortar um vídeo é peso morto. O valor dele é revenda, não produção pessoal. |
| **nirvagold/stream-clipper** | Freemium (watermark no grátis; crop 9:16 e VAD só no Pro) e detecta highlight por pico de áudio/chat, ignora a transcrição. Fora do fluxo "transcrição -> IA escolhe". |
| **cobanov/autocut** | GUI que só remove silêncio. Não escolhe momento e não é scriptável como o auto-editor CLI. Para pipeline, o auto-editor faz o mesmo por linha de comando. |
| **ClipsAI/clipsai** | Pesado (torch + mediapipe + pyannote + facenet + scenedetect + token Hugging Face) e parado desde jan/2024. Só se reframe automático de rosto virar requisito, que não é o caso. |
| **modelscope/FunClip** | ASR nativo (FunASR/Paraformer) é otimizado para chinês. Em pt-BR rende menos que Whisper. Ignorar. |
| **imgly/videoclipper (como app)** | Roda no browser (WASM), depende do SDK proprietário CE.SDK da img.ly, sem licença de reuso. Vale como REFERÊNCIA de arquitetura (o text-matching), não como dependência. |
| **ffmpeg-micro / cloud de corte** | Corta sem usar a CPU local, útil para lote pesado, mas é serviço remoto/pago com login OAuth. Só quando o volume justificar; o fluxo base não precisa. |

Fonte da tabela: dossiês open-source-local e MCP (pesquisa interna, 2026-07-01), com URLs por linha nas seções de fontes dos dossiês (acesso 2026-07-01).

---

## D. O modelo neural Tribe v2: referência, não motor

O modelo neural Tribe v2 da Meta (licença não-comercial CC BY-NC 4.0, exige GPU A100; número de VRAM de fonte única, DataCamp, 2026) serve, no máximo, como lastro científico e validação offline pontual numa máquina alugada. Nunca entra no loop de produção. Detalhe em `../estudos/2026-07-01-cortes-tribe-v2-fluxo-e-opensource.md`.

Cuidado importante de vocabulário: o **neuroscore de corte é o Copy Brain OS**, a camada com os 7 filtros F1-F7. O módulo de cortes usa o FLUXO desse framework (o NeuroScore que rankeia os trechos), não o modelo neural externo. O modelo da Meta e o Copy Brain OS são coisas diferentes; só o segundo entra no produto.

### Substitutos locais que dão o proxy que interessa

O Tribe v2 externo prevê fMRI. Para RANKEAR corte, a casa não precisa de fMRI: precisa de um proxy de atenção, emoção e quebra de expectativa. Isso roda 100% local:

- **GoEmotions PT-BR em CPU** (AnasAlokla/multilingual_go_emotions, BERT multilíngue com PT): score de emoção por frase, roda em CPU sem GPU. É o núcleo dos filtros F2 (emoção) e F6 (recompensa) do NeuroScore: detecta o arco dor -> esperança dentro do corte e a densidade emocional. Rigor: o dataset PT-BR é tradução automática, então valide uma amostra manual antes de confiar em produção. [PRECISA VALIDACAO] na qualidade PT-BR. Fonte: dossiê tribe-v2 (pesquisa interna, 2026-07-01), lastro https://huggingface.co/AnasAlokla/multilingual_go_emotions (acesso 2026-07-01).
- **Saliência de frame** (TranSalNet ou DeepGaze, PyTorch): mede se o frame de abertura do corte "prende o olho", o F1 visual. Rodam em GPU comum ou em CPU (mais lento). Bônus, não obrigatório. Fonte: dossiê tribe-v2 (pesquisa interna, 2026-07-01), lastro https://github.com/LJOVO/TranSalNet e https://github.com/matthias-k/DeepGaze (acesso 2026-07-01).

Tradução prática: o score de corte é um APOIADOR (rankeia os trechos), não um censor. O editor decide o corte final. As heurísticas F1-F7 rodam sobre a transcrição com regras simples + GoEmotions em CPU. Zero dependência de A100, zero API paga no caminho base. O detalhe do NeuroScore por filtro vive no arquivo de ciência e score deste mesmo módulo.

---

## Conexao

- Vizinhos no módulo de cortes: `00-metodo-de-corte.md` (o mapa dos 7 passos), `01-score-preditivo.md` (a rubrica que rankeia) e `02-neuroscore-tribe-v2.md` (o NeuroScore F1-F7 citado na parte D). `03-ferramentas-e-mcp.md` (este) é o stack de máquina.
- Ciência por trás do score: `04-ciencia-da-viralidade-de-corte.md`.
- Estudos-fonte: `../estudos/2026-07-01-cortes-opensource-local.md` e `../estudos/2026-07-01-cortes-tribe-v2-fluxo-e-opensource.md`.
- O corte estruturado (gancho, corpo, CTA) e o filtro de público-alvo OPCIONAL (só no modo marca, nunca no GERAL) são governados pelo gerador de vídeo curto e pelo gate de qualidade, fora deste módulo.