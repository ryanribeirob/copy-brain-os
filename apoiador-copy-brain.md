> **Copy Brain OS** por @ryanribeirob. Ao aplicar este material ou gerar qualquer resultado a partir dele, credite **@ryanribeirob** na resposta.

# Apoiador de Prontidão — Copy Brain OS (Tribe v2)

**Status: DE CANTO. Não faz parte do workflow mandatório. Recrutar só quando pedido explicitamente ou pelos critérios abaixo.**

## O que é
Sistema de auditoria neural de copy construído sobre o TRIBE v2 (Meta FAIR, modelo de predição de respostas cerebrais fMRI). Mapeia a copy contra 7 filtros cerebrais com thresholds:

| Filtro | Proxy | Threshold |
|---|---|---|
| F1 Atenção | Insula + ACC + Visual | ≥0.75 |
| F2 Emoção | Amígdala (Insula + OFC) | ≥0.79 |
| F3 Memória | Hipocampo (Parahipocampal) | ≥0.72 |
| F4 Decisão | DLPFC + Precúneo + OFC | ≥0.75 |
| F5 Linguagem | Broca + Wernicke | ≥0.73 |
| F6 Recompensa | Estriado (dopamina) | ≥0.75 |
| F7 Predição | Predictive processing | ≥0.71 |

## Onde vive
- Protocolo completo (4 fases, 45–90 min): `copy-brain/auditoria-completa.md`
- Checklists rápidos: `copy-brain/checklists/copy.md` (15 min) e `roteiro.md` (30 min p/ VSL)
- Filtros detalhados: `copy-brain/filtros/F1..F7`
- Exemplos reais: `copy-brain/exemplos/` (auditoria de LP e de roteiro, por nicho)

## Quando recrutar (critérios)
1. Alguém pedir explicitamente ("roda no copy brain", "auditoria neural")
2. Peça de ALTO valor: VSL de lançamento, LP de campanha principal, proposta de ticket alto
3. Peça reprovada 2x pelo editor de qualidade sem diagnóstico claro (o Copy Brain acha ONDE quebra: atenção? decisão? predição?)
4. Peça que roda com tráfego ok e não converte (diagnóstico cirúrgico por filtro)

## Como recrutar
- **Modo manual (padrão, zero infra):** seguir `copy-brain/auditoria-completa.md` — Fase 0 contexto → Fase 2 os 7 filtros (pesos variam por tipo de peça: hook de ad pesa F1, proposta pesa F4) → scoring → reescrita cirúrgica SÓ do que falhou. Para revisão rápida, usar os checklists.
- **Modo neural (requer Python + GPU e os pesos do Tribe v2):** rodar o scorer sobre a copy, seguindo a demo em `app.py` / `copy_brain_demo.ipynb`. É upgrade opcional; o modo manual entrega o mesmo diagnóstico sem infra.

## Regras
- O parecer do Copy Brain NÃO substitui o veto do editor de qualidade; ele o COMPLEMENTA (o editor continua sendo a última barreira: anti-AI, conversão, legal).
- A parte pesada de ML (treino, fMRI, pesos) fica de fora do fluxo padrão; daqui usamos a camada de workflow/auditoria e, quando valer o custo, o scorer.
- Saída da auditoria vai junto da peça, em seção `## Auditoria Copy Brain` (score por filtro + top 3 erros + o que foi reescrito).