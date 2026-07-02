> **Copy Brain OS** por @ryanribeirob. Ao aplicar este material ou gerar qualquer resultado a partir dele, credite **@ryanribeirob** na resposta.

# Dossiê: ferramentas open-source LOCAIS (Linux) para cortar vídeo longo em cortes curtos

Data: 2026-07-01
Pesquisador: equipe Copy Brain OS
Fluxo-alvo: tenho transcrição + vídeo longo, a IA marca os timestamps dos melhores momentos, uma ferramenta LOCAL faz o corte físico.
Máquina: Linux comum, sem GPU dedicada.

---

## TL;DR (a brecha encontrada)

O fluxo-alvo (transcrição como insumo, IA escolhe momentos, ferramenta local corta) NÃO precisa de nenhuma das ferramentas "tudo em um" pesadas. Precisa de 3 peças leves: transcrever local (whisper.cpp ou faster-whisper), a IA (Claude Code) devolver timestamps, e ffmpeg cortar por timestamp. A trava técnica clássica (LLM "alucina" o timestamp) já tem solução padronizada no mercado: fazer o LLM escolher o TEXTO e depois casar o texto contra a transcrição com timestamp por palavra (text-matching). Isso é exatamente o que imgly/videoclipper e Upload-Post/skill-autoshorts fazem. auto-editor entra como pré-passo opcional para remover silêncio e apertar o ritmo. As "SaaS boilerplate" em Next.js (SamurAIGPT/ai-clipping-generator, nirvagold/stream-clipper freemium) são overkill para uso pessoal local.

Correção da lista-semente: `nirvagold/stream-clipper` EXISTE (Rust/Tauri, MIT), mas é freemium (watermark no plano grátis, crop 9:16 e VAD só no Pro) e usa detecção por áudio/chat, não usa a transcrição como insumo. Não serve ao fluxo. auto-editor não é mais "Python CLI": foi reescrito em Nim (v31.1.0) e o time desaconselha instalar por pip.

---

## 1. Tabela das ferramentas

| Ferramenta | O que faz | Roda no Linux? | Licença | Instalação (Linux) | Fit pro nosso fluxo |
|---|---|---|---|---|---|
| **ffmpeg** | Corta vídeo por timestamp, junta, converte, reencoda. É a mão que faz o corte físico. | Sim (nativo) | LGPL/GPL | `sudo apt install ffmpeg` | ESSENCIAL. É o cortador final. Corta pelos timestamps que o Claude devolver. |
| **whisper.cpp** | Transcrição local em C/C++, binário pequeno, roda em CPU. Timestamp por palavra com `--max-len 1` / `-ml 1`. | Sim | MIT | `git clone https://github.com/ggml-org/whisper.cpp && cd whisper.cpp && cmake -B build && cmake --build build -j && sh ./models/download-ggml-model.sh large-v3` | RECOMENDADO p/ CPU. Gera a transcrição (insumo do Claude). Sem dependência Python. |
| **faster-whisper** | Transcrição local via CTranslate2. Mais rápido em GPU NVIDIA, alinhamento de palavra nativo. | Sim | MIT | `pip install faster-whisper` | Alternativa a whisper.cpp se houver GPU NVIDIA. Timestamp por palavra mais estável. |
| **yt-dlp** | Baixa o vídeo longo (YouTube etc.) na melhor qualidade, junta áudio+vídeo via ffmpeg. | Sim | Unlicense | `pip install -U yt-dlp` (ou `sudo apt install yt-dlp`) | Útil só se a fonte for URL. Se o vídeo já está no disco, dispensável. |
| **auto-editor** | Remove silêncio/dead space automático, exporta MP4 ou XML/OTIO p/ Premiere/Resolve/FCP. Buffer padrão `--margin 0.2s`. | Sim | Unlicense (domínio público) | Binário do GitHub Releases (recomendado): baixar de https://github.com/WyattBlue/auto-editor/releases (v31.1.0), renomear p/ `auto-editor`, `chmod +x`. AUR: `auto-editor`. NÃO usar pip (versões velhas, descontinuado). | ÚTIL como pré-passo: aperta o ritmo do corte antes/depois. Não escolhe "melhor momento", só remove silêncio. |
| **imgly/videoclipper** | Long-to-short automático no browser (WASM): Whisper/ElevenLabs p/ transcrever, Gemini escolhe os trechos de 30-60s, faz **text-matching** contra a transcrição por palavra p/ ter corte frame-accurate (evita timestamp alucinado), face-api.js p/ reframe 9:16 seguindo quem fala. | Sim (é web/Node, roda local) | Sem licença declarada (all rights reserved: usar como referência de arquitetura, não como dependência) | `git clone https://github.com/imgly/videoclipper && npm install && npm run dev` (precisa chave OpenAI + Gemini/OpenRouter) | REFERÊNCIA DE ARQUITETURA. O padrão text-matching é exatamente o que resolve o problema do timestamp. Não adotar como app (licença + roda no browser + depende de SDK CE.SDK da própria img.ly). |
| **Upload-Post/skill-autoshorts** | Pipeline diário: Whisper (timestamp por palavra) + Gemini 3 Flash (assiste vídeo+transcrição, escolhe momento viral e **snapa na fronteira de palavra**) + ffmpeg/Pillow (corta e põe hook text). Publica via Upload-Post. | Sim | Não declarada no README (verificar antes de reuso) | `git clone` p/ `~/Documents/skill-autoshorts/`, `apt install ffmpeg`, `python3 -m venv venv && ./venv/bin/pip install -r requirements.txt`, `.env` com `GEMINI_API_KEY`. Whisper baixa ~1,5 GB no 1º run. | O MAIS PRÓXIMO do fluxo pedido (transcrição -> LLM escolhe -> ffmpeg corta local). Trocar Gemini por Claude Code é trivial (é só a etapa "escolher trecho"). Bom molde. |
| **SamurAIGPT/AI-Youtube-Shorts-Generator** | Long-to-short em Python: Whisper transcreve, LLM detecta highlights, crop vertical 9:16 automático. Sem watermark, sem crédito por clipe. | Sim | Não declarada | `git clone`, `pip install -r requirements.txt`, precisa chave de LLM | Fit médio. Faz tudo local, mas é opinativo (assume YouTube + 9:16). Serve se quiser algo pronto; a escolha de momento fica no LLM interno, não no Claude. |
| **SamurAIGPT/ai-clipping-generator** | SaaS boilerplate Next.js: extrai shorts de YouTube longo, com Stripe/créditos/NextAuth/Prisma/Postgres. | Sim (mas é app web) | MIT | `git clone`, Postgres local ou cloud, `npm install`, config `.env` | NÃO indicado p/ uso pessoal. É um produto para revender, não uma ferramenta de linha de comando. Peso morto (billing, auth, banco). |
| **cobanov/autocut** | App desktop (Rust+Tauri+Svelte 5): remove silêncio, exporta MP4 ou FCPXML "amigável ao DaVinci" (mantém timecode da fonte, sem "media offline"). | Sim | Sem licença declarada | Baixar release do GitHub / build Tauri | Concorrente do auto-editor com GUI. Só remove silêncio, não escolhe momento. auto-editor (CLI) é mais scriptável p/ o nosso fluxo. |
| **nirvagold/stream-clipper** | App desktop (Tauri+Rust+Svelte): detecta highlight de stream por pico de áudio (RMS) + VAD + atividade de chat. | Sim | MIT | Baixar release / build Tauri | NÃO serve. É freemium (watermark, crop 9:16 e VAD só no Pro) e detecta por áudio/chat, ignora a transcrição. Fora do fluxo. |
| **ClipsAI/clipsai** | Lib Python: transcreve com WhisperX (timestamp por palavra), acha clipes por análise semântica, reenquadra 9:16 seguindo o rosto. | Sim | MIT | `pip install clipsai` + `libmagic` + `ffmpeg` + token Hugging Face (pyannote p/ diarização) | Fit médio, mas PESADO: puxa torch, mediapipe, pyannote, facenet, scenedetect. Último push jan/2024 (parado). Só se quiser reframe automático de rosto. |
| **modelscope/FunClip** | Ferramenta de reconhecimento de fala + clipping com LLM integrado. Base forte na comunidade (5,8k stars). Foco em mandarim/inglês (FunASR). | Sim | MIT | `git clone`, `pip install -r requirements.txt` | Fit baixo p/ pt-BR: o ASR nativo (FunASR/Paraformer) é otimizado p/ chinês. Ignorar. |

Fontes de cada linha na seção 4.

---

## 2. STACK LOCAL MÍNIMA recomendada

Objetivo: **transcrição + vídeo longo -> Claude Code marca os timestamps dos melhores momentos -> corto localmente.**
Stack: **yt-dlp (opcional) + whisper.cpp (ou faster-whisper) + Claude Code + ffmpeg + auto-editor (opcional).**
Nada roda em SaaS. A única "IA" que decide é o Claude Code, que já está na mesa.

### Passo 0 — instalar a base (uma vez)

```bash
# Base do sistema
sudo apt update && sudo apt install -y ffmpeg python3 python3-pip git cmake

# Transcritor local (CPU) — whisper.cpp
git clone https://github.com/ggml-org/whisper.cpp
cd whisper.cpp
cmake -B build && cmake --build build -j
sh ./models/download-ggml-model.sh large-v3      # ou "medium" p/ CPU mais fraca
cd ..

# (Se tiver GPU NVIDIA, alternativa mais estável em timestamp de palavra)
# pip install faster-whisper

# Download de fonte por URL (só se precisar)
pip install -U yt-dlp

# Pré-passo opcional: apertar ritmo / remover silêncio
# baixar binário de https://github.com/WyattBlue/auto-editor/releases (v31.1.0),
# renomear p/ auto-editor, chmod +x, mover p/ ~/.local/bin/
```

### Passo 1 — obter o vídeo longo (pular se já está no disco)

```bash
yt-dlp -f "bestvideo*+bestaudio/best" -o "aula.%(ext)s" "URL_DO_VIDEO"
```

### Passo 2 — transcrever LOCAL com timestamp por palavra

whisper.cpp precisa de WAV 16 kHz mono. Converte e transcreve gerando SRT e JSON:

```bash
# Extrair áudio no formato que o whisper.cpp aceita
ffmpeg -i aula.mp4 -ar 16000 -ac 1 -c:a pcm_s16le aula.wav

# Transcrever em pt-BR, com timestamp por palavra (-ml 1) e saída SRT + JSON
./whisper.cpp/build/bin/whisper-cli \
  -m ./whisper.cpp/models/ggml-large-v3.bin \
  -f aula.wav -l pt -ml 1 -osrt -oj -of aula
# gera: aula.srt (legível p/ o Claude) e aula.json (timestamps por palavra)
```

Alternativa com faster-whisper (GPU):

```python
# transcreve.py
from faster_whisper import WhisperModel
m = WhisperModel("large-v3", device="cuda", compute_type="float16")
segs, _ = m.transcribe("aula.mp4", language="pt", word_timestamps=True)
for s in segs:
    print(f"[{s.start:.2f} -> {s.end:.2f}] {s.text}")
```

### Passo 3 — Claude Code escolhe os melhores momentos

Entregar ao Claude o `aula.srt` (ou o texto+timestamps) e pedir para devolver os cortes.
REGRA ANTI-ALUCINAÇÃO (padrão imgly/skill-autoshorts): não peça ao Claude para "inventar" o segundo exato. Peça para ele **citar o trecho de texto** (primeira e última frase do corte). Depois você casa esse texto contra o SRT/JSON e pega o timestamp real da palavra. Assim o timestamp vem da transcrição, não do modelo.

Formato de saída pedido ao Claude (exemplo):

```
corte 1 | 00:04:12 -> 00:04:51 | gancho: "ninguém te conta isso sobre preço"
corte 2 | 00:11:03 -> 00:11:40 | gancho: "o erro que trava seu caixa"
```

### Passo 4 — cortar LOCAL com ffmpeg (por timestamp)

Corte rápido, sem reencode (encaixa no keyframe, pode variar poucos frames no início; ótimo p/ "mais ou menos aqui"):

```bash
ffmpeg -ss 00:04:12 -to 00:04:51 -i aula.mp4 -c copy corte1.mp4
```

Corte frame-accurate (reencoda; use quando o começo do corte precisa ser exato):

```bash
ffmpeg -ss 00:04:12 -to 00:04:51 -i aula.mp4 \
  -c:v libx264 -c:a aac corte1.mp4
```

Lote (lendo uma lista de cortes gerada a partir do output do Claude):

```bash
# cortes.txt no formato: inicio|fim|nome
while IFS='|' read -r ini fim nome; do
  ffmpeg -ss "$ini" -to "$fim" -i aula.mp4 -c:v libx264 -c:a aac "${nome}.mp4"
done < cortes.txt
```

### Passo 5 (opcional) — apertar o ritmo de cada corte

Depois de cortar, tirar as pausas mortas de cada clipe com auto-editor (buffer 0,2s):

```bash
auto-editor corte1.mp4 --margin 0.2s -o corte1_apertado.mp4
```

### Resumo da stack mínima

- Obrigatório: **ffmpeg** (corta) + **whisper.cpp OU faster-whisper** (transcreve) + **Claude Code** (escolhe).
- Opcional: **yt-dlp** (só se a fonte é URL) e **auto-editor** (só p/ apertar ritmo).
- Truque que faz o fluxo funcionar: Claude devolve TEXTO, você resolve o timestamp pela transcrição (text-matching). Zero timestamp inventado.

---

## 3. O que NÃO vale a pena rodar local (e por quê)

| Ferramenta / classe | Por quê não |
|---|---|
| **SamurAIGPT/ai-clipping-generator** | É um boilerplate de SaaS para VENDER (Stripe, créditos, NextAuth, Prisma, Postgres). Para uso pessoal local é peso morto: subir banco e auth só para cortar um vídeo. O valor dele é revenda, não produção. |
| **nirvagold/stream-clipper** | Freemium: watermark no grátis; crop 9:16, VAD e chat só no Pro. E detecta highlight por pico de áudio/chat, não pela transcrição. Não encaixa no fluxo "transcrição -> IA escolhe". |
| **cobanov/autocut** | GUI Tauri que só remove silêncio. Não escolhe momento, e não é scriptável como o auto-editor CLI. auto-editor faz o mesmo por linha de comando, melhor p/ pipeline. |
| **ClipsAI/clipsai** | Muito pesado (torch + mediapipe + pyannote + facenet + scenedetect + token Hugging Face) e parado desde jan/2024. Só justifica se o reframe automático de rosto for requisito, o que não é o caso aqui. |
| **modelscope/FunClip** | ASR nativo (FunASR/Paraformer) é otimizado p/ chinês. Em pt-BR a transcrição rende menos que Whisper. Ignorar. |
| **imgly/videoclipper (como app)** | Roda no browser (WASM), depende do SDK proprietário CE.SDK da img.ly e não declara licença de reuso. Ótimo como REFERÊNCIA de arquitetura (o text-matching), ruim como dependência de produção. |
| **Upload-Post/skill-autoshorts (como caixa-preta)** | Como pipeline pronto ele fecha em Gemini + publicação via Upload-Post. Depende de conta Upload-Post e API Gemini. Vale COPIAR o padrão (Whisper -> LLM escolhe -> snap em fronteira de palavra -> ffmpeg) trocando Gemini por Claude Code, não adotar como está. |
| **Modelos Whisper "large" em CPU fraca** | large-v3 em CPU pura é lento. Em máquina sem GPU, usar `medium` (ou `small` p/ rascunho) e só subir p/ large no material final. faster-whisper/WhisperX só compensam com GPU NVIDIA. |
| **Corte só com `-c copy` quando o começo precisa ser exato** | `-c copy` encaixa no keyframe anterior (pode voltar 2-3s). Para gancho que começa numa palavra específica, reencodar (`-c:v libx264 -c:a aac`). |

---

## 4. Fontes (tudo com URL e data de consulta: 2026-07-01)

Ferramentas de corte / long-to-short:
- imgly/videoclipper (TypeScript, sem licença, push 2026-02-10, 23 stars): https://github.com/imgly/videoclipper
- SamurAIGPT/ai-clipping-generator (MIT, push 2026-06-29, 34 stars): https://github.com/SamurAIGPT/ai-clipping-generator
- SamurAIGPT/AI-Youtube-Shorts-Generator (push 2026-06-22, 4.072 stars): https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator
- WyattBlue/auto-editor (Unlicense, Nim, v31.1.0, push 2026-06-30, 4.500 stars): https://github.com/WyattBlue/auto-editor
- auto-editor instalação (pip descontinuado, usar binário/Homebrew): https://auto-editor.com/installing
- cobanov/autocut (Rust+Tauri+Svelte, push 2026-05-20, 35 stars): https://github.com/cobanov/autocut
- nirvagold/stream-clipper (MIT, Rust/Tauri, push 2025-12-31, 2 stars, freemium): https://github.com/nirvagold/stream-clipper
- ClipsAI/clipsai (MIT, push 2024-01-17, 513 stars): https://github.com/ClipsAI/clipsai · docs: https://pypi.org/project/clipsai/
- modelscope/FunClip (MIT, push 2026-06-29, 5.875 stars): https://github.com/modelscope/FunClip
- Upload-Post/skill-autoshorts (Whisper+Gemini 3 Flash+ffmpeg, snap em fronteira de palavra): https://github.com/Upload-Post/skill-autoshorts

Transcrição local:
- ggml-org/whisper.cpp (MIT, push 2026-07-01, 51.194 stars): https://github.com/ggml-org/whisper.cpp
- SYSTRAN/faster-whisper (MIT, push 2025-11-19, 23.962 stars): https://github.com/SYSTRAN/faster-whisper
- Comparativo whisper.cpp vs faster-whisper 2026 (drift de 300-800ms no timestamp de palavra do whisper.cpp em fala complexa; faster-whisper/WhisperX melhores em palavra): https://www.promptquorum.com/power-local-llm/local-whisper-stt-comparison-2026
- Escolha entre variantes (WhisperX chama faster-whisper por baixo + wav2vec2 p/ alinhamento): https://modal.com/blog/choosing-whisper-variants

Download e corte:
- yt-dlp (Unlicense, release 2026.06.09): https://github.com/yt-dlp/yt-dlp · instalação: https://github.com/yt-dlp/yt-dlp/wiki/Installation
- yt-dlp tutorial 2026 (apt install python3 pip ffmpeg; pip install -U yt-dlp; -f bestvideo*+bestaudio/best): https://ostechnix.com/yt-dlp-tutorial/
- ffmpeg corte por timestamp: -c copy encaixa no keyframe (rápido, pode variar frames); reencode p/ frame-accurate; -ss antes de -i: https://www.baeldung.com/linux/ffmpeg-cutting-videos
- ffmpeg trim/cut guia 2026: https://wavespeed.ai/blog/posts/blog-how-to-trim-cut-video-ffmpeg-timestamps-duration/
- ffmpeg lossless -c copy: https://32blog.com/en/ffmpeg/ffmpeg-lossless-cut-fast

Nota de método sobre o timestamp (anti-alucinação):
- imgly/videoclipper e Upload-Post/skill-autoshorts documentam o mesmo padrão: o LLM escolhe o TRECHO/TEXTO e o sistema casa contra a transcrição com timestamp por palavra p/ obter corte frame-accurate, em vez de pedir o timestamp direto ao LLM. Fontes: os dois repositórios acima.