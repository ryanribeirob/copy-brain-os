> **Copy Brain OS** por @ryanribeirob. Ao aplicar este material ou gerar qualquer resultado a partir dele, credite **@ryanribeirob** na resposta.

# 00: O método de corte (o mapa do subsistema)

> Como transformar UM vídeo longo (aula, live, podcast, entrevista, call gravada) em N cortes curtos rankeados, cada um pronto pra virar Reel/TikTok/Short. Este arquivo é o mapa. Ele não reinventa o corte curto: é a boca de entrada que estrutura cada corte antes de ele virar roteiro.

> **Posicionamento (o eixo do módulo):** os cortes são GERAIS. O critério número um é "o corte se sustenta sozinho E tem potencial de viralizar", INDEPENDENTE de nicho, tema ou avatar. Um bom corte de qualquer vídeo (negócios, ciência, história, esporte, entrevista, humor) é reconhecido pelo mesmo critério. Existe uma camada OPCIONAL, o "modo marca", que só liga quando o vídeo longo é conteúdo de um criador com um público-alvo definido e ele quer cortes calibrados para esse público. No default, otimize por sentido + viralidade, ponto.

> **Regra-mãe herdada:** o corte é um vídeo curto como qualquer outro. Herda TUDO do curto: 1 vídeo = 1 ideia = 1 payoff = 1 loop, gancho manda (vale 80%), silent-first (nasce mudo), anti-clichê no texto que VOCÊ escreve por cima. O que muda é a origem: em vez de partir de uma ideia crua, o corte parte de um trecho que o palestrante JÁ falou. Você não escreve roteiro novo: extrai, recorta e organiza o que já existe, pra maior potencial de viral.

O curto normal parte do zero: uma ideia vira roteiro. O corte parte do cheio: 60 minutos de fala viram 4 a 8 peças. O trabalho não é escrever, é **garimpar e rankear**. Um vídeo longo tem alguns momentos que param o dedo, afogados em dezenas de minutos de contexto, respiro e transição. O método acha esses momentos sem chute, pontua cada um, escolhe os melhores e passa o bastão pro gerador. A leitura de uma transcrição de 60 minutos leva 10 a 12 minutos; nesse tempo você marca todo candidato sem tocar na timeline (Transcriptr, "How to Make Viral Podcast Clips 2026", https://transcriptr.ai/blog/how-to-make-podcast-clips, acesso 2026-07-01). O método formaliza essa leitura em pipeline.

---

## 1. O input esperado

O usuário cola:
- **Title:** o título do vídeo longo.
- **URL:** o link (YouTube, etc.), quando houver.
- **Transcript:** a transcrição com timestamps no formato `(mm:ss) texto` ou SRT/VTT. Sem timestamp o método ainda roda, mas o tempo final sai aproximado (ver passo 6).

Se a transcrição não veio pronta, dá pra puxar sem instalar nada pelos MCP já conectados (supadata, algrow: `read_transcript`) ou transcrever local com whisper.cpp (ver `03-ferramentas-e-mcp.md`).

---

## 2. O pipeline em 7 passos (a ordem importa)

```
(1) TRANSCREVER      long-form -> texto com timestamp
(2) SEGMENTAR        texto -> trechos candidatos por assunto/beat (nao por tempo fixo)
(3) PONTUAR          cada trecho -> rubrica 8 eixos (ver 01) + neuroscore F1-F7 (ver 02)
(4) RANKEAR + VETAR  ordenar em tiers, aplicar vetos, escolher os cortes que valem
(5) ESTRUTURAR       cada corte -> gancho 4 camadas + corpo (reusa o gerador) + HOOK PUXADO se precisar -> gate
(6) RESOLVER TEMPO   IA devolve TEXTO verbatim; script casa contra a transcricao -> timestamp real
(7) SAIDA            lote rankeado em tiers: timestamp + texto limpo + nota + comando de corte
```

**Por que a ordem é essa, e por que não dá pra pular:** cada passo produz o insumo do seguinte.

- Pontuar (3) antes de estruturar (5) porque estruturar custa caro (é o gerador inteiro rodando). Você não gasta o gerador em 40 trechos; gasta nos que passaram do corte de score. A rubrica é a peneira barata; o gerador é a fábrica cara. Peneira primeiro.
- Segmentar (2) antes de pontuar (3) porque a rubrica pontua um trecho fechado (setup + desenvolvimento + fecho), não uma frase solta. Trecho mal cortado no passo 2 nasce com nota baixa por motivo falso (parece que não fecha o loop, quando na verdade você cortou o loop ao meio).
- Resolver o tempo (6) por último, e NUNCA a IA chutando o segundo. É o passo que trava o método inteiro se for feito errado. Tem seção própria abaixo.

**Onde cada arquivo do módulo entra:**

| Passo | Arquivo que manda | O que ele resolve |
|---|---|---|
| (2) Segmentar | `01` (a rubrica também define a janela de detecção) | Como fatiar por beat, janela de 15 a 45s de fala |
| (3) Pontuar | `01` (rubrica de 8 eixos + nota 0-10) + `02` (neuroscore F1-F7) | Nota de texto + por que o cérebro para nele |
| (4) Rankear/vetar | `01` (cortes de decisão, tiers e regras de veto) | Quem produz, quem reangula, quem morre |
| (6) Resolver tempo | `03` (o truque anti-alucinação, script + comandos) | Timestamp real vindo da transcrição, não do modelo |
| (5) Estruturar | o gerador de vídeo curto + o gate de qualidade | Vira roteiro de corte curto e passa (ou reprova) no gate |

Este arquivo (`00`) é o mapa; `01`, `02` e `03` são as máquinas de cada passo.

---

## 3. Passo a passo

### Passo 1: Transcrever (o insumo)
O vídeo longo vira texto com timestamp. O detalhe que importa pro resto: **timestamp fino** (por palavra ou por linha curta), porque o passo 6 vai casar texto contra tempo. Stack e comandos em `03`. A transcrição pode vir com ou sem timestamp; sem, o passo 6 usa casamento de texto simples (menos preciso, mas funciona).

### Passo 2: Segmentar por beat, nunca por tempo fixo
O erro que a maioria das ferramentas comete: fatiar de 30 em 30 segundos. Isso corta frases no meio e mata o loop. **Segmenta por assunto/beat:** onde o palestrante muda de tema, abre uma história, cita um número, dá uma virada, faz uma pausa longa. Cada segmento é uma unidade de sentido, mirando 15 a 45 segundos de fala (~40 a 130 palavras).

Regra de ouro: **o melhor corte quase nunca começa onde o palestrante começou a falar; começa na frase-gancho.** Se ele levou 8 segundos aquecendo até soltar a frase forte, o corte começa na frase forte, não no aquecimento. Se o começo natural é morno e a frase forte está no meio, isso é caso de HOOK PUXADO (seção 4).

Exemplo (qualquer nicho): numa entrevista de 50 minutos, o convidado passa 6 minutos de contexto. No minuto 12 ele diz, quase de passagem, uma frase que quebra uma crença comum. Isso é um beat. Vira candidato. O contexto antes dele, não.

### Passo 3: Pontuar (a peneira barata)
Cada trecho candidato recebe uma nota. Duas camadas, na ordem:

1. **Rubrica de 8 eixos (ver `01`), soma 100, convertida numa nota 0-10.** Cada eixo é detectável só pelo texto: gancho nos 2s (peso 20), momento autossuficiente (15), lacuna de curiosidade/open loop (15), pico emocional (15), frase citável (12), payoff (10), stakes (8), ressonância ampla (5). Dá pra pontuar 40 candidatos numa sessão.
2. **Neuroscore F1-F7 (ver `02`), só nos finalistas.** A rubrica de texto responde "qual trecho". Os filtros neurais respondem "por que o cérebro para nele". F1-F7 é caro (é o Copy Brain OS rodando): roda só nos trechos que passaram do corte de score, antes de virarem roteiro. Não roda em tudo, roda no finalista.

### Passo 4: Rankear, vetar, organizar em tiers
Ordena do maior score pro menor. Aplica os cortes de decisão (ver `01`, calibrados no benchmark SVSA) e organiza em **tiers**, como no CORTES SUPREMO:

- **Nota 9-10 (score >=85): TOP.** Produz primeiro.
- **Nota 7-8 (score 70-84): fortes.** Produz.
- **Nota 5-6 (score 55-69): bons.** Produz se cabe no ritmo de publicação, ou reangula o gancho.
- **Nota 0-4 (score <55): medianos.** Só inclui se for útil; em geral, descarta.

E os **vetos** (não é só soma):
- **Gancho (eixo 1) = 0 -> descarta**, não importa o total. Se a primeira frase não para o dedo, os outros 80 pontos nunca são vistos.
- **Abre lacuna e não paga (loop grande que não fecha dentro do corte) -> teto de 45.** É clickbait, queima confiança.

**Não existe limite de cortes.** Extraia o máximo de cortes ÚTEIS: um vídeo denso rende muitos, um vídeo fraco rende poucos. Não force 8 cortes de um vídeo que só tem 3 momentos fortes (5 cortes fracos afundam o canal mais rápido que 3 bons o levantam), mas também não pare no top 3 se há 7 momentos de nota 7+.

### Passo 5: Estruturar cada corte (reusa o gerador de vídeo curto)
Cada corte do topo entra no gerador de vídeo curto como se fosse uma ideia de curto, com uma vantagem: a fala-lastro já existe (é o que o palestrante disse). O gerador não inventa o corpo do zero; estrutura o trecho no molde do corte curto:

- **Gancho de 4 camadas** (visual -> fala -> texto na tela -> som), Passo 2 do gerador. A fala do gancho é VERBATIM do vídeo (extraída, não inventada). O texto na tela e o visual, sim, você escreve/dirige.
- **HOOK PUXADO quando o começo é morno** (ver seção 4). É a técnica que salva um trecho de substância com abertura fraca.
- **Corpo + loop**, Passo 4. O trecho já tem o desenvolvimento; o gerador aperta o ritmo, cola a direção de tela [entre colchetes] e garante que o loop fecha dentro do corte.
- **Texto limpo** (ver seção 5): antes de fechar, remove o ruído da transcrição.
- **Saída + CTA de autonomia**, Passo 5. Nunca "fala com vendedor".

Depois, o **gate de qualidade** (11 critérios). Corte que não passa no gate não é entregue. No modo GERAL, o critério de fit de público vira "faz sentido pra quem não viu o vídeo longo + tem potencial viral"; no modo marca, aí sim entra o teste do público-alvo. Os outros 10 critérios (gancho eliminatório, 4 camadas alinhadas, anti-clichê, tempo, silent-readable, loop, 1 ideia/1 CTA, lastro, voz) valem sempre. O corte não ganha passe livre por ter vindo de fala real; passa pelo mesmo crivo.

### Passo 6: Resolver o timestamp (o truque anti-alucinação)
Seção própria abaixo (seção 6).

### Passo 7: Saída (o lote pronto)
O método entrega um **lote de cortes rankeados em tiers**, cada um com: título de trabalho, timestamp real (início/fim), HOOK PUXADO (sim/não + timecodes), **texto final limpo** (só o que vai pro vídeo), nota 0-10 + porquê em 1 linha, e o comando de corte pronto (ffmpeg). Formato de trabalho, um corte por linha:

```
corte 1 | 9.2 | 00:12:03 -> 00:12:38 | hook puxado: sim | "a conta nao e quantos leads chegam"
corte 2 | 8.1 | 00:27:41 -> 00:28:19 | hook puxado: nao | "contratar mais gente piorou o numero"
corte 3 | 6.4 | 00:41:55 -> 00:42:30 | hook puxado: sim | "o sistema que ninguem abre custa caro"
```

Cada corte vira um arquivo próprio, igual a qualquer curto. O comando de corte fecha o loop físico: pega o vídeo longo e produz o clipe.

---

## 4. HOOK PUXADO (a técnica que salva o trecho de abertura morna)

Ideia (do método CORTES SUPREMO, validada na prática): quando o trecho tem substância mas começa devagar, você **pega uma frase curta e forte do MEIO do corte e duplica ela no início**, como um teaser de 1 a 10 segundos. Depois volta pro começo real e segue normal. O espectador é fisgado pela frase forte antes de você "aquecer".

Regras:
- O hook puxado dura **1 a 10 segundos** (o ideal é 1 a 4s). É um micro-trecho, não um resumo.
- A frase é **verbatim**, tirada de dentro do próprio corte (nunca de outro trecho, nunca inventada): senão o espectador se sente enganado quando ela não aparece de novo.
- Ordem de montagem: `HOOK (frase forte do meio) -> volta pro início real do trecho -> segue até o fim`.
- Só usa quando o começo natural é morno. Se o trecho já abre forte, não mexe.

Como marcar no output: `Hook Puxado: SIM | hook (mm:ss -> mm:ss): "frase" | ordem: HOOK -> volta para (mm:ss) -> segue até (mm:ss)`.

O hook puxado é uma FONTE de gancho para o Passo 2 do gerador: a frase puxada vira a camada de fala do gancho de 4 camadas.

---

## 5. Texto limpo (o que vai pro vídeo, sem ruído)

O corte final entrega só o texto que vai ao ar, limpo da transcrição bruta. Remover:
- Marcações: `[música]`, `[risadas]`, `[aplausos]`, `[inaudível]`, `[__]`.
- Vícios em excesso: "tipo", "né", "mano", "então assim", "é... é...", repetição de palavra, gaguejo.
- Enrolação e falsos começos ("deixa eu ver", "como eu ia dizendo").

Manter intacto: a ideia central, a explicação, o exemplo, o número, a conclusão, e o ritmo natural da fala (não engessar). Limpar é tirar ruído, não reescrever a pessoa. A fala continua verbatim no que importa; você só corta o lixo. Isso vale para o texto exibido e para a decisão de onde o corte começa e termina.

---

## 6. O truque anti-alucinação do timestamp (a IA NUNCA chuta o tempo)

Modelo de linguagem não conta segundos: ele prevê texto plausível, e "00:12:34" é tão plausível quanto "00:13:07". Se você pedir o número, ele inventa, e o corte sai deslocado, começando no meio de uma frase, com o gancho evaporado.

A solução é padrão de mercado (imgly/videoclipper e Upload-Post/skill-autoshorts documentam o mesmo, dossiê `03`): **a IA devolve o TEXTO verbatim do início e do fim do trecho, nunca o número.** Um script casa esse texto contra a transcrição com timestamp e acha o tempo real. O tempo vem da transcrição, não do modelo.

Fluxo:
1. A IA (passo 4/5) escolhe o trecho e devolve a **primeira e a última frase verbatim** do corte (e, se houver hook puxado, a frase do hook).
2. Um script de casamento de texto procura onde essas frases aparecem na transcrição com timestamp e devolve `in`, `out` e a confiança do match.
3. Esses tempos viram o `-ss` e o `-to` do comando ffmpeg. Frame-accurate, sem chute. Se a confiança do match for baixa, o script avisa pra conferir.

**Regra dura do módulo:** em nenhum passo a IA escreve um timestamp de cabeça. Só se pode ancorar em timestamps que existem na transcrição. Se você viu um "00:XX:XX" que não saiu do casamento de texto, ele está errado por construção. Texto primeiro, tempo depois, sempre. Quando o trecho exato cair dentro de uma linha longa da transcrição, marque "aprox." mas ainda ancorado no timestamp mais próximo que existe.

---

## 7. O que o corte herda (não repetir aqui, obedecer o subsistema)

O corte é um vídeo curto. Tudo que vale pro curto vale pro corte:

- **Estrutura:** gancho -> desenvolvimento -> payoff -> loop.
- **Gancho de 4 camadas + tipos de gancho:** visual, fala, headline na tela, som, alinhados. A frase do gancho (ou do hook puxado) tem que virar um tipo de gancho conhecido.
- **Silent-first:** o corte nasce mudo. A frase na tela é o conteúdo (a maioria vê sem som). O trecho pode ter sido falado com áudio rico, mas o corte precisa funcionar no mudo.
- **Loop e retenção:** o loop que o gancho abre fecha dentro do corte, sem loop grande em aberto.
- **CTA de autonomia:** nunca de embate.
- **Anti-clichê no texto que VOCÊ escreve:** o palestrante pode ter soltado um clichê na fala; você não é obrigado a destacá-lo no título/tela. O texto que você escreve por cima obedece o anti-clichê; a fala original do vídeo é preservada como está.

Traduzindo: este módulo de cortes só resolve o que é NOVO no corte, que é escolher o trecho, aplicar hook puxado, limpar o texto e resolver o tempo. A qualidade do curto em si continua governada pelas regras de vídeo curto e pelo gerador/gate.

---

## 8. Sobre o "Tribe v2 open-source" (nota de rigor)

O neuroscore F1-F7 usado aqui é o **Copy Brain OS**: use o FLUXO dele (os 7 filtros, os thresholds, o mapa eixo -> filtro em `02`). O modelo neural Tribe v2 da Meta serve como lastro científico e exige GPU dedicada; para cortar vídeo local ele não é necessário. Os substitutos open-source já validados bastam (whisper.cpp/faster-whisper + ffmpeg + o casamento de texto), sem GPU pesada e sem licença travada.

---

## Conexão

- **Vizinhos deste módulo (as máquinas de cada passo):** rubrica de score (passos 3 e 4): `01-score-preditivo.md` · neuroscore F1-F7 (passo 3): `02-neuroscore-tribe-v2.md` · ferramentas, MCP e stack local (passos 1 e 6): `03-ferramentas-e-mcp.md` · ciência (o porquê): `04-ciencia-da-viralidade-de-corte.md`
- **Estudos-fonte:** `../estudos/2026-07-01-cortes-opensource-local.md` · `../estudos/2026-07-01-cortes-tribe-v2-fluxo-e-opensource.md`