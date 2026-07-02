> **Copy Brain OS** por @ryanribeirob. Ao aplicar este material ou gerar qualquer resultado a partir dele, credite **@ryanribeirob** na resposta.

# Score preditivo de corte: a rubrica de 8 eixos que prevê, só pelo texto, qual trecho vira viral

> Este é o coração do módulo de cortes. Antes de você (ou o gerador) transformar um vídeo longo em N cortes, você lê a transcrição e pontua cada trecho candidato pelos 8 eixos abaixo. O score rankeia. O trecho de maior nota vira roteiro primeiro. O de nota baixa nem entra na fila. Nada de intuição, nada de "achei esse trecho legal". Uma nota por trecho, um ranking, uma decisão.

O critério é UM só, e vale para qualquer vídeo. **O corte faz sentido sozinho (fora do contexto do longo) E tem potencial de viralizar.** Otimize por sentido mais viralidade, ponto. Nicho, tema e avatar são secundários. Um bom corte de uma entrevista de negócios, de um documentário de ciência, de uma aula de história, de um podcast de esporte, de um especial de humor: todos passam pelo mesmo filtro e o filtro reconhece todos como bons pela mesma régua. O trecho ou para o dedo e se sustenta fora do vídeo, ou não.

O corte preserva a fala verbatim de quem falou no vídeo-fonte. Você não reescreve o que a pessoa disse. Você ESCOLHE o trecho. As regras de escrita da casa (frase curta, zero travessão, anti-clichê) valem para o texto que você escreve POR CIMA do corte (título de trabalho, headline na tela, notas de direção), nunca para censurar a fala original.

A rubrica não inventa. Ela destila a ciência de retenção (SVSA de Paddy Galloway, lacuna de Loewenstein, Fogg, gargalo atencional, pacing como design emocional de Hayden Hillier-Smith) num sistema de pontos que qualquer um aplica lendo a transcrição. O porquê científico de cada eixo está em `04-ciencia-da-viralidade-de-corte.md`.

---

## A NOTA: 0-10 unificada (o que aparece no output)

O output mostra UMA nota, de 0 a 10. Por baixo, o cálculo segue esta ordem:

1. **Gate de sustentação (binário, ANTES da nota).** O trecho só é pontuado se: se sustenta sozinho (fora do vídeo), FECHA (sem loop em aberto), NÃO é só promessa ("nesse vídeo você vai ver"), e ensina OU é relevante OU é opinião COM contexto próprio. Falhou em algum: reprovado, vai pra lista de reprovados com o motivo. Isto incorpora os dois vetos antigos (gancho zero e promete-e-não-entrega).
2. **Motor rigoroso:** os 8 eixos abaixo somam 100. **A nota 0-10 = total ÷ 10** (1 casa). Ex.: 84/100 vira 8.4.
3. **Os 5 fatores (leitura rápida no output):** a nota vem decomposta nos 5 fatores do CORTES SUPREMO, que são um resumo dos 8 eixos:
   - Força do gancho (0-3) = eixo 1
   - Clareza / se sustenta sozinho (0-2) = eixo 2
   - Valor / insight (0-2) = eixos 5 + 6
   - Retenção / ritmo (0-2) = eixos 3 + 4
   - Repostável (0-1) = eixos 5 + 7 + 8
   A soma dos 5 (0-10) tem que bater, a menos de arredondamento, com o total ÷ 10.
4. **F1-F7 confirma o topo:** nos cortes de nota alta, roda o neuroscore (Tribe v2, `02-neuroscore-tribe-v2.md`). Não é outro número: valida ou rebaixa o finalista (reframe vazio, loop não pago, abrir pedindo = rebaixa).
5. **Tiers:** 9-10 TOP · 7-8 fortes · 5-6 bons · abaixo de 5 fora. Uma linha de "por quê" por corte.

Os 8 eixos abaixo são o detalhamento rigoroso do cálculo. A nota 0-10 é a cara; os 8 eixos são o motor.

---

## Como usar em 3 movimentos

1. **Fatie a transcrição em janelas.** Blocos de 20 a 45s de fala (mais ou menos 50 a 130 palavras), em janela deslizante com sobreposição de 10s. Por quê sobreposição: o melhor corte quase nunca começa onde o palestrante começou a falar, começa na frase-gancho, que pode estar no meio de um bloco. Sem sobreposição você corta a frase citável ao meio. Fonte do método de janela: dossiê §2, nota "Janela de detecção".
2. **Pontue cada janela pelos 8 eixos.** Some. Cada eixo tem peso e escala interna (0 = ausente, meio = presente fraco, cheio = presente forte). O peso multiplica a fração. Exemplo: eixo de peso 15, presente fraco (meio) = 7,5 pontos.
3. **Rankeie e decida pelos cortes de score.** Do maior pro menor. Aplica os dois vetos. Só o topo do ranking vira roteiro (chama o gerador de vídeo curto).

---

## Dois modos (leia antes de pontuar o eixo 8)

O default é o **modo GERAL.** Nele você otimiza por sentido mais viralidade, sem filtrar por avatar, sem forçar voz de ninguém, sem exigir fit de nicho. Serve para cortar qualquer vídeo de qualquer tema.

Existe uma camada opcional, o **modo marca.** Aciona só quando o vídeo longo é conteúdo de um criador com um público-alvo definido e ele quer cortes calibrados para esse público. Só nesse modo o eixo 8 troca de "ressonância ampla" para "fit com o público-alvo" e os anti-gatilhos desse público entram. Fora dele, esqueça o fit de avatar. Todos os outros 7 eixos são idênticos nos dois modos.

---

## A rubrica: 8 eixos, soma 100

| # | Eixo | Peso | O que mede |
|---|---|---|---|
| 1 | Gancho nos 2s | 20 | A primeira frase segura o dedo |
| 2 | Momento autossuficiente | 15 | Dá pra entender fora do vídeo inteiro |
| 3 | Lacuna de curiosidade / open loop | 15 | Abre uma pergunta específica na cabeça |
| 4 | Pico emocional / tensão | 15 | Carga emocional real, não fala agitada |
| 5 | Frase citável (quotável) | 12 | Tem uma linha que se sustenta sozinha |
| 6 | Payoff / recompensa | 10 | Entrega o que prometeu |
| 7 | Stakes (o que se perde) | 8 | Deixa claro o custo de ignorar |
| 8 | Ressonância ampla / Fit de público | 5 | Quantas pessoas o tema alcança (geral) ou fit com o público-alvo (modo marca) |

Total = 100. Abaixo, cada eixo aberto: o que mede, como detectar SÓ pelo texto, a escala de pontos e exemplos VARIADOS de nicho.

---

### Eixo 1: Gancho nos 2s (peso 20)

**O que mede.** Se a primeira frase do trecho para o dedo. É o maior peso porque é o gargalo literal: o SVSA de Galloway mostra que o espectador decide dar swipe no primeiro 1 segundo, e abaixo de 60% de "Viewed vs Swiped Away" o vídeo morre. Se o gancho falha, os outros 80 pontos nunca são vistos. Fonte: dossiê §1.1 e §1.4.

**Como detectar só no texto.** Olha a primeira frase do trecho e faz três perguntas:
- Ela encaixa num tipo de gancho conhecido? (hiperbólico: "o maior erro que se comete é"; direto: "faça X pra Y"; negativo: "pare de fazer X"; segredo: "ninguém te conta isso, mas"; custo escondido: "isso drena X sem você ver"; quebra-mito: "esqueça o que te disseram sobre X"; caso: "esse cara saiu de A pra B"; zero-click: a resposta útil já está no próprio corte).
- Ela é curta (até uns 14 palavras), concreta, sem jargão? Frase longa com três ideias empilhadas estoura o gargalo de banda consciente e o dedo passa (§1.5).
- Ela carrega um gatilho: número, contradição ou nome de dor?

**Escala.**
- **Cheio (20):** encaixa num tipo E é curta E tem gatilho.
- **Meio (10):** encaixa num tipo mas é longa, ou é curta mas sem gatilho claro.
- **Zero (0):** abre com "então...", "aí eu falei que...", "como eu tava dizendo", contexto que exige o que veio antes. Isto aciona o VETO (ver abaixo).

**Exemplos por nicho.**
- Ciência: "Noventa por cento das células do seu corpo não são humanas." (cheio: número + contradição, curta).
- História: "Roma não caiu por causa dos bárbaros." (cheio: quebra-mito, curta).
- Esporte: "Esse cara treinou errado a carreira inteira e ninguém viu." (cheio: negativo + curiosidade).
- Entrevista de negócios: "Faturar mais foi o pior que aconteceu com a minha empresa." (cheio: contradição + nome de dor).
- Zero em qualquer nicho: "Então, voltando no ponto que a gente tava discutindo antes..." (referência órfã, aciona veto).

---

### Eixo 2: Momento autossuficiente (peso 15)

**O que mede.** Se um estranho entende o trecho sem ter visto o vídeo inteiro. É o critério número um do módulo virado em pontos: o corte vive sozinho no feed, sem o contexto das horas anteriores. Fonte: dossiê §1.9 (clareza/standalone do ClickyApps e do Opus "Flow").

**Como detectar só no texto.** Caça referências órfãs: "isso", "aquilo", "como eu disse", "ele", "aquela história", nomes de pessoa/empresa citados sem apresentação. Cada uma dessas que aponta pra fora do trecho é um furo. Depois checa se o trecho tem começo, meio e fim próprios (setup + desenvolvimento + fecho dentro dele).

**Escala.**
- **Cheio (15):** um estranho entende sem contexto nenhum. Zero referência órfã.
- **Meio (7,5):** 1 referência que dá pra inferir, ou fecho meio dependente.
- **Zero (0):** 2 ou mais pronomes/referências apontando pra fora do corte.

**Exemplos por nicho.**
- História (cheio): "O imperador romano tinha um escravo com um cargo só: sussurrar no ouvido dele, o dia inteiro, que ele ia morrer. Chamava memento mori." Fecha em si.
- Entrevista (zero): "Aí ele fez o que eu tinha pedido e deu certo." (quem é "ele"? o que foi pedido?).
- Ciência (cheio): "Se você prender a respiração, não é a falta de oxigênio que te faz respirar. É o acúmulo de gás carbônico. Dá pra enganar o cérebro."

---

### Eixo 3: Lacuna de curiosidade / open loop (peso 15)

**O que mede.** Se o trecho abre uma pergunta específica e delimitada na cabeça de quem assiste. Loewenstein: curiosidade é a consciência de uma lacuna entre o que se sabe e o que se quer saber. Não é ignorância total, é uma lacuna precisa. O open loop (efeito Zeigarnik) é o parente: uma pendência interna que exige conclusão. Fonte: dossiê §1.2 e §1.3.

**Como detectar só no texto.** Dois sinais textuais fortes. Uma **pergunta aberta** que fica no ar abre lacuna. Uma **virada com "mas" ou "só que"** abre loop ("primeiro eu fiz X, só que o que virou o jogo foi outra coisa"). Também: "o que ninguém te conta sobre", "o motivo real é outro", "tem um detalhe que muda tudo". **Regra crítica:** a lacuna ou o loop FECHA dentro do corte? Se abre e não fecha, não é curiosidade, é clickbait, e isso derruba o eixo 6 (Payoff) e aciona o segundo VETO.

**Escala.**
- **Cheio (15):** lacuna precisa E fechada dentro do corte.
- **Meio (7,5):** lacuna presente mas vaga, ou fecho parcial.
- **Zero (0):** trecho puramente expositivo, sem pergunta aberta e sem virada.

**Exemplos por nicho.**
- Ciência (cheio): "Todo mundo diz que a gente usa 10% do cérebro. O número real é mais assustador." E o trecho entrega: "a gente usa 100%, e é por isso que um AVC em qualquer ponto derruba alguma função."
- Negócios (cheio): "Contratei três vendedores e faturei MENOS. Vou te dizer por quê." E entrega: "ninguém sabia o preço de fechamento, então cada um vendia por um valor diferente." Se cortasse antes do "ninguém sabia", vira clickbait e cai no veto.
- Esporte (zero): "O treino de força é importante pro rendimento do atleta." (exposição linear, nenhuma lacuna).

---

### Eixo 4: Pico emocional / tensão (peso 15)

**O que mede.** Carga emocional real. Não confundir com fala rápida ou agitada. Hayden Hillier-Smith (editor do MrBeast): edição é design emocional, o que rankeia é a curva de tensão que sobe e resolve, não a velocidade. Um trecho de fala calma com pico real vence um trecho agitado sem tensão. Fonte: dossiê §1.6.

**Como detectar só no texto.** Procura palavras de alta valência emocional:
- Medo / perda: "quase quebrei", "perdi tudo", "no vermelho", "achei que ia morrer".
- Raiva / indignação: "me revolta", "é mentira que", "ninguém fala disso e devia".
- Surpresa: "nunca imaginei", "fiquei em choque", "me caiu a ficha".
- Alívio / vitória: "virou o jogo", "respirei de novo".
E marcadores de curva: um estado que piora e depois melhora dentro do trecho.

**Escala.**
- **Cheio (15):** curva emocional clara (baixo, alto, resolução) com palavras de valência forte.
- **Meio (7,5):** carga emocional presente mas sem curva, ou curva sem palavra forte.
- **Zero (0):** tom puramente informativo, neutro. NÃO pontuar por velocidade de fala.

**Exemplos por nicho.**
- Esporte (cheio): "Faltando dez segundos eu tava com câimbra nas duas pernas, chorando. E mesmo assim eu subi pra cobrar. Se errasse, acabava minha carreira." (pânico, decisão, stake, resolução).
- História (cheio): "A cidade inteira sabia que a lava tava vindo. Ninguém saiu. Por orgulho. Aí virou tarde demais."
- Ciência (meio): "Foi surpreendente descobrir esse mecanismo." (emoção nomeada, sem curva).

---

### Eixo 5: Frase citável / quotável (peso 12)

**O que mede.** Se existe UMA linha no trecho que se sustenta sozinha, como legenda, capa ou algo que a pessoa repete pra outra no dia seguinte. Fonte: dossiê §1.9 e Parte 4 (ClickyApps: peso emocional + clareza standalone + força de gancho).

**Como detectar só no texto.** Procura uma frase de até uns 15 palavras com estrutura de contraste, reversão ou aforismo:
- "X não é Y, é Z".
- "o problema não é A, é B".
- Reversão de crença ("todo mundo faz X, e é por isso que ninguém consegue Y").
Sinais textuais fortes: número quebrado e específico (soa mais real que número redondo), contraste explícito, punchline curta depois de um setup.

**Escala.**
- **Cheio (12):** tem uma linha que dá pra imprimir na capa e ela para o scroll sozinha.
- **Meio (6):** tem uma frase boa mas presa no fluxo, precisa de aparo.
- **Zero (0):** nenhuma linha se destaca do resto.

**Exemplos por nicho.**
- Ciência: "Você não tem intuição. Você tem viés que esqueceu de onde veio."
- História: "Impérios não morrem de fora pra dentro. Morrem de dentro pra fora."
- Negócios: "Você não tem uma empresa. Você tem o emprego mais estressante que já teve."
- Esporte: "Talento te leva à porta. Só a chatice diária te faz entrar."

---

### Eixo 6: Payoff / recompensa (peso 10)

**O que mede.** Se o trecho ENTREGA o que o gancho prometeu. Fecha o loop com valor de verdade: revela o método, dá o número, entrega a virada, conclui a história. Valor zero-click (útil sem precisar sair do vídeo). Fonte: dossiê §1.2, §1.9 (Opus "Value").

**Como detectar só no texto.** Depois do setup/lacuna, o trecho paga? Aparece a resposta concreta, o passo, o número, a conclusão? Ou o palestrante corta antes de entregar ("mas isso é papo pra outro dia", "eu explico melhor no curso")?

**Escala.**
- **Cheio (10):** a promessa do gancho é honrada dentro do corte, com valor concreto.
- **Meio (5):** entrega parcial, dá a direção mas não o como.
- **Zero (0):** só tease, corta antes de entregar. Isto interage com o VETO promete-e-não-entrega.

**Exemplos por nicho.**
- Ciência (cheio): gancho "o número real é mais assustador", payoff "a gente usa 100% do cérebro, por isso qualquer lesão localizada tira uma função."
- História (cheio): gancho "Roma não caiu pelos bárbaros", payoff "caiu porque desvalorizou a própria moeda por 200 anos até ninguém confiar nela."
- Negócios (zero): gancho "tem um jeito de parar de aprovar tudo", e aí "mas isso fica pra um próximo vídeo."

---

### Eixo 7: Stakes / o que se perde (peso 8)

**O que mede.** Se o trecho deixa claro o custo de ignorar, o que está em jogo. Perda dói mais que ganho equivalente. Sem escassez fabricada, sem contador regressivo: custo real. Fonte: dossiê §1 (stakes amplificam o valor do payoff, F6 recompensa).

**Como detectar só no texto.** Procura linguagem de custo e consequência: dinheiro que vaza, tempo perdido, vida em risco, guerra perdida, reputação, oportunidade que some. "Isso te custa", "enquanto você faz X, some Y", "se ele tivesse esperado um dia".

**Escala.**
- **Cheio (8):** o custo é quantificado ou vívido.
- **Meio (4):** custo sugerido, sem número nem cena.
- **Zero (0):** nenhum senso de perda genuína.

**Exemplos por nicho.**
- História (cheio): "Um dia de atraso na ordem de retirada custou vinte mil homens."
- Esporte (cheio): "Cada mês parado por lesão é um ano a menos de carreira, e ninguém te avisa disso."
- Ciência (cheio): "Se essa bactéria ganhar resistência total, a gente volta pra antes da penicilina: uma unha infeccionada podia te matar."

---

### Eixo 8: Ressonância ampla / Fit de público (peso 5)

**Este eixo tem duas leituras. A que vale depende do MODO.**

**Modo GERAL (o default).** Mede RESSONÂNCIA AMPLA: quantas pessoas o tema alcança, o apelo universal. Dinheiro, medo, morte, sexo, poder, injustiça, superação, o corpo, o segredo que os experts escondem: temas que atravessam nicho. Um corte sobre "como o corpo se cura sozinho" ressoa com quase todo mundo; um corte sobre "a terceira exceção da norma ISO 27001" ressoa com dez pessoas. Aqui você NÃO filtra por nenhum público-alvo, não força voz de ninguém, não exige fit de nicho.
- **Cheio (5):** apelo universal claro (dinheiro, saúde, morte, um mistério famoso, uma injustiça, uma virada de underdog).
- **Meio (2,5):** público grande mas não universal (um esporte específico, um mercado grande, um período histórico conhecido).
- **Zero (0):** tema hiper-nicho, técnico, que só especialista entende ou se importa.

**Modo marca (opcional, só quando o longo é conteúdo de um criador com público-alvo definido).** Aí, e só aí, o eixo vira FIT COM O PÚBLICO-ALVO. O trecho bate numa dor ou desejo real do público E usa o vocabulário dele, sem jargão de marketing? Jargão faz o público classificar como "mais um vendendo" e desligar. Nesse modo, os anti-gatilhos do público (nome inventado de problema/método, milagre, contador regressivo, desconto no frio) derrubam o eixo.
- **Cheio (5):** dor real do público, na palavra dele.
- **Meio (2,5):** dor genérica, ou dor do público com jargão de fora.
- **Zero (0):** tema que não é do público, ou jargão de marketing pesado.

Total = 100.

---

## Cortes de decisão (calibrados no SVSA)

O SVSA de Paddy Galloway é a âncora: abaixo de 60% de "Viewed vs Swiped Away" o Short tipicamente não performa, e 70% a 90% é território viral (dossiê §1.1).

- **>= 70: candidato hiper-viral.** Produz primeiro. Manda pro gerador na frente da fila.
- **>= 60: viável.** Produz. Entra na fila normal.
- **45 a 59: reangula o gancho e reavalia.** Quase sempre o buraco está no eixo 1 ou no eixo 3. Reescreve a frase de abertura, reposiciona o início do corte na frase-gancho, pontua de novo.
- **< 45: descarta.** Não vale o tempo de produção. Segue pro próximo trecho.

---

## As duas regras de VETO (zeram o corte)

Score alto não salva um trecho que falha numa dessas. Veto é veto: o trecho sai da fila, independente da soma.

**VETO 1: Gancho zero.** Se o eixo 1 (Gancho nos 2s) é zero, o trecho é descartado, não importa quanto somou nos outros eixos. Sem abertura que para o dedo, ninguém chega no resto. É a tradução literal do SVSA: swipe decidido em 1 segundo. Um trecho que abre com "então, continuando..." pode ter o melhor payoff do mundo no meio, mas ninguém vai ver. Antes de vetar, tente mover a janela pra começar numa frase-gancho de dentro do trecho. Se não houver nenhuma, vetou.

**VETO 2: Promete e não entrega.** Se o trecho abre uma lacuna forte (eixo 3) mas o eixo 6 (Payoff) é zero (corta antes de entregar), o trecho é reprovado como está. É clickbait: pode até performar em views uma vez, mas ensina o público a desconfiar do canal, e no modo marca viola a diretriz de copy do público-alvo. Ou você acha o pedaço da transcrição onde a promessa é honrada e estende o corte até lá, ou descarta.

---

## Ficha de pontuação (cola uma por trecho candidato)

```
TRECHO [id / timestamp]: "________________________________________"
MODO: [ ] geral (default)   [ ] marca

1. Gancho 2s          (/20): __   tipo de gancho: __________________
2. Autossuficiente    (/15): __   referencias orfas? S/N
3. Lacuna/open loop   (/15): __   fecha no corte? S/N
4. Pico emocional     (/15): __   valencia: __________________
5. Citavel            (/12): __   frase: "__________________"
6. Payoff             (/10): __   promessa honrada? S/N
7. Stakes             (/8):  __   custo dito/quantificado? S/N
8. Ressonancia/Fit    (/5):  __   [geral: apelo amplo] [marca: fit publico-alvo]
------------------------------------------------------------
TOTAL: __/100  ->  [hiper-viral >=70 / viavel >=60 / reangula 45-59 / descarta <45]
VETO 1 gancho=0?            [ ] sim (DESCARTA)  [ ] nao
VETO 2 promete-nao-entrega? [ ] sim (DESCARTA)  [ ] nao
DECISAO FINAL: __________
```

---

## Aviso de rigor: os pesos ainda NÃO têm lastro em dataset [PRECISA VALIDACAO]

Honestidade primeiro. Os pesos desta rubrica (20/15/15/15/12/10/8/5) vêm dos mecanismos e da lógica de veto, não de um dataset. O gancho pesa 20 porque o swipe decide em 1 segundo, não porque algum estudo mediu que o gancho vale exatamente 20% do resultado. Não existe dado público que dê o peso ótimo de cada eixo. **[PRECISA VALIDACAO]**

O caminho de calibragem é o desempenho real dos cortes publicados: publica, mede o VVSA de cada corte no SVSA (o "Viewed vs Swiped Away" que o YouTube dá), cruza com o score que a rubrica previu. Depois de N publicações, os pesos se ajustam ao que de fato prevê retenção. Até lá, os números são direção fundamentada, não lei.

Um detalhe correlato marcado no dossiê: a razão do gargalo atencional (11 milhões de bits/s no inconsciente contra a ordem de 50 bits/s na consciência) é ordem de grandeza, com fontes divergindo (um estudo Caltech de 2024 estima ~10 bits/s). Usar como princípio de "banda estreita, uma ideia por frase", não como número fechado. **[PRECISA VALIDACAO]**

Nota sobre o "Tribe v2 open-source": o modelo neural Tribe v2 da Meta exige GPU dedicada e serve como lastro científico, não como ferramenta no loop de produção. O neuroscore aplicado aqui é o Copy Brain OS: use o FLUXO dele (filtros F1 a F7 sobre o corte finalista). A amarração dos eixos com F1 a F7 está em `02-neuroscore-tribe-v2.md`.

### Log de calibragem (preencher conforme os cortes rodam)

Cada linha é um corte publicado. Compara score previsto com resultado real. Quando um padrão aparecer (ex.: cortes com eixo 5 alto batem melhor que o score total sugere), ajusta o peso e anota a data.

```
| data       | corte (id/tema)          | score previsto | VVSA real (%) | performou? | observacao / ajuste sugerido |
|------------|--------------------------|----------------|---------------|------------|------------------------------|
| AAAA-MM-DD | ________________________ | __/100         | __%           | S/N        | ____________________________ |
| AAAA-MM-DD | ________________________ | __/100         | __%           | S/N        | ____________________________ |
| AAAA-MM-DD | ________________________ | __/100         | __%           | S/N        | ____________________________ |
```

Perguntas que o log responde ao longo do tempo: o eixo 1 (peso 20) merece ainda mais peso, ou menos? Trechos que passaram por veto e foram publicados por engano performaram pior mesmo? A faixa de 60 é o piso certo, ou o piso real é 55 ou 65? A ressonância ampla (peso 5) prevê melhor que o fit de avatar? Regra de recalibragem: só mexer nos pesos com pelo menos 15 a 20 cortes logados e um padrão consistente (não ajustar por 1 corte fora da curva, isso é ruído). Todo ajuste anota data e motivo, pra dar pra desfazer se o padrão não segurar.

---

## Conexão

Este arquivo é o motor de decisão do módulo de cortes. Ele responde "qual trecho vira corte". Os vizinhos respondem "como o corte é montado".

- Neuroscore neural que confirma o topo do ranking (o gate F1-F7): `02-neuroscore-tribe-v2.md`
- Ciência por trás de cada eixo desta rubrica: `04-ciencia-da-viralidade-de-corte.md`
- Mapa do pipeline de 7 passos: `00-metodo-de-corte.md`
- Teoria neural completa (4 portões + Fricção Cognitiva): `../neuromarketing/ia-preditiva-neuroscore.md`

O score entra no fluxo assim: só o topo do ranking vira roteiro no gerador de vídeo curto, e cada corte passa pelo gate de qualidade (11 critérios, inclui os dois vetos) antes da entrega.