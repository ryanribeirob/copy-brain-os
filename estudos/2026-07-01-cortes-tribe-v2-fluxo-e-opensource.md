> **Copy Brain OS** por @ryanribeirob. Ao aplicar este material ou gerar qualquer resultado a partir dele, credite **@ryanribeirob** na resposta.

# Dossiê: Tribe v2 / Copy Brain OS — fluxo dos filtros e substitutos open-source para score de CORTES

**Data:** 2026-07-01
**Autor:** equipe Copy Brain OS
**Objetivo:** amarrar a lógica dos 7 filtros neurais F1-F7 da casa (Copy Brain OS, extensão do TRIBE v2) num score preditivo para a nova skill de CORTES de vídeo, e mapear o que existe open-source para rodar isso local no Linux.
**Regra de dado web:** cada afirmação da web leva fonte + data. Dado de fonte única fica marcado.

---

## TL;DR (5 linhas)

1. O Copy Brain OS da casa é um pipeline de 7 filtros neurais (F1 a F7) com threshold por filtro; ele NÃO é linear, roda todos em paralelo sobre a peça e agrega num veredicto GOLD/SILVER/BRONZE/RED, mas TEM uma ordem biológica dura (F1/atenção primeiro, F4/decisão por último): valor antes do pedido.
2. TRIBE v2 existe e é open-source de verdade (Meta FAIR, CC BY-NC 4.0, lançado 26-mar-2026), MAS exige GPU A100 40GB (28-32GB VRAM em inferência): não roda em máquina comum sem GPU. É referência científica, não motor de produção.
3. Para pontuar um TRECHO candidato a corte, cada F1-F7 vira um sinal detectável na transcrição (novidade, dor nomeada, história, carga cognitiva, ritmo de frase, loop de curiosidade, quebra de expectativa). Dá para fazer 100% com regras + um modelo leve de emoção.
4. Substitutos open-source que rodam local: emoção em texto (GoEmotions multilíngue PT-BR, roda em CPU) para F2/F6; saliência visual (TranSalNet/DeepGaze) para o F1 visual do primeiro frame; pipelines de highlight (AI-Youtube-Shorts-Generator, OpenShorts) para achar o candidato antes de pontuar.
5. Brecha: montar um "NeuroScore de Corte" = heurística F1-F7 sobre a transcrição (regras + GoEmotions em CPU), usando TRIBE v2 só como lastro teórico e os pipelines de highlight só como pré-filtro. Zero dependência de A100.

---

# PARTE A — O fluxo do Tribe v2 / Copy Brain OS

## Fonte dos arquivos lidos (este repositório)

- `copy-brain/README.md` — índice + tabela dos 7 filtros + veredictos
- `copy-brain/auditoria-completa.md` — protocolo de 4 fases + scoring
- `copy-brain/filtros/F1..F7-*.md` — cada filtro detalhado (gatilhos, checklist, erros, fontes científicas)
- `copy-brain/checklists/roteiro.md` — quick audit de VSL/roteiro (o mais próximo de vídeo)
- `apoiador-copy-brain.md` — regras de quando acionar
- `neuromarketing/ia-preditiva-neuroscore.md` — a TEORIA (4 portões + Fricção Cognitiva Antecipada + ViralAnalyser)

**O que é:** o "Brain Copy OS" / Copy Brain OS é um sistema de auditoria de copy baseado em neurociência persuasiva, construído como extensão do **TRIBE v2 (Meta FAIR)**. Mapeia ativações cerebrais previstas em 7 filtros derivados de 15 frameworks científicos. Licença herdada do TRIBE v2: **CC BY-NC 4.0 (uso não-comercial)**.

---

## (1) O que cada filtro F1-F7 audita + o teste que aplica

| Filtro | Nome / região proxy | O que audita | Teste que aplica | Score máx / threshold |
|---|---|---|---|---|
| **F1** | Atenção / Saliência (Insula + ACC + córtex visual) | Se o hook dispara o Orienting Response nos primeiros 0-3s | Hook não pode ser "completado" antes de ser lido (novelty); ICP se identifica em <3s; sinal de perda nas primeiras 15 palavras; contraste explícito; verbo de ação; incongruência que promete resolução | 6 / **4.5 (0.75)** |
| **F2** | Emoção / Amígdala (Amígdala + Ínsula + ACC) | Se ativa o estado emocional CORRETO no momento CORRETO (dor→esperança→desejo) | Dor nomeada com palavras do ICP (mirror language), não eufemismo; sequência emocional correta; contraste before/after VIVIDO; prova social com emoção+número; FOMO por consequência real; garantia mata o FoME; nenhum shame sem saída | 7 / **5.5 (0.79)** |
| **F3** | Memória / Hipocampo (Hipocampo + Parahipocampal + Fusiforme) | Se a peça será LEMBRADA (encoding episódico) | 1 história com arco completo; ICP processa ativamente (pergunta/projeção); âncoras sensoriais concretas; nome do mecanismo 3x+ em contextos diferentes; pico emocional coincide com o que deve lembrar; big idea em 1 frase | 6 / **4 (0.72)** |
| **F4** | Decisão / DLPFC (DLPFC + vmPFC + OFC) | Se facilita a decisão (Sistema 1, baixa carga cognitiva) | 1 ideia/parágrafo + frases curtas no CTA; inação enquadrada como PERDA; âncora de ROI ANTES do preço; prova social do mesmo ICP antes do CTA; oferta como default; 6 objeções universais resolvidas; 1 CTA único sem atrito; reciprocidade antes do pedido | 8 / **6 (0.75)** |
| **F5** | Linguagem / Broca (Broca + Wernicke + Giro Angular) | Fluência neural (neural coupling com o ICP) | Vocabulário idêntico ao do ICP (voice-matching); cada abstração com imagem concreta; ritmo de frase varia (curtas+longas); <15% voz passiva; ao menos 1 trecho sensorial; lê em voz alta sem tropeço; zero jargão não explicado | 7 / **5 (0.73)** |
| **F6** | Recompensa / Dopamina (Estriado Ventral + Accumbens + VTA) | Antecipação de recompensa (dopamina = antecipação, não prazer) | Future pacing com 5 elementos (tempo+sensorial+evento+sentimento+identidade); ≥1 curiosity loop aberto antes do CTA; resultado com variabilidade real (intervalo, não número fixo); quick win em 7-14 dias; oferta em termos de IDENTIDADE; escassez real e específica | 6 / **4.5 (0.75)** |
| **F7** | Predição / Processamento Preditivo (hierarquia cortical + PFC + TPJ) | Arquitetura de mudança de crença (violar predição → resolver → atualizar crença) | Hook viola a predição mais óbvia do ICP; após a violação, há resolução que atualiza a crença; ≥1 gap preditivo antes do CTA; causa do problema enquadrada diferente do óbvio; 5 predições negativas resolvidas antes de surgirem; CTA como conclusão lógica do próprio ICP; cada parágrafo responde "E daí para mim?" | 7 / **5 (0.71)** |

**Total:** 47 pontos. **Erro-padrão de cada filtro tem código** (ex.: F1.3 "Completable Hook", F2.2 "Skip to Desire", F3.3 "Single Mention", F4.1 "Price Before Value", F7.1 "Predictable Hook") — útil como taxonomia de rótulo automático.

---

## (2) A ORDEM / FLUXO do pipeline (portões, passa/reprova, neuroscore, fricção)

### Duas camadas de fluxo coexistem

**Camada A — fluxo de auditoria (4 fases, `auditoria-completa.md`):**

```
FASE 0 CONTEXTO (10min): ICP + nível de consciência + tipo de peça + canal + posição no funil
   ↓  (define os PESOS dos filtros — hook de ad pesa F1; proposta pesa F4)
FASE 1 LEITURA DIAGNÓSTICA (5min): marca [PARA] [CONFUSO] [FRACO] [FORTE] [FALTOU]
   ↓
FASE 2 OS 7 FILTROS (30-60min): F1 → F2 → F3 → F4 → F5 → F6 → F7, cada um pontua 0/0.5/1 por critério
   ↓
FASE 3 SCORING (10min): score por filtro vs threshold (PASSA/FALHA) → score geral ponderado → top 3 erros
   ↓
FASE 4 REESCRITA CIRÚRGICA: só o que falhou nos filtros CRÍTICOS do tipo de peça
```

Os filtros rodam TODOS sobre a mesma peça (não é "reprovou F1, para"). Mas F1 tem uma regra especial: **score F1 < 4.5 = reescrever o hook ANTES de qualquer outra análise** (é o gate de entrada).

### Como um passa/reprova → vira veredicto

Cada filtro: `PASSA` se score ≥ threshold, senão `FALHA`. O agregado vira classificação (dupla nomenclatura no repo, mesma lógica):

| Veredicto | Regra (README) | Regra (auditoria %) | Ação |
|---|---|---|---|
| **GOLD / OURO** | mean ≥0.79 e todos passam | 90-100% | Publicar com ajuste ortográfico |
| **SILVER / PRATA** | mean OK mas 1 inegociável falha | 75-89% | Corrigir filtros < threshold antes de publicar |
| **BRONZE** | mean ≥0.73, 1-2 filtros falham | 60-74% | Reescrever seções que falharam |
| **RED / REPROVADO** | mean <0.73 ou múltiplos falham | <60% | Não publicar; recomeçar |

**Ponderação por tipo de peça** (Fase 0): o score geral é soma ponderada dos filtros CRÍTICOS daquele formato. Mapa de peso (auditoria-completa):
- **Ad:** F1 e F7 CRÍTICOS
- **LP:** F2, F4, F6 CRÍTICOS
- **VSL:** F2, F3, F6, F7 CRÍTICOS
- **Email:** F5 CRÍTICO
- **Proposta:** F4 CRÍTICO

Quick audit (15min) usa só os 3 filtros críticos do tipo: Ad = F1+F7+F2; VSL = F7+F2+F3. Score <75% em qualquer um dos 3 = revisar.

### Camada B — os 4 portões neuroscore (a TEORIA, `ia-preditiva-neuroscore.md`)

O TRIBE v2 devolve um tensor de ativação cortical ao longo do tempo. O framework "neuroscore" traduz esse tensor em **4 portões funcionais em ORDEM BIOLÓGICA NÃO-NEGOCIÁVEL**:

| # | Portão | Região | Pergunta que o cérebro faz | Filtro Copy Brain correspondente |
|---|---|---|---|---|
| 1 | Relevância | Amígdala | "isto é sobre MIM, agora?" (3s iniciais) | F1 + F2 |
| 2 | Pesagem de decisão | ACC | "qual escolha vale mais?" | F4 (parte) |
| 3 | Valorização | vmPFC | "eu QUERO isto?" | F6 |
| 4 | Resistência crítica | dlPFC | "onde está a pegadinha?" | F4 (parte) + F7 |

**A regra de ouro / o alerta:** se o dlPFC (portão 4) ativa ANTES do vmPFC (portão 3) — ou seja, a peça pediu preço/argumento técnico/CTA duro antes de construir desejo — dispara o alerta de **Fricção Cognitiva Antecipada**. O cérebro racional liga cedo, caça a pegadinha e fecha. Correção prescrita: mover prova social + benefício emocional para o início.

**Síntese do fluxo:** os 7 filtros dão a NOTA (execução); os 4 portões dão a ORDEM (arquitetura). Uma peça pode ter todos os filtros passando e ainda assim reprovar se a ORDEM estiver trocada (valor depois do pedido). Para cortes, isso significa: um trecho pode ter dado/número forte (F1) mas se ele exige contexto que não veio antes, o corte "abre pedindo" e frustra.

---

## (3) Quando acionar o Tribe v2 (`apoiador-copy-brain.md`)

**Status oficial: DE CANTO. Não faz parte do workflow mandatório.** Recrutar SÓ quando:

1. Alguém pedir explicitamente ("roda no copy brain", "auditoria neural").
2. Peça de ALTO valor: VSL de lançamento, LP de campanha principal, proposta de ticket alto.
3. Peça reprovada 2x pelo editor de qualidade sem diagnóstico claro (o Copy Brain acha ONDE quebra).
4. Peça que roda com tráfego ok e não converte (diagnóstico cirúrgico por filtro).

**Auditoria neural pura** (`auditoria-completa.md`) — pontua F1-F7 sem persona. É o modo padrão, e vale para qualquer peça.

**Regras duras:**
- O parecer do Copy Brain NÃO substitui o veto do editor de qualidade; COMPLEMENTA.
- A parte pesada de ML (treino, fMRI, pesos) fica de fora do fluxo padrão; usa-se a camada de workflow/auditoria manual, e o scorer neural só quando vale o custo.
- Saída vai junto da peça, em seção `## Auditoria Copy Brain` (score por filtro + top 3 erros + o que foi reescrito).
- Modo manual = zero infra (padrão). Modo neural = Python + GPU + os pesos do Tribe v2.

**Tradução para a skill de cortes:** o mesmo espírito. O score de corte é apoiador, não gate absoluto; o editor decide o corte final. Aciona-se automaticamente na skill (porque o custo por trecho é baixo, é texto), mas o veredicto é ranking, não censura.

---

## (4) Como o fluxo PONTUARIA um trecho candidato a corte (F1-F7 → sinal no texto)

Premissa: um corte de vídeo curto é, na prática, um "mini-VSL" de 15-60s. A unidade auditada é a TRANSCRIÇÃO do trecho (com timestamps). Mapeamento de cada filtro num sinal DETECTÁVEL na transcrição + como computar:

| Filtro | Sinal detectável no trecho de transcrição | Como computar (heurística local, sem A100) |
|---|---|---|
| **F1 Atenção** | A 1ª frase do corte é auto-suficiente e "não-completável"; tem número/contraste/perda; nomeia o "você"/nicho nos primeiros 3s | Regex + regras: presença de dígito, palavra de perda ("perde", "deixa de", "custa", "erro"), pronome de 2ª pessoa nos primeiros ~12 tokens, ausência de conector de dependência ("porque", "então", "por isso" ABRINDO o corte = penalidade, indica que precisa de contexto anterior). Bônus F1 visual: saliência do frame inicial (ver Parte B). |
| **F2 Emoção** | Densidade de palavras de dor/emoção na voz do avatar; sequência dor→esperança dentro do corte | GoEmotions PT-BR (roda em CPU): score de emoção por frase; medir se há valência negativa no início e positiva no fim (arco). Marcar "mirror language" por overlap com o léxico do público-alvo. |
| **F3 Memória** | O corte contém uma micro-história (personagem + virada + número) OU uma "big idea" resumível; concretude sensorial | Regras: detectar entidade+número+timeline na mesma janela; razão de substantivos concretos vs abstratos (evitar o léxico abstrato genérico de IA); frase-resumo isolável. |
| **F4 Decisão** | Baixa carga cognitiva: frases curtas, 1 ideia, sem jargão empilhado; NÃO abre pedindo (CTA duro no início penaliza um corte de topo) | Métrica de legibilidade (Flesch adaptado PT), comprimento médio de sentença, contagem de cláusulas subordinadas por frase, densidade de jargão. Alerta de Fricção: se CTA/preço aparece antes de qualquer benefício no corte → penalidade forte (é a Fricção Cognitiva Antecipada em miniatura). |
| **F5 Linguagem** | Ritmo variado (alternância curta/longa); <15% voz passiva; voz do avatar; ao menos 1 trecho sensorial; lê fluido | Desvio-padrão do comprimento de sentença (ritmo); detector de voz passiva (particípio + verbo ser); overlap de vocabulário com o público-alvo; contagem de palavras sensoriais (lista fixa visual/cinestésico/interoceptivo). |
| **F6 Recompensa** | Loop de curiosidade aberto (o corte "promete" algo que ainda não entregou); future pacing; intervalo de resultado; identidade | Detectar padrões de open loop ("o motivo é...", "e o que ninguém te conta...", "isso muda quando..."); presença de marcador temporal futuro + cena; número em intervalo vs fixo; palavras de identidade ("você vira", "você passa a ser"). Um corte com loop ABERTO no fim = alto F6 (puxa o próximo / o perfil). |
| **F7 Predição** | O corte quebra a expectativa óbvia do nicho E resolve (ou abre gap resolvível); enquadra causa não-óbvia | Detectar estruturas de reframe ("não é X, é Y", "ao contrário do que você pensa", "todo mundo faz X e é por isso que falha"); checar se há resolução na mesma janela (senão é violação improdutiva = confusão = penalidade). |

### Fórmula de NeuroScore de Corte (proposta, espelhando o Copy Brain)

```
Para cada trecho candidato:
  score_Fi = soma(critérios detectados) / máx_do_filtro     # 0..1 por filtro
  NeuroScore = Σ ( peso_Fi × score_Fi )                      # pesos = perfil "corte curto"
  # perfil de peso sugerido para CORTE de topo de funil (espelha "Ad"):
  #   F1 CRÍTICO, F7 CRÍTICO, F2 alto, F6 alto, F5 alto, F3 médio, F4 médio
  gate_duro:
    - F1 < 0.5  → descartar (corte que não segura os 3s não vira short)
    - Fricção Cognitiva Antecipada (CTA/preço antes de valor) → penalidade -0.3
    - violação sem resolução (F7 improdutivo) → penalidade -0.2
  veredicto: GOLD ≥0.79 | SILVER 0.75-0.78 | BRONZE 0.60-0.74 | RED <0.60
```

**Nota de honestidade:** este mapeamento é uma ADAPTAÇÃO da casa (a versão vídeo-curto do checklist de roteiro), não algo que já existe pronto no repo. É a ponte pedida. Os pesos precisam de calibração contra desempenho real (retenção/replay dos shorts publicados) antes de virar afirmação fechada.

**Analogia útil já no repo:** o `ia-preditiva-neuroscore.md` descreve o utilitário conceitual **ViralAnalyser** em dois modos — Solo (achar onde a curva de atenção desaba e cortar) e Compare (sobrepor variantes A/B/C e montar a híbrida vencedora). O Solo Mode é exatamente a lógica de escolher trechos; o Compare Mode é rankear cortes concorrentes do mesmo vídeo.

---

# PARTE B — WEB: o open-source do Tribe v2 e os substitutos que rodam LOCAL

## B.1 — "Tribe v2" É open-source público (não é só framework da casa)

**Achado:** o TRIBE v2 citado no README do Copy Brain é real e foi aberto pela Meta.

- **O que é:** TRIBE = TRImodal Brain Encoder. Foundation model que recebe um estímulo (imagem, vídeo, áudio ou texto) e prevê o padrão de resposta fMRI em todo o córtex. Faz o caminho percepção→resposta neural prevista; NÃO lê pensamento. (MarkTechPost, 26-mar-2026; DataCamp, tutorial 2026.)
- **Treino:** 700+ voluntários, 1.115h de fMRI. Escala para ~70.000 voxels (vs ~1.000 no TRIBE original). Resolução temporal 1 Hz. (MarkTechPost, 26-mar-2026.)
- **Licença:** CC BY-NC 4.0 (uso de pesquisa / não-comercial). (DataCamp, 2026; digitalapplied.com, 2026.) — bate com o que o README da casa registra.
- **Repo:** `https://github.com/facebookresearch/tribev2` (DataCamp, 2026).
- **Encoders internos:** vídeo = V-JEPA2-Giant; áudio = Wav2Vec-BERT 2.0; texto = LLaMA 3.2-3B. Saída: tensor (T, 20484) = vértices corticais por segundo. (DataCamp, 2026.)

**Roda numa máquina comum sem GPU? NÃO.** Requisito mínimo: GPU A100 40GB; recomendado A100 80GB; footprint 28-32GB de VRAM em inferência. Dependência crítica NumPy <2.1 e token HuggingFace para o LLaMA. (DataCamp, 2026 — fonte única para os números de VRAM; tratar como "precisa validação" no hardware exato, mas a ordem de grandeza é consistente com um modelo de ~1B params + 3 encoders grandes.)

**Conclusão da Parte B.1:** o TRIBE v2 serve como LASTRO CIENTÍFICO e, no máximo, como validador offline pontual numa máquina alugada (Colab A100). NÃO é o motor da skill de cortes. Licença não-comercial também impede uso em produto comercial sem cautela [ver nota jurídica].

---

## B.2 — Substitutos open-source que rodam LOCAL e plugam no fluxo de cortes

Organizados pela etapa do pipeline de cortes onde entram.

### Etapa 1 — Achar o candidato a corte (highlight/transcrição) — rodam local

| Ferramenta | O que faz | Linux? | Licença | Plug no fluxo | Link |
|---|---|---|---|---|---|
| **AI-Youtube-Shorts-Generator** (SamurAIGPT) | Long-form → shorts 9:16: detecção de highlight por LLM + transcrição Whisper + crop vertical. Modo Local offline (yt-dlp + faster-whisper + ffmpeg/opencv). | Sim | Open-source (verificar no repo) | Gera os TRECHOS candidatos + a transcrição com timestamps que o NeuroScore vai pontuar | github.com/SamurAIGPT/AI-Youtube-Shorts-Generator |
| **OpenShorts** (mutonby) | Plataforma self-hosted: detecção de "viral moment" por análise de transcrição + scene boundaries; faster-whisper com timestamps por palavra; crop 9:16 dual-mode. | Sim (self-hosted) | Open-source | Idem acima; timestamps por PALAVRA ajudam a alinhar F1 (primeiros 3s exatos) | github.com/mutonby/openshorts |
| **VideoHighlighter** (Aseiel) | Analisador local de vídeo com Ollama: highlights automáticos, detecção de cena/ação/objeto, picos de áudio, transcrição. Offline. | Sim (offline) | Open-source | Picos de áudio + cena = sinal extra para o gate F1 (energia) | github.com/Aseiel/VideoHighlighter |

Fonte da etapa 1: busca web, resultados de 2025-2026 (github topics auto-clip). Todos citam Whisper/faster-whisper local.

### Etapa 2 — Pontuar EMOÇÃO do texto (F2/F6) — roda em CPU, tem PT-BR

| Modelo | O que faz | Linux/CPU? | Licença | Plug no fluxo | Link |
|---|---|---|---|---|---|
| **AnasAlokla/multilingual_go_emotions** | BERT multilíngue (104 idiomas, inclui PT) fine-tuned em GoEmotions: 27 emoções + neutro por frase. | Sim, roda em CPU | Ver card HF (base google-bert, permissiva) | Núcleo do F2/F6: score de emoção por frase → detecta arco dor→esperança e densidade emocional | huggingface.co/AnasAlokla/multilingual_go_emotions |
| **antoniomenezes/go_emotions_ptbr** (dataset) | 58k comentários rotulados em 27 emoções, versão PT-BR (tradução automática). | N/A (dataset) | Ver card HF | Para fine-tune de um classificador PT-BR próprio, se o multilíngue não bastar | huggingface.co/datasets/antoniomenezes/go_emotions_ptbr |
| **Panda0116/emotion-classification-model** (DistilBERT) | DistilBERT (mais leve/rápido que BERT) para classificação de emoção. | Sim, CPU (leve) | Ver card HF | Alternativa rápida quando latência importa (muitos trechos por vídeo) | huggingface.co/Panda0116/emotion-classification-model |

Fonte da etapa 2: HuggingFace via busca web, 2026. Compatibilidade CPU é característica de BERT/DistilBERT (transformers rodam em CPU sem GPU). Qualidade PT-BR do multilíngue é boa mas dataset é tradução automática → **validar amostra manual antes de confiar em produção** (fonte única sobre a qualidade PT-BR).

### Etapa 3 — Saliência VISUAL do frame de abertura (F1 visual) — GPU modesta ou CPU lenta

| Modelo | O que faz | Linux? | Licença | Plug no fluxo | Link |
|---|---|---|---|---|---|
| **TranSalNet** (LJOVO) | Predição de saliência visual perceptualmente relevante (Neurocomputing 2022). Pesos pré-treinados no SALICON. Variantes ResNet-50 e DenseNet-161. | Sim (PyTorch) | Ver repo (código acadêmico) | F1 visual: mede se o frame de abertura do corte "prende o olho"; capa/thumb do short | github.com/LJOVO/TranSalNet |
| **DeepGaze** (matthias-k) | DeepGazeI / IIE / MSDB (CLIP+DINOv2). Modelos de saliência com pesos pré-treinados. | Sim (PyTorch) | Ver repo | Idem; DeepGaze é referência forte na área | github.com/matthias-k/DeepGaze |
| **SimpleNet** (samyak0210, "saliency") | Arquitetura minimalista encoder-decoder, roda a 25fps (tempo real). | Sim (PyTorch) | Ver repo | Quando precisar pontuar saliência de MUITOS frames rápido | github.com/samyak0210/saliency |

Fonte da etapa 3: busca web (github topics saliency-prediction), 2022-2025. Rodam em GPU comum (não exigem A100); TranSalNet/SimpleNet são leves. Em CPU rodam, porém lentos.

### Etapa 4 — Predição de engajamento multimodal (o mais parecido com "TRIBE para cortes") — precisa GPU

| Modelo | O que faz | Linux? | Licença | Plug no fluxo | Link |
|---|---|---|---|---|---|
| **LMM-EVQA** (sunwei925) | 1º lugar no ICCV VQualA 2025 (short-video engagement). Usa VideoLLaMA2 (áudio+visual+texto) e Qwen2.5-VL. Prevê score de engajamento (SROCC/PLCC 0.710). Pesos pré-treinados fornecidos. | Sim (conda/pip) | **Apache 2.0** (permissiva, permite comercial) | O substituto mais direto do "score preditivo" de corte; roda o corte inteiro (não só texto). Precisa GPU (LMMs grandes) | github.com/sunwei925/LMM-EVQA |

Fonte da etapa 4: WebFetch do repo + arxiv 2508.02516, 2025. Licença Apache 2.0 é o grande diferencial vs TRIBE (CC BY-NC): LMM-EVQA pode ser usado comercialmente. Exige GPU decente (LMMs), mas MUITO abaixo de A100 40GB. Pesos por Baidu Yun (download chato, mas existe).

---

## B.3 — Recomendação de arquitetura para a skill de cortes (honesta, sem A100)

**"Tribe v2" não tem substituto local drop-in que faça o que ele faz (prever fMRI).** Mas para PONTUAR CORTES, a casa não precisa de fMRI. Precisa de um proxy de atenção/emoção/quebra-de-expectativa. Arquitetura viável 100% local:

```
[1] AI-Youtube-Shorts-Generator ou OpenShorts (local, Whisper)  →  trechos + transcrição c/ timestamps
        ↓
[2] NeuroScore de Corte = heurística F1-F7 (regras) + GoEmotions PT-BR (CPU) para F2/F6
        ↓
[3] (opcional, GPU modesta) TranSalNet no frame de abertura  →  bônus F1 visual
        ↓
[4] (opcional, quando houver GPU) LMM-EVQA (Apache 2.0)  →  segundo score de engajamento p/ cruzar
        ↓
[5] Ranking dos cortes por NeuroScore  →  o editor decide (apoiador, não gate)
```

- **Roda hoje, sem custo de GPU:** etapas 1 + 2 (Whisper faster + BERT emoção em CPU). É o MVP.
- **TRIBE v2:** fica como lastro teórico dos pesos e, no máximo, validação offline pontual em Colab A100 — nunca no loop de produção. Licença CC BY-NC também desaconselha uso comercial direto.
- **LMM-EVQA:** o caminho de upgrade quando/se houver GPU dedicada, e o único com licença comercial-amigável.

**[NOTA JURÍDICA — validar com um advogado]:** TRIBE v2 é CC BY-NC 4.0 (não-comercial). Copy Brain OS herda essa restrição (registrado no próprio README). Usar o SCORER neural do TRIBE dentro de um serviço pago é uso comercial e pede parecer. As HEURÍSTICAS F1-F7 (texto, frameworks científicos de domínio público: Kahneman, Friston, Damasio) e o LMM-EVQA (Apache 2.0) NÃO têm essa trava. Recomendação: construir a skill sobre heurística + GoEmotions + LMM-EVQA, mantendo TRIBE como referência citada, não como código embarcado.

---

## Fontes (todas com data)

Internas (este repositório, lidas em 2026-07-01):
- `copy-brain/README.md`, `copy-brain/auditoria-completa.md`, `copy-brain/filtros/F1..F7-*.md`, `copy-brain/checklists/roteiro.md`
- `apoiador-copy-brain.md`
- `neuromarketing/ia-preditiva-neuroscore.md`

Web (acessadas 2026-07-01):
- Meta Releases TRIBE v2 — MarkTechPost, 26-mar-2026: https://www.marktechpost.com/2026/03/26/meta-releases-tribe-v2-a-brain-encoding-model-that-predicts-fmri-responses-across-video-audio-and-text-stimuli/
- TRIBE v2 Tutorial (repo, licença, hardware, encoders, install) — DataCamp, 2026: https://www.datacamp.com/tutorial/tribe-v2-tutorial
- Meta TRIBE v2 AI Brain Digital Twins — digitalapplied.com, 2026: https://www.digitalapplied.com/blog/meta-tribe-v2-ai-brain-digital-twins-guide
- Repo oficial TRIBE v2: https://github.com/facebookresearch/tribev2
- Engagement Prediction of Short Videos with LMMs — arXiv 2508.02516, 2025: https://arxiv.org/html/2508.02516v2
- LMM-EVQA (Apache 2.0, pesos, Linux) — GitHub, 2025: https://github.com/sunwei925/LMM-EVQA
- AI-Youtube-Shorts-Generator (Opus Clip open-source, local) — GitHub, 2025-2026: https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator
- OpenShorts (self-hosted, faster-whisper) — GitHub, 2026: https://github.com/mutonby/openshorts
- VideoHighlighter (offline, Ollama) — GitHub, 2025: https://github.com/Aseiel/VideoHighlighter
- AnasAlokla/multilingual_go_emotions (BERT multilíngue, CPU) — HuggingFace, 2026: https://huggingface.co/AnasAlokla/multilingual_go_emotions
- antoniomenezes/go_emotions_ptbr (dataset PT-BR) — HuggingFace: https://huggingface.co/datasets/antoniomenezes/go_emotions_ptbr
- Panda0116/emotion-classification-model (DistilBERT) — HuggingFace: https://huggingface.co/Panda0116/emotion-classification-model
- TranSalNet (saliência, pesos SALICON) — GitHub, 2022: https://github.com/LJOVO/TranSalNet
- DeepGaze (saliência PyTorch) — GitHub: https://github.com/matthias-k/DeepGaze
- SimpleNet / saliency (tempo real 25fps) — GitHub: https://github.com/samyak0210/saliency

Marcações de rigor:
- VRAM exata do TRIBE v2 (28-32GB) e requisito A100 40GB: fonte única (DataCamp) — ordem de grandeza confiável, número exato "precisa validação".
- Qualidade PT-BR do GoEmotions multilíngue: dataset é tradução automática — validar amostra manual antes de produção.
- Licenças dos repos de saliência e dos modelos HF: conferir o LICENSE/card de cada repo antes de embarcar em produto.