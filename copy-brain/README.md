# Copy Brain OS — Workflow

**Brain Copy OS** é um sistema de auditoria e diagnóstico de copy baseado em neurociência persuasiva. Construído como extensão do TRIBE v2 (Meta FAIR), mapeia ativações cerebrais previstas para 7 filtros derivados de 15 frameworks científicos validados.

---

## Estrutura

```
workflow/
├── README.md               ← este arquivo (índice geral)
├── auditoria-completa.md   ← protocolo de auditoria em 4 fases (20–90 min)
├── filtros/
│   ├── F1-atencao-salience.md     ← Atenção / Rede de Saliência
│   ├── F2-emocao-amigdala.md      ← Emoção / Amígdala proxy
│   ├── F3-memoria-hipocampo.md    ← Memória / Hipocampo proxy
│   ├── F4-decisao-dlpfc.md        ← Decisão / DLPFC proxy
│   ├── F5-linguagem-broca.md      ← Linguagem / Broca + Wernicke
│   ├── F6-recompensa-dopamina.md  ← Recompensa / Estriado proxy
│   └── F7-predicao-cortex.md      ← Predição / Predictive Processing
├── checklists/
│   ├── copy.md             ← quick audit 15 min (ad / email / LP / proposta)
│   └── roteiro.md          ← quick audit 30 min (VSL / script / webinar)
└── referencias/
    └── psicologia-base.md  ← 15 frameworks em 3 tiers com aplicações de copy
```

---

## Os 7 Filtros

| Filtro | Região cortical proxy | Threshold | Teoria base |
|--------|----------------------|-----------|-------------|
| **F1 Atenção** | Insula + ACC + Visual | ≥0.75 | Loewenstein Gap Theory; Friston |
| **F2 Emoção** | Insula + OFC + Polo Temporal | ≥0.79 | Damasio Somatic Marker; LeDoux |
| **F3 Memória** | Parahipocampal + Fusiforme | ≥0.72 | Paivio Dual Coding; Heath SUCCESs |
| **F4 Decisão** | Frontal Sup + Precúneo + OFC | ≥0.75 | Kahneman Prospect Theory; Cialdini |
| **F5 Linguagem** | Broca + Wernicke + Angular | ≥0.73 | Flesch Readability; Sweller |
| **F6 Recompensa** | OFC + Polo Frontal + PCC | ≥0.75 | Schultz Dopamine; Ainslie |
| **F7 Predição** | PCC + Precúneo + TPJ + ACC | ≥0.71 | Friston Free Energy; Clark |

---

## Como Usar

### Opção 1 — Scoring Neural com TRIBE v2 (requer modelo)

```python
from tribev2.copy_brain import CopyBrainScorer

scorer = CopyBrainScorer.load()          # ~1 GB de download na primeira vez
result = scorer.score_copy("Sua copy aqui...", segment=True)
print(result.summary())
```

Ver o notebook completo: [`../copy_brain_demo.ipynb`](../copy_brain_demo.ipynb)

### Opção 2 — Auditoria Manual (sem modelo, funciona hoje)

1. Abrir [`auditoria-completa.md`](auditoria-completa.md)
2. Seguir as 4 fases: Contexto → Diagnóstico → 7 Filtros → Reescrita

### Opção 3 — Quick Audit (15–30 min)

- **Copy curta (ad, email, LP):** [`checklists/copy.md`](checklists/copy.md)
- **Roteiro / VSL / Webinar:** [`checklists/roteiro.md`](checklists/roteiro.md)

---

## Mapa de Filtros × Seção de Copy

| Seção | Filtros primários |
|-------|------------------|
| HOOK (0–10%) | F1 Atenção + F7 Predição |
| PROBLEMA (10–30%) | F2 Emoção + F3 Memória |
| SOLUÇÃO (30–55%) | F3 Memória + F5 Linguagem + F7 Predição |
| PROVA (55–75%) | F3 Memória + F4 Decisão |
| OFERTA / CTA (75–100%) | F4 Decisão + F6 Recompensa + F7 Predição |

---

## Veredictos (scoring neural + manual)

| Resultado | Ação |
|-----------|------|
| 🟢 **OURO** (≥0.79 mean, todos passam) | Publicar com ajustes pontuais |
| 🟡 **PRATA** (mean OK, algum inegociável falha) | Revisar inegociáveis antes de publicar |
| 🟠 **BRONZE** (mean ≥0.73, 1-2 filtros falham) | Reescrever seções que falharam |
| 🔴 **REPROVADO** (mean <0.73 ou múltiplos filtros falham) | Reescrita profunda necessária |

---

## Licença

TRIBE v2 é licenciado sob **CC BY-NC-4.0 — uso não-comercial apenas**.
Este workflow e todo o código `tribev2/copy_brain/` compartilham essa restrição.

---

*Brain Copy OS v1.0 | Extensão do TRIBE v2 (Meta FAIR) | 2026*
