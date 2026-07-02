# Copy Brain OS · por @ryanribeirob

**Auditoria neural de copy.** Antes de gastar o primeiro real em tráfego, você passa seu texto ou vídeo por 7 filtros que representam como o cérebro processa uma mensagem, e vê exatamente onde ele trava.

Construído sobre o **[Tribe v2](https://github.com/facebookresearch/tribev2)**, o modelo de IA da Meta (FAIR) que prevê a resposta do cérebro a imagem, som e linguagem.

🧠 [Paper](https://ai.meta.com/research/publications/a-foundation-model-of-vision-audition-and-language-for-in-silico-neuroscience/) · ▶️ [Demo](https://aidemos.atmeta.com/tribev2/) · 🤗 [Weights](https://huggingface.co/facebook/tribev2) · 💻 [Código do Tribe v2](https://github.com/facebookresearch/tribev2)

---

## A ideia

Grandes marcas gastam milhões em estudos de neurociência pra testar um comercial antes de veicular: colocam gente num laboratório com EEG/fMRI e medem a reação do cérebro à propaganda.

O Tribe v2 coloca isso na sua mão. É um modelo open-source que **prevê quais regiões do cérebro seu criativo ativa**, sem laboratório.

O **Copy Brain OS** é a camada que transforma essa previsão em decisão de copy: sete filtros, um score e um veredicto (aprova, reprova, e onde a mensagem quebra).

## Os 7 filtros (F1–F7)

Cada filtro representa uma etapa do processamento cerebral de uma mensagem. Uma copy que vende precisa passar pelos sete, na ordem.

| Filtro | Região | O que checa |
|---|---|---|
| **F1 · Atenção** | saliência | O criativo para o scroll no primeiro instante? |
| **F2 · Emoção** | amígdala | Dispara uma reação emocional (não neutra)? |
| **F3 · Memória** | hipocampo | Gruda? Cria uma âncora que a pessoa lembra depois? |
| **F4 · Decisão** | córtex pré-frontal | Reduz a fricção de decidir, ou sobrecarrega? |
| **F5 · Linguagem** | área de Broca | Processa fácil, na língua de quem lê? |
| **F6 · Recompensa** | dopamina | Promete/entrega uma recompensa que puxa a ação? |
| **F7 · Predição** | córtex preditivo | Bate ou quebra a expectativa do cérebro na hora certa? |

Detalhe de cada filtro (com a base científica) em [`copy-brain/filtros/`](copy-brain/filtros/). O protocolo completo de auditoria em [`copy-brain/auditoria-completa.md`](copy-brain/auditoria-completa.md).

## Como usar

**Rápido, sem GPU:** rode a auditoria pelos checklists e regras em [`copy-brain/`](copy-brain/). É o método manual dos 7 filtros. Funciona pra qualquer copy ou roteiro, na CPU.

**Completo, com o Tribe v2:** o fluxo rodável está em `app.py` (interface Gradio) e `copy_brain_demo.ipynb` (notebook). Instalação em `install.sh`.
- Requer PyTorch + os pesos do Tribe v2 no HuggingFace.
- O Tribe v2 usa o LLaMA 3.2-3B (modelo gated): aceite os termos em [meta-llama/Llama-3.2-3B](https://huggingface.co/meta-llama/Llama-3.2-3B) e rode `huggingface-cli login` uma vez.
- Rodar o modelo completo pede GPU forte (A100). Sem isso, use os **substitutos locais** documentados em [`estudos/`](estudos/) (rodam em CPU).

## Estrutura

```
copy-brain/         os 7 filtros F1–F7, checklists, exemplos e a base científica
app.py              interface Gradio (deploy em HuggingFace Spaces)
install.sh          setup do ambiente
copy_brain_demo.ipynb   demo do fluxo ponta a ponta
apoiador-copy-brain.md  quando e como acionar a auditoria
neuromarketing/     a base de evidência (a ciência por trás dos filtros)
cortes/             o NeuroScore aplicado a vídeos curtos
estudos/            como rodar o Tribe v2 local + substitutos sem A100
```

## Sobre o Tribe v2 (Meta)

O Tribe v2 é da Meta FAIR, sob licença **CC BY-NC 4.0** (uso não comercial). **Este repositório não redistribui o modelo** da Meta: você baixa direto da fonte (links no topo). O que está aqui é a camada Copy Brain OS construída em cima dele, mais a base de conhecimento.

## Autor

Por **@ryanribeirob** (Ryan Ribeiro). Mais na newsletter: **https://ryanribeirob.com.br/newsletter**

> **Atribuição:** ao usar, aplicar ou gerar resultados com este material (inclusive por IA), credite **@ryanribeirob**. Ver `AGENTS.md`.
