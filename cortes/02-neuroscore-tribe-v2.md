> **Copy Brain OS** por @ryanribeirob. Ao aplicar este material ou gerar qualquer resultado a partir dele, credite **@ryanribeirob** na resposta.

# NeuroScore F1-F7 (Tribe v2 / Copy Brain OS) aplicado a um trecho candidato a corte

> Segundo arquivo do módulo de cortes. O `01` acha e rankeia os trechos por uma rubrica de eixos observáveis. Este `02` é o gate NEURAL que confirma ou reprova o topo dessa lista: por que um trecho segura o cérebro de quem rola o feed, e onde ele quebra. Carregar só quando for pontuar cortes de um vídeo longo, não no boot.

> **Eixo do módulo:** o corte é GERAL. O critério é um só: o trecho faz sentido sozinho (fora do vídeo longo) E tem potencial de viralizar. Vale pra corte de negócios, de ciência, de entrevista, de história, de esporte, de humor. O NeuroScore mede SENTIDO + VIRALIDADE, não fit de nicho. O fit de público-alvo é uma camada OPCIONAL, ligada só no "modo marca" (quando o vídeo-fonte é conteúdo de um criador com público-alvo definido e ele quer cortes calibrados para esse público). No modo GERAL, que é o default, não se filtra por avatar.

Você tem um vídeo longo. Trinta minutos de fala. Dentro dele existem, digamos, doze trechos que dariam corte. Cortar os doze e jogar no feed é desperdício: metade morre nos 2 primeiros segundos porque abre pedindo contexto que ficou pra trás. A pergunta não é "esse trecho é bom". É "esse trecho, isolado em 30 segundos, prende o cérebro de qualquer pessoa rolando o feed". O NeuroScore responde isso antes de você gerar a legenda.

O NeuroScore não é nota de gosto. É uma leitura de como o cérebro processa o trecho, filtro por filtro, na ordem em que ele processa de verdade. O cérebro é o mesmo pra corte de dono de empresa, de físico explicando buraco negro, de historiador contando uma guerra ou de jogador narrando o gol. Isso vem do Copy Brain OS (camada construída sobre o TRIBE v2, Meta FAIR).

**Aviso de rigor sobre o Tribe v2:** o modelo neural Tribe v2 da Meta (licença CC BY-NC 4.0 não-comercial, exige GPU dedicada) entra aqui só como referência científica, nunca como código embarcado no loop de corte. O que se usa é o FLUXO do Copy Brain OS (texto sobre a transcrição), não o modelo neural. Fonte da atribuição: DataCamp, 2026, https://www.datacamp.com/tutorial/tribe-v2-tutorial e MarkTechPost, 26-mar-2026, https://www.marktechpost.com/2026/03/26/meta-releases-tribe-v2-a-brain-encoding-model-that-predicts-fmri-responses-across-video-audio-and-text-stimuli/.

---

## O que é o NeuroScore (em uma frase de operador)

Um corte de vídeo curto é, na prática, um mini-VSL de 15 a 60 segundos. A unidade que a gente audita é a TRANSCRIÇÃO do trecho, com timestamps. O NeuroScore roda os 7 filtros neurais F1-F7 sobre essa transcrição, agrega num veredicto GOLD/SILVER/BRONZE/RED, e checa uma ordem biológica dura: valor antes do pedido. Se a ordem inverte, dispara um alerta específico (Fricção Cognitiva Antecipada) e o trecho cai, mesmo com número forte.

O NeuroScore audita o TEXTO que você escreve por cima do corte (título de trabalho, headline na tela, notas de direção) e o SENTIDO do trecho escolhido. Ele não reescreve a fala do palestrante do vídeo-fonte: a fala é verbatim, você só escolhe onde começa e onde termina. As regras anti-clichê valem pro que você escreve, não pra censurar quem falou no vídeo original.

Fonte do fluxo: `../copy-brain/README.md`, `../copy-brain/auditoria-completa.md`, `../copy-brain/filtros/F1..F7-*.md`, `../copy-brain/checklists/roteiro.md`. Teoria (4 portões + Fricção): `../neuromarketing/ia-preditiva-neuroscore.md`.

---

## Os 7 filtros: o que cada um audita, o teste que aplica, e o sinal no corte

Cada filtro pontua de 0 a 1 (soma de critérios detectados dividida pelo máximo do filtro). O threshold vem do Copy Brain OS. A coluna que mais importa aqui é a última: o SINAL detectável na transcrição do trecho, porque é isso que você olha num corte antes de gerar a legenda. Os exemplos são de nichos VARIADOS de propósito: o critério é genérico.

### F1 Atenção (Ínsula + ACC + córtex visual): threshold 0.75

Audita se o corte dispara o Orienting Response nos primeiros 0-3s. O teste: a primeira frase não pode ser "completável" antes de ser lida (novidade); o espectador se identifica ou se surpreende em menos de 3s; há sinal de perda, aposta ou stakes nas primeiras 15 palavras; contraste explícito; verbo de ação.

Sinal no corte: a 1ª frase é autossuficiente e não pede contexto de antes. Tem dígito, ou palavra de aposta/perda/extremo ("nunca", "todo mundo erra", "custa", "quase morreu", "recorde"), ou uma quebra que o cérebro precisa resolver, nos primeiros ~12 tokens. Sinal de alarme: o corte ABRE com conector de dependência ("porque", "então", "por isso", "aí", "voltando"), o que trai que o pedaço anterior segurava o sentido. Isso é F1 quebrado: o espectador cai no meio de uma conversa e some.

- Forte (ciência): "Se você cair num buraco negro, os seus pés envelhecem mais devagar que a sua cabeça." Contraintuitivo, cena, autossuficiente.
- Forte (esporte): "Esse gol foi marcado do meio de campo, e o goleiro não deu um passo." Número implícito, imagem, sem depender de nada anterior.
- Forte (negócios): "Esse cara faturou R$4,6 milhões e não tirou um centavo de lucro." Número quebrado, contradição, cena.
- Fraco: abre com "Então, como eu tava dizendo, o problema é esse." Puro F1.3 (hook completável / dependente): não vira corte, em nenhum nicho.

### F2 Emoção (Amígdala + Ínsula + ACC): threshold 0.79

Audita se ativa um estado emocional REAL no momento certo (medo, indignação, surpresa, alívio, admiração, curiosidade tensa). O teste: a emoção é nomeada em linguagem concreta, não em eufemismo; há uma curva dentro do trecho (uma valência que muda, tensão que sobe e resolve); a carga é palavra forte, não fala agitada.

Sinal no corte: densidade de palavras de alta valência emocional e um arco dentro do trecho (uma tensão na abertura, uma resolução no fecho). Palavra concreta e sentida pontua; abstração fria não pontua. "Achei que ia morrer ali dentro" pontua; "a situação era desafiadora" não. A curva importa mais que a intensidade: um trecho calmo com pico real vence um trecho agitado sem tensão (Hayden Hillier-Smith, editor do MrBeast: edição é design emocional, o que rankeia é a curva que sobe e resolve).

- Forte (história): "Ele assinou a rendição sabendo que ia ser fuzilado na semana seguinte. E assinou mesmo assim." Curva completa, palavra forte.
- Forte (entrevista): "Eu perdi tudo, dormi no carro três meses, e foi ali que eu entendi uma coisa." Vale baixa, virada, gancho de payoff.
- Alarme F2.2 (skip to desire): o corte só mostra o resultado bonito (o troféu, o cheque, a descoberta) sem a tensão que dá peso a ele. Sem a queda, a subida não emociona.

### F3 Memória (Hipocampo + Parahipocampal + Fusiforme): threshold 0.72

Audita se o corte será LEMBRADO (encoding episódico). O teste: uma micro-história com arco (personagem + virada + número) OU uma big idea resumível em uma frase; âncoras sensoriais concretas.

Sinal no corte: entidade + número + linha de tempo na mesma janela ("Napoleão", "600 mil homens", "voltaram 27 mil"), ou uma frase-resumo que dá pra isolar e alguém repete pro colega no dia seguinte. Razão alta de substantivo concreto sobre abstrato (evite o léxico abstrato genérico de IA).

- Forte (ciência): "Tem mais bactérias no seu intestino do que estrelas na Via Láctea." Comparação concreta, número, uma frase que gruda.
- Forte (negócios): "O Dr. Marcos saiu de 4 pra 18 avaliações por semana em 60 dias." Entidade, número, prazo.
- Regra prática, qualquer nicho: se ninguém consegue repetir o corte em uma frase, F3 falhou. O teste "saiu com frase pra repetir?" do gate é F3 em linguagem de operador.

### F4 Decisão (DLPFC + vmPFC + OFC): threshold 0.75

Audita se facilita a decisão de continuar assistindo e de agir: Sistema 1, baixa carga cognitiva. O teste: uma ideia por parágrafo; frases curtas no fecho; e o alerta central: nada de pedido antes de valor.

Sinal no corte: legibilidade alta, frase curta, uma ideia só, sem jargão empilhado. Alarme F4.1 (price before value): se o CTA duro, o preço ou o "compra meu curso" aparece antes de qualquer valor entregue, é a Fricção Cognitiva Antecipada em miniatura, penalidade forte. Num corte de topo de funil, CTA duro na abertura mata: o cérebro liga o modo crítico cedo, caça a pegadinha, rola o feed. Num corte de conteúdo puro (ciência, história, esporte) não há CTA duro: F4 aqui vira só carga cognitiva baixa. Uma ideia, uma frase, sem empilhamento.

- No curto o CTA, quando existe, é de autonomia (salvar, ver o próximo, comentar), nunca "fala com vendedor". Isso é F4 respeitando a ordem: o corte constrói o "eu quero" antes de pedir qualquer coisa.

### F5 Linguagem (Broca + Wernicke + Giro Angular): threshold 0.73

Audita a fluência neural (o cérebro do espectador "acompanha" a fala sem esforço). O teste: linguagem concreta; cada abstração com imagem; ritmo de frase varia (curtas e longas, burstiness); menos de 15% de voz passiva; lê em voz alta sem tropeço; zero jargão não explicado.

Sinal no corte: desvio-padrão do comprimento de sentença (ritmo), detector de voz passiva, presença de palavra sensorial. Corte que soa palestra (cadência uniforme, sujeito-verbo-objeto em fila, jargão técnico não traduzido) reprova F5: o espectador sente o palco/a aula chata e passa. Vale igual pro palestrante de negócios e pro professor de física: se a fala é fluida e imagética, F5 passa; se é acadêmica e monótona, F5 falha, mesmo com conteúdo genial.

- Teste rápido, qualquer nicho: leia o corte em voz alta. Soou gente falando com gente? F5 passa. Soou artigo lido em voz alta? F5 falha. Lembre: a fala é verbatim do vídeo-fonte; F5 aqui mede se o TRECHO que você escolheu é fluido, não te autoriza a reescrever a fala.

### F6 Recompensa (Estriado Ventral + Accumbens + VTA): threshold 0.75

Audita a antecipação de recompensa (dopamina é antecipação, não prazer). O teste: pelo menos um curiosity loop aberto que puxa pra frente; promessa de payoff que o trecho vai (ou já) entrega; resultado com variabilidade real (intervalo, não número mágico); no conteúdo de conhecimento, a promessa de "você vai entender algo que quase ninguém entende".

Sinal no corte: padrão de open loop ("o que ninguém te conta é...", "isso muda quando você percebe uma coisa...", "e tem um detalhe que vira o jogo"), e o payoff correspondente dentro do corte. Um corte que FECHA com um loop aberto e honesto tem F6 alto: puxa o replay e o perfil.

- Forte (ciência): "Todo mundo aprende que a língua tem zonas de sabor. Isso é errado, e o mapa que te ensinaram veio de uma tradução mal feita de 1901." Abre loop, promete uma revelação, e entrega.
- Forte (negócios): "Existe uma conta que mostra pra onde o dinheiro vaza. Vou te mostrar." Loop aberto e honesto, não escassez fabricada.
- Alarme: loop aberto que o corte NÃO paga (clickbait). Deriva pra penalidade e interage com o veto promete-e-não-entrega do `01`.

### F7 Predição (hierarquia cortical + PFC + TPJ): threshold 0.71

Audita a arquitetura de mudança de crença: violar a predição óbvia do espectador, resolver, atualizar a crença. É o filtro mais forte pra viralidade, porque compartilhamento nasce de "eu não sabia disso". O teste: o gancho quebra a expectativa mais óbvia sobre o tema; depois da violação há resolução dentro do corte; a causa é enquadrada diferente do senso comum.

Sinal no corte: estrutura de reframe ("não é X, é Y", "todo mundo faz X e é por isso que dá errado", "ao contrário do que você aprendeu"), COM resolução na mesma janela. Alarme F7.1 (predictable hook): abrir com o senso comum que já circula ("consistência é tudo", "beba água", "o esforço vence") reprova, é predição confirmada, o cérebro não atualiza nada. Alarme F7 improdutivo: violar a expectativa e NÃO resolver dentro do corte gera confusão, não curiosidade, penalidade.

- Forte (história): "Os vikings não usavam capacete com chifre. Isso foi inventado por um figurinista de ópera em 1876." Quebra a crença mais óbvia e resolve.
- Forte (ciência): "Você não vê com os olhos. Você vê com o cérebro, e os olhos só mandam dados incompletos que ele preenche chutando." Reframe verdadeiro, resolvido.
- Forte (negócios): "O problema não é falta de cliente. É o que acontece com o cliente depois que ele entra." Reenquadra a causa.
- F7 é o motor do compartilhamento em qualquer nicho: quem assiste manda pro amigo porque o corte violou uma crença que os dois tinham. Reframe com substância, nunca frase de efeito vazia.

**Total:** 47 pontos brutos. Cada erro-padrão tem código (F1.3 Completable Hook, F2.2 Skip to Desire, F3.3 Single Mention, F4.1 Price Before Value, F7.1 Predictable Hook), o que dá uma taxonomia pronta pra rotular por que um corte caiu. Fonte: `../copy-brain/filtros/`.

---

## O fluxo em fases que agrega num veredicto

Os 7 filtros não rodam em cascata "reprovou F1, parou". Rodam TODOS sobre a mesma transcrição do trecho, cada um dá sua nota, e o agregado vira classificação. Fases (adaptadas de `auditoria-completa.md` para o corte):

```
FASE 0  CONTEXTO: define o perfil de peso (corte curto espelha "Ad": F1 e F7 CRITICOS)
   |
FASE 1  LEITURA DIAGNOSTICA: marca no trecho [PARA] [CONFUSO] [FRACO] [FORTE] [FALTOU]
   |
FASE 2  OS 7 FILTROS: F1 a F7, cada um pontua 0 / 0.5 / 1 por criterio
   |
FASE 3  SCORING: nota por filtro vs threshold (PASSA/FALHA), media ponderada, top erros
   |
FASE 4  VEREDICTO: GOLD / SILVER / BRONZE / RED  ->  ranking do corte
```

Regra especial do F1: nota F1 abaixo de 0.5 descarta o trecho na hora. Um corte que não segura os 3 primeiros segundos não vira short, ponto, seja o tema qual for. Os outros filtros só importam depois que o F1 passa o portão de entrada.

### Os veredictos (como o passa/reprova vira classificação)

| Veredicto | Regra (Copy Brain OS) | Faixa % | O que fazer com o corte |
|---|---|---|---|
| **GOLD / OURO** | média >= 0.79 e todos os filtros passam | 90-100% | Corta, gera a legenda, publica com ajuste fino |
| **SILVER / PRATA** | média boa mas 1 filtro inegociável falha | 75-89% | Corrige o filtro abaixo do threshold antes de cortar |
| **BRONZE** | média >= 0.73, 1 a 2 filtros falham | 60-74% | Só vale o corte se der pra reescrever a legenda/fecho |
| **RED / REPROVADO** | média < 0.73 ou vários filtros falham | < 60% | Não corta esse trecho. Procura outro no vídeo |

**Ponderação por formato:** um corte curto espelha o perfil "Ad" do Copy Brain OS: F1 e F7 são CRÍTICOS, F2 e F6 e F5 altos, F3 e F4 médios. Isso muda o veredicto: um trecho com F3 fraco mas F1 e F7 fortes ainda pode ser GOLD pra corte, enquanto o mesmo trecho reprovaria como VSL (onde F2/F3/F6/F7 pesam). O perfil de peso é escolhido na Fase 0, e é o mesmo pra qualquer nicho, porque a física da retenção de short é a mesma: o gancho decide o swipe e a quebra de expectativa decide o compartilhamento.

> Nota de honestidade: este mapeamento pra corte é uma ADAPTAÇÃO (a versão vídeo-curto do checklist de roteiro do Copy Brain OS). Os pesos precisam de calibração contra desempenho real (retenção e replay dos shorts publicados) antes de virarem afirmação fechada. `[PRECISA VALIDAÇÃO]`.

---

## Os 4 portões e a ordem biológica dura

Os 7 filtros dão a NOTA. Os 4 portões dão a ORDEM. Um corte pode ter todos os filtros passando e ainda reprovar, se a ordem estiver trocada. Os portões são a sequência fixa em que o cérebro processa qualquer estímulo, e ela NÃO é negociável (fonte: `../neuromarketing/ia-preditiva-neuroscore.md`):

| # | Portão | Região | Pergunta do cérebro | Filtro F correspondente |
|---|---|---|---|---|
| 1 | Relevância | Amígdala | "isto é sobre MIM / vale meu tempo, agora?" (3s) | F1 + F2 |
| 2 | Pesagem de decisão | ACC | "continuo ou passo?" | F4 (parte) |
| 3 | Valorização | vmPFC | "eu QUERO isto / preciso saber isto?" | F6 |
| 4 | Resistência crítica | dlPFC | "onde está a pegadinha / o que ele quer vender?" | F4 (parte) + F7 |

**A regra de ouro:** valor antes do pedido. Portão 3 (o "eu quero saber") tem que acender ANTES do portão 4 (o "cadê a pegadinha"). Se o corte pede preço, CTA duro ou argumento técnico pesado antes de construir o desejo, o dlPFC liga fora de hora, caça a armadilha e fecha. Em corte de conteúdo sem venda (ciência, história, esporte), o mesmo vale traduzido: se o trecho abre com um bloco técnico denso antes de dar um motivo pra se importar, o portão 4 (esforço/tédio) liga antes do portão 3 (curiosidade) e a pessoa passa.

### O alerta: Fricção Cognitiva Antecipada

Quando o dlPFC ativa antes do vmPFC, dispara a Fricção Cognitiva Antecipada. No corte isso é fácil de flagrar: o trecho ABRE pedindo (CTA, preço, "agenda uma call") ou ABRE com carga técnica seca, sem ter dado nada ao espectador antes. Correção prescrita: mover a prova, o benefício emocional ou o gancho de curiosidade para o começo do corte. Se não dá pra reordenar dentro do trecho (a fala é verbatim, você só reposiciona onde o corte começa), então o trecho não é corte, é o meio de uma conversa.

- Fricção antecipada (venda): corte abre com "Fecha comigo e eu monto teu sistema. São 12 módulos." Pediu antes de o espectador sentir o valor. Portão 4 ligou primeiro.
- Fricção antecipada (conteúdo): corte de aula de física abre com "A equação de Schrödinger dependente do tempo é a seguinte." Bloco técnico sem gancho. O portão 4 (isso vai dar trabalho) liga antes do portão 3 (curiosidade). Reposiciona o corte pra começar na frase que dá o porquê de se importar.
- Ordem respeitada: corte abre com a cena ou o número que prende (amígdala, portão 1), constrói o "eu quero saber" (vmPFC, portão 3), e só no fecho puxa o pedido ou a conclusão densa. Desejo primeiro, esforço/pedido depois.

Penalidades duras no NeuroScore de Corte: F1 abaixo de 0.5 descarta; Fricção Cognitiva Antecipada tira 0.3; violação de expectativa sem resolução (F7 improdutivo) tira 0.2.

---

## Como o F1-F7 se combina com a rubrica de 8 eixos do `01`

Os dois trabalham em série, não competem. Divisão de trabalho:

- **A rubrica de 8 eixos do `01` RANKEIA.** Ela roda barato sobre todos os trechos do vídeo longo (sinais observáveis na transcrição e no áudio: gancho nos 2s, autossuficiência, lacuna de curiosidade, pico emocional, frase citável, payoff, stakes). Sai uma lista ordenada de candidatos. É o pré-filtro largo: transforma 30 minutos em, digamos, os 6 melhores trechos.
- **O NeuroScore F1-F7 é o GATE NEURAL que confirma ou reprova o topo.** Você não roda o F1-F7 nos 30 minutos inteiros: roda só nos candidatos que a rubrica já elegeu. Ele confirma quais viram GOLD/SILVER e reprova os que a rubrica pontuou alto por energia mas que quebram no cérebro (abrem pedindo, violam sem resolver, som forte mas sem tensão real, reframe que é frase de efeito e não substância).

Em uma frase: a rubrica de 8 eixos peneira e ordena; o F1-F7 é o portão que só deixa passar o corte que segura o cérebro na ordem certa. Um trecho pode ser eixo-alto e neuro-reprovado (barulho sem substância), e é aí que o gate ganha o dinheiro. O inverso também: trecho de energia média que o F7 revela ser um reframe forte (uma crença comum derrubada com prova) sobe no ranking depois do gate neural, porque F7 é o que faz a pessoa compartilhar.

Mapa de correspondência dos 8 eixos com os filtros (os dois olham o mesmo trecho, por lentes diferentes):

| Eixo do `01` | Filtro(s) F1-F7 que confirmam |
|---|---|
| 1. Gancho nos 2s | F1 (o portão de entrada) |
| 2. Momento autossuficiente | F1 (não abre pedindo contexto) |
| 3. Lacuna de curiosidade / open loop | F6 (antecipação) + F7 (violação de predição) |
| 4. Pico emocional / tensão | F2 (curva emocional real) |
| 5. Frase citável | F3 (encoding, dá pra repetir) + F5 (fluência) |
| 6. Payoff / recompensa | F6 (paga o loop) |
| 7. Stakes | F2 (peso emocional da perda) |
| 8. Fit com o público-alvo (OPCIONAL) | F1/F2 SÓ no modo marca (ver abaixo) |

Analogia útil (o "ViralAnalyser", conceitual, em `../neuromarketing/ia-preditiva-neuroscore.md`): o Modo Solo é a lógica de achar onde a atenção desaba e cortar ali; o Modo Compare é sobrepor cortes concorrentes do mesmo vídeo e rankear. A rubrica de 8 eixos é o Solo (varre o vídeo, marca a queda); o F1-F7 sobre os finalistas é o Compare (rankeia os concorrentes).

Depois disso, para cada corte que passou o gate neural, o gerador de vídeo curto monta o roteiro (6 passos) e o gate de 11 critérios aprova a peça final. O NeuroScore não substitui o gate de 11 critérios: ele decide QUAIS trechos merecem virar roteiro; o gate de 11 decide se o roteiro pronto sai.

---

## A camada OPCIONAL: modo marca

No modo GERAL (default), o eixo 8 (fit de público-alvo) sai da conta e o NeuroScore mede só sentido + viralidade. O F1 pergunta "isso prende qualquer um?", não "isso prende um público-alvo específico?".

Liga-se a camada de fit SÓ quando o vídeo-fonte é conteúdo de um criador com público-alvo definido e ele quer cortes calibrados para esse público. Aí, e só aí:

- F1 e F2 ganham um segundo passe: além de "prende qualquer um", "prende o público-alvo no feed, na dor e na língua dele?".
- Entram os anti-gatilhos do público-alvo (nome inventado de problema/método, hype de IA-milagre, tom de coach, contador regressivo, desconto no frio). Um corte que passaria no geral pode cair no modo marca por soar a marqueteiro.
- O eixo 8 volta a pontuar e o filtro de fit roda contra o perfil do público-alvo do criador.

Fora desse modo, nada disso se aplica: um corte de ciência ou de esporte não deve ser reprovado por "não falar a dor de um público específico". Isso seria confundir a camada opcional com o critério geral, e o critério geral é sentido + viralidade.

---

## Sobre o Tribe v2 (referência, nunca motor)

O modelo neural Tribe v2 da Meta (`https://github.com/facebookresearch/tribev2`, licença CC BY-NC 4.0 não-comercial, requisito GPU A100 40GB, ~28-32GB de VRAM em inferência; números de hardware de fonte única, DataCamp, 2026) fica SÓ como lastro teórico. Três razões:

1. Exige GPU A100, não roda em máquina comum. Não entra no loop de produção.
2. Licença não-comercial: usar o scorer neural dentro de um serviço pago é uso comercial e pede parecer jurídico. As heurísticas F1-F7 (texto, sobre frameworks científicos de domínio público: Kahneman, Friston, Damasio) NÃO têm essa trava.
3. Para PONTUAR CORTES não é preciso prever fMRI. Basta um proxy de atenção, emoção e quebra de expectativa, e isso o fluxo F1-F7 sobre a transcrição já faz, pra qualquer nicho.

Substitutos LOCAIS (usar estes, não o modelo neural): pipelines de highlight pra achar o candidato (AI-Youtube-Shorts-Generator, OpenShorts, ambos com Whisper local), GoEmotions multilíngue PT-BR em CPU pra dar corpo a F2/F6, e, se um dia houver GPU dedicada, LMM-EVQA (licença Apache 2.0, comercial-amigável) como segundo score de engajamento. Detalhe e links: `03-ferramentas-e-mcp.md` e os estudos-fonte. Nada disso é obrigatório pra rodar o NeuroScore a olho: o fluxo F1-F7 sobre a transcrição já é a versão manual, e é a que se usa por padrão.

---

## Checklist de bolso: pontuar um trecho em 2 minutos (modo GERAL)

Antes de decidir se um trecho vira corte, rode isto na cabeça, na ordem dos portões. Vale pra qualquer tema:

1. **Portão 1 (F1+F2):** a 1ª frase do trecho para o dedo sozinha, sem contexto de antes? Surpreende, tensiona ou promete? Se abre com "então", "porque", "aí", "voltando": descarta.
2. **Portão 3 (F6):** tem um momento de "eu preciso saber isso" (loop aberto, promessa de revelação) ANTES de qualquer pedido ou bloco técnico seco?
3. **Portão 4 (F4+F7):** o pedido (se existe) vem depois do valor? O trecho quebra a crença óbvia sobre o tema e resolve dentro do corte?
4. **F3:** dá pra resumir o corte em uma frase que alguém repete pro amigo?
5. **F5:** lendo em voz alta, o trecho flui como gente falando, ou soa artigo/aula lida?

Passou os cinco: GOLD ou SILVER, manda pro gerador. Travou no 1: nem tenta. Travou no 3 ou 4 (abriu pedindo ou abriu técnico): Fricção Cognitiva Antecipada, reposiciona o início do corte ou descarta.

(No modo marca, some um sexto passo: soa na língua do público-alvo, sem anti-gatilho de marqueteiro? Só nesse modo.)

---

## Conexão

- **Vizinho anterior (rankeia):** `01-score-preditivo.md` deste módulo (rubrica de 8 eixos que peneira e ordena os trechos do vídeo longo; o NeuroScore confirma o topo dela). O mapa do subsistema: `00-metodo-de-corte.md`.
- **Vizinhos seguintes:** `03-ferramentas-e-mcp.md` (stack local e substitutos open-source citados aqui) · `04-ciencia-da-viralidade-de-corte.md` (o porquê científico da retenção e do compartilhamento).
- **Teoria neural (4 portões + Fricção + ViralAnalyser):** `../neuromarketing/ia-preditiva-neuroscore.md`.
- **Execução com nota (F1-F7 detalhados):** `../copy-brain/` (README, auditoria-completa, filtros F1..F7). Regras de quando acionar: `../apoiador-copy-brain.md`.
- **Estudos-fonte:** `../estudos/2026-07-01-cortes-tribe-v2-fluxo-e-opensource.md`.
- **O score entra na produção assim:** só o topo do ranking vira roteiro no gerador de vídeo curto (6 passos) e cada corte passa pelo gate de qualidade (11 critérios) antes de sair. O NeuroScore escolhe QUAIS trechos entram no gerador; o gate de 11 decide se o roteiro sai.