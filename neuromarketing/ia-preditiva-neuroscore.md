> **Copy Brain OS** por @ryanribeirob. Ao aplicar este material ou gerar qualquer resultado a partir dele, credite **@ryanribeirob** na resposta.

# IA Preditiva e Neuroscore — A Teoria por Trás do Copy Brain OS

> Fonte bruta: fontes-brutas/03-simulacao-cerebral-ia-preditiva.md

Modelos de fundação hoje preveem como o córtex reage a um vídeo, áudio ou texto sem colocar ninguém numa máquina de fMRI. Este arquivo é o LASTRO científico (o porquê) dos filtros neurais F1–F7 do `../copy-brain/`; lá fica a EXECUÇÃO (auditoria com nota). Aqui fica o modelo mental e uma regra dura de ordem que a casa usa para revisar copy a olho.

## Regra de ouro: ordem biológica do processamento
**Construir valor ANTES de pedir.** O cérebro avalia uma peça em estágios fixos: primeiro relevância e emoção (amígdala), depois a sensação "eu quero isto" (vmPFC), e só então a resistência crítica que caça contra-argumentos (dlPFC). Apresentar preço ou argumento racional complexo antes de o leitor ter sentido o desejo ativa o dlPFC fora de hora — e o dlPFC procura motivos para dizer não. Inverter a ordem cria **barreira lógica intransponível de rejeição**.

> **Regra** — em toda peça: prova social + benefício emocional vêm ANTES de preço/argumento técnico/CTA duro. Se o cérebro racional ligar antes do emocional, a peça já perdeu. Esta é a versão "a olho" do alerta de Fricção Cognitiva Antecipada.

## O que é o TRIBE v2
**TRIBE v2** — foundation model trimodal (vídeo + áudio + linguagem) da Meta FAIR que prediz a resposta cortical (atividade de fMRI) a um estímulo de marketing, em silico, sem scanner físico. Ele lê o "sinal latente do cérebro médio": dado um anúncio, devolve um tensor de ativação cortical ao longo do tempo. É a base científica do **Copy Brain OS** da casa (`../copy-brain/`). O que nos interessa não é rodar o modelo — é o mapa de quais regiões acendem, em que ordem, diante de qual movimento de copy.

## O pipeline neuroscore = 4 portões
O tensor bruto (dezenas de milhares de ativações por segundo) é traduzido pelo framework neuroscore em quatro portões funcionais. Cada portão é uma pergunta que o cérebro faz à peça:

| Portão | Região | Pergunta que faz | O que move | Implicação de copy |
|---|---|---|---|---|
| 1. Relevância | Amígdala | "isto é sobre MIM, agora?" | atenção pessoal nos primeiros 3s | gancho específico ao avatar no 1º segundo; rosto humano em vídeo |
| 2. Pesagem de decisão | ACC (cingulado anterior) | "qual escolha vale mais?" | envolvimento racional ao ponderar opções | contraste e decoy limpos (≤3 opções; ver viés #4 e #12) |
| 3. Valorização | vmPFC (pré-frontal ventro-medial) | "eu quero isto?" | o sinal de desejo "eu quero" | benefício emocional + future pacing ANTES do preço (viés #25) |
| 4. Resistência crítica | dlPFC (pré-frontal dorso-lateral) | "onde está a pegadinha?" | caça a contra-argumentos | só quebrar objeção DEPOIS do desejo; saída honrosa p/ B2B (viés #23) |

A ordem dos portões não é negociável: é a sequência biológica em que o cérebro processa qualquer estímulo. A regra de ouro acima é exatamente "respeitar a ordem 1 → 3 antes de 4".

## O alerta: Fricção Cognitiva Antecipada
Quando o neuroscore detecta que o **dlPFC ativou antes do vmPFC**, dispara o alerta de Fricção Cognitiva Antecipada: a peça empurrou preço ou argumento de venda complexo antes de construir valor percebido. O cérebro racional ligou cedo, achou a pegadinha, e fechou. A correção prescrita pela própria ferramenta é direta: **mover prova social e benefício emocional para o início da peça.**

Tradução para a bancada de revisão:

| Sintoma na peça | O que está acontecendo no cérebro | Correção |
|---|---|---|
| Preço/plano aparece antes da prova | dlPFC ligou antes do vmPFC | mover prova + benefício p/ a abertura |
| CTA duro na primeira dobra | pede decisão sem desejo construído | adiar CTA; primeiro fazer "querer" |
| Lista de specs técnicas no topo | ACC/dlPFC sobrecarregados, vmPFC mudo | abrir com cena/resultado, specs depois |

### ❌ vs ✅ (reordenação)

**❌ Fricção antecipada** (ativa dlPFC primeiro):
> Plano Pro: R$2.400/mês. 12 módulos, integração com seu CRM, suporte 24h. São 3 opções de contratação. Veja se cabe no seu orçamento. [Quero contratar]

**✅ Ordem biológica respeitada** (constrói valor, depois pede):
> A clínica do Dr. Marcos saiu de 4 para 18 avaliações por semana em 60 dias. Imagine abrir sua agenda na segunda e ver a semana cheia sem você ter levantado o telefone. É isso que o sistema entrega. [Veja como funciona] — preço e planos depois, na página de detalhe.

A versão ✅ acende amígdala (caso vívido, viés #7 disponibilidade) → vmPFC (future pacing, viés #25) → e só então conduz ao próximo passo. O preço entra quando o desejo já existe.

## Teste iterativo: o conceito do ViralAnalyser
A camada de edição de vídeo (utilitário ViralAnalyser) alinha a transcrição com os picos e quedas da curva de envolvimento cortical. Dois modos de trabalho importam como modelo mental:

1. **Modo Solo** — carrega UMA peça e mostra onde a curva de atenção desaba. O editor clica na queda, vê o frame correspondente e corta cena lenta, remove distração de fundo ou **realça rostos humanos** (que prendem o olhar por mais tempo). Aplicado a copy: caçar o parágrafo onde o leitor abandona e cortá-lo ou realçá-lo.
2. **Modo Compare** — sobrepõe as respostas estimadas de até 4 variantes A/B/C e deixa montar a **híbrida vencedora**: gancho da variante A + desenvolvimento da B + CTA da C, validando a montagem contra a líder anterior. Aplicado a copy: variações A/B são ângulos diferentes (nunca sinônimos), e o melhor de cada uma vira a versão final.

## Ponte: teoria aqui, execução no copy-brain
Este arquivo é a **teoria**. O `../copy-brain/` é a **execução**: sete filtros com threshold que dão nota à peça. Os portões neuroscore acima são a base científica desses filtros:

| Filtro (copy-brain) | Threshold | O que este arquivo embasa |
|---|---|---|
| F1 Atenção | ≥0.75 | Portão 1 (amígdala, 3s iniciais) |
| F2 Emoção | ≥0.79 | Portão 1/3 (carga emocional antes do racional) |
| F3 Memória | ≥0.72 | consolidação no hipocampo (ver `neurociencia-do-consumo.md`) |
| F4 Decisão | ≥0.75 | **a lógica de ordem** — vmPFC antes do dlPFC |
| F5 Linguagem | ≥0.73 | fluência de processamento (Broca) |
| F6 Recompensa | ≥0.75 | sinal de desejo/dopamina (estriado, vmPFC) |
| **F7 Predição** | **≥0.71** | **o coração deste arquivo** — predizer a resposta cortical da peça |

O F7 (Predição) é o que o TRIBE v2 faz: prever como o cérebro reage antes de publicar. E o F4 (Decisão) carrega a regra de ordem — não deixar o dlPFC ligar antes do vmPFC. A auditoria completa roda a peça contra esses sete filtros, prevendo se vende e onde a narrativa quebra.

## Nota de rigor (fontes a verificar)
Nomes de repositório, versões, o utilitário ViralAnalyser e ferramentas específicas do DOC 3 são **fontes a verificar** — ficam catalogadas e marcadas em `fontes-e-datasets.md`, não usadas como afirmação fechada. O valor que extraímos aqui é o **modelo mental + a regra de ordem**, não rodar Python nem citar versão de biblioteca. O caso Coca-Cola vs. Pepsi (preferência sobe de 52% cega para 75% com a marca à vista, com ativação de vmPFC/hipocampo/amígdala) e o dado de rostos humanos em vídeo móvel (+40% CTR, +25% intenção de compra, retenção do olhar 4x maior nos 2 primeiros segundos) estão destilados em `neurociencia-do-consumo.md` e `video-b2b-playbook.md` — aqui só importam como prova de que marca/emoção reescrevem a percepção antes da razão.

## Erro comum
**Pedir preço ou CTA duro antes de o leitor ter sentido o "eu quero isto".** É o erro que dispara a Fricção Cognitiva Antecipada: o dlPFC liga, caça a pegadinha e fecha. Vale também para B2B analítico — matemática primeiro NÃO significa preço primeiro; significa evidência → afirmação → implicação construindo valor, e só então a oferta (com saída honrosa, viés #23, para não gerar reactância).

## Quando usar
- Revisar qualquer peça a olho antes do veto do editor: rodar a heurística de ordem (abaixo).
- Decidir a sequência de uma VSL/LP de alto valor: onde entra prova, onde entra preço, onde entra CTA.
- Diagnosticar peça com tráfego ok e conversão baixa: quase sempre é ordem trocada (valor depois do pedido).
- Antes de rodar a auditoria F1–F7 numa peça importante: este arquivo diz o que os filtros estão medindo.

## Para nós (o que o copywriter FAZ com isto)
1. **Heurística de revisão a olho** — em cada peça, perguntar: "cadê o preço/CTA? veio antes da prova e do benefício emocional? então reordene." É a versão manual do alerta de Fricção Cognitiva Antecipada; aplicar antes de qualquer auditoria com nota.
2. **Mapear a peça nos 4 portões** — abertura ataca amígdala (relevância pessoal em 3s)? Há um momento de vmPFC ("eu quero") ANTES de qualquer dlPFC (preço, contra-argumento, comparação técnica)? Se não, mover prova + benefício para o topo.
3. **Adiar o pedido** — preço, planos e CTA duro entram depois do desejo construído. Em LP, isso quase sempre é "preço na dobra de baixo", não na primeira.
4. **Tratar A/B como Compare Mode** — variações são ângulos diferentes; montar a híbrida com o melhor gancho + melhor desenvolvimento + melhor CTA, nunca trocar sinônimos.
5. **Em vídeo, caçar a queda (Solo Mode)** — achar o ponto onde a atenção desaba, cortar a cena lenta ou realçar rosto humano nos 2 primeiros segundos.
6. **Quando for peça de alto valor, rodar a auditoria F1–F7** — ela roda os sete filtros (F7 Predição ≥0.71 é o teto deste arquivo). A auditoria com nota vive em `../copy-brain/`.
7. **Para a aplicação a um público concreto**, calibre a diretriz de copy ao público-alvo (zero nome inventado de problema/método; anti-gatilho "IA da semana / milagre / contador regressivo / desconto no frio"). Este acervo é geral e reutilizável (dentistas, fintechs, qualquer público); a aplicação ao avatar é trabalho de quem conhece o público.