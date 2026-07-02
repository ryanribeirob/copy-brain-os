"""Copy Brain OS — Gradio App for HuggingFace Spaces deployment.

Replicates and extends the vishnuverse-in/ad-brain-scorer Space with:
  - 7 neuro-persuasion filters (F1–F7) instead of generic ad categories
  - Per-section scoring (HOOK / PROBLEMA / SOLUÇÃO / PROVA / OFERTA_CTA)
  - F7 Predictive Processing (unique differentiator — not in any other Space)
  - A/B neural comparison mode
  - Interactive radar chart + time series

DEPLOYMENT:
    1. Push this repo to HuggingFace (with TRIBE v2 as dependency)
    2. Set HF_TOKEN secret with access to meta-llama/Llama-3.2-3B
    3. Space runs on GPU (recommended: A10G)

LOCAL:
    gradio app.py
    # or:
    python app.py

License: CC BY-NC-4.0 — non-commercial use only.
"""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

import gradio as gr
import numpy as np

SAMPLE_COPY = """Se você está lendo isso, sua agenda já deveria estar cheia de pacientes de implante.
Mas ela não está. E você sabe o porquê.

Não é falta de competência. Não é falta de equipamento.
É que os pacientes que chegam até você não têm como pagar.
Você fecha consultas de R$200 enquanto concorrentes cobram R$8.000 pelo mesmo procedimento.

A diferença não está na técnica. Está em quem você está atraindo.

O Implant Patient Acquisition System™ mudou isso para 47 clínicas em 2024.
Em média, 12 pacientes qualificados financeiramente por mês, nos primeiros 30 dias.
Sem leads genéricos. Sem pacientes que somem no orçamento.
Só consultas com quem já decidiu investir no próprio sorriso.

Dr. Carlos, São Paulo: saiu de 2 para 11 implantes por mês em 6 semanas.
Dra. Ana, Belo Horizonte: faturou R$47.000 no primeiro mês do sistema.

Garantia: 8 pacientes qualificados em 30 dias ou devolvemos 100% do investimento.

Agenda com 3 vagas esta semana. Reserve a sua antes que feche.
Clique abaixo e veja como funciona na sua cidade."""

SAMPLE_COPY_B = """Descubra como clínicas odontológicas estão aumentando seus faturamentos.
Com nosso sistema, você pode conseguir mais pacientes de implante.
Entre em contato para saber mais sobre nossos serviços.
Nossa equipe está disponível para atendê-lo com excelência.
Trabalhamos com as melhores estratégias do mercado para resultados consistentes."""

_scorer = None


def get_scorer():
    global _scorer
    if _scorer is None:
        from tribev2.copy_brain import CopyBrainScorer
        cache = os.environ.get("TRIBE_CACHE", "./cache")
        _scorer = CopyBrainScorer.load(cache_folder=cache)
    return _scorer


def score_copy(copy_text: str, do_segment: bool) -> tuple:
    """Score copy and return formatted outputs."""
    if not copy_text or not copy_text.strip():
        return (
            "⚠️ Please enter some copy text.",
            None, None, None, "—"
        )

    try:
        scorer = get_scorer()
        result = scorer.score_copy(copy_text, segment=do_segment)
    except Exception as e:
        return (f"❌ Error: {str(e)}", None, None, None, "—")

    # Text summary
    summary = result.summary() + "\n\n— Copy Brain OS · @ryanribeirob"

    # Radar chart (matplotlib → Gradio)
    try:
        import matplotlib.pyplot as plt
        from tribev2.copy_brain import plot_filter_radar, plot_filter_timeseries, plot_section_heatmap

        fig_radar, _ = plot_filter_radar(result)
        fig_ts, _ = plot_filter_timeseries(result)

        if result.section_results:
            fig_heat, _ = plot_section_heatmap(result)
        else:
            fig_heat = None
    except Exception:
        fig_radar = fig_ts = fig_heat = None

    # JSON output
    json_out = result.to_json()

    return summary, fig_radar, fig_ts, fig_heat, json_out


def compare_versions(copy_a: str, copy_b: str) -> str:
    """Run A/B neural comparison."""
    if not copy_a.strip() or not copy_b.strip():
        return "⚠️ Both versions required for comparison."

    try:
        scorer = get_scorer()
        comparison = scorer.compare_versions(
            copy_a, copy_b,
            labels=("Version A", "Version B")
        )
    except Exception as e:
        return f"❌ Error: {str(e)}"

    lines = ["# A/B Neural Comparison", ""]
    lines.append(f"**Winner: {comparison['winner']}**")
    lines.append(f"Mean activation improvement: +{comparison['improvement']:.3f}")
    lines.append("")
    lines.append("### Per-filter deltas (+ = Version B wins)")

    from tribev2.copy_brain import FILTER_LABELS
    for filt, delta in comparison.get("per_filter_delta", {}).items():
        fname = FILTER_LABELS.get(filt, filt)
        sign = "+" if delta >= 0 else ""
        winner_icon = "🟢" if delta > 0.02 else ("🔴" if delta < -0.02 else "⚪")
        lines.append(f"- {winner_icon} **{fname}**: {sign}{delta:.3f}")

    lines.append("")
    lines.append("— Copy Brain OS · @ryanribeirob")
    return "\n".join(lines)


# ─── Gradio UI ────────────────────────────────────────────────────────────────

with gr.Blocks(
    title="Copy Brain OS — Neural Copy Scoring",
    theme=gr.themes.Base(
        primary_hue="purple",
        neutral_hue="slate",
        font=gr.themes.GoogleFont("JetBrains Mono"),
    ),
    css="""
    .gradio-container { background: #0D0D1A; }
    .gr-prose { color: #E8E8F0; }
    h1 { color: #9B7EE8 !important; }
    h2 { color: #7C5CBF !important; }
    .gr-button-primary { background: #7C5CBF !important; }
    """,
) as demo:

    gr.Markdown("""
    # 🧠 Copy Brain OS
    ### por @ryanribeirob · neural copy scoring powered by TRIBE v2 (Meta FAIR)

    Scores your copy against **7 neuro-persuasion filters** derived from 15 peer-reviewed
    frameworks. Maps fMRI predictions to attention, emotion, memory, decision, language,
    reward, and predictive processing circuits.

    > **License:** CC BY-NC-4.0 — non-commercial research use only.
    """)

    with gr.Tab("Score Copy"):
        with gr.Row():
            with gr.Column():
                copy_input = gr.Textbox(
                    label="Copy Text",
                    placeholder="Paste your copy here...",
                    lines=12,
                    value=SAMPLE_COPY,
                )
                do_segment = gr.Checkbox(
                    label="Segment by funnel section (HOOK → OFERTA/CTA)",
                    value=True,
                )
                score_btn = gr.Button("🧠 Run Neural Analysis", variant="primary")

            with gr.Column():
                summary_out = gr.Textbox(
                    label="Analysis Report",
                    lines=20,
                    interactive=False,
                )

        with gr.Row():
            radar_out = gr.Plot(label="Filter Radar (F1–F7)")
            ts_out = gr.Plot(label="Time Series per Filter")

        heat_out = gr.Plot(label="Section Heatmap (filter × section)")
        json_out = gr.JSON(label="Raw JSON Output")

        score_btn.click(
            fn=score_copy,
            inputs=[copy_input, do_segment],
            outputs=[summary_out, radar_out, ts_out, heat_out, json_out],
        )

    with gr.Tab("A/B Neural Test"):
        gr.Markdown("""
        Compare two versions of a copy (hook, headline, CTA) at the neural level.
        TRIBE v2 runs inference on both and returns per-filter deltas.
        """)
        with gr.Row():
            ab_a = gr.Textbox(
                label="Version A",
                lines=8,
                value=SAMPLE_COPY_B,
                placeholder="Version A (control)...",
            )
            ab_b = gr.Textbox(
                label="Version B",
                lines=8,
                value=SAMPLE_COPY[:300],
                placeholder="Version B (challenger)...",
            )
        ab_btn = gr.Button("⚡ Compare Versions", variant="primary")
        ab_out = gr.Markdown(label="Comparison Result")

        ab_btn.click(
            fn=compare_versions,
            inputs=[ab_a, ab_b],
            outputs=[ab_out],
        )

    with gr.Tab("The 7 Filters"):
        gr.Markdown("""
        ## F1–F7: Neuro-Persuasion Filters

        | Filter | Brain Region (proxy) | Foundation | Threshold |
        |--------|---------------------|------------|-----------|
        | **F1 Atenção** | Insula + ACC + Visual cortex | Loewenstein Gap Theory; Friston | ≥0.75 |
        | **F2 Emoção** | Insula + OFC + Temporal pole | Damasio Somatic Marker; LeDoux | ≥0.79 |
        | **F3 Memória** | Parahippocampal + Fusiform | Paivio Dual Coding; Heath SUCCESs | ≥0.72 |
        | **F4 Decisão** | Superior frontal + Precuneus | Kahneman Prospect Theory; Cialdini | ≥0.75 |
        | **F5 Linguagem** | Broca + Wernicke + Angular | Flesch Readability; Sweller CLT | ≥0.73 |
        | **F6 Recompensa** | OFC + Frontal pole + PCC | Schultz Dopamine; Ainslie | ≥0.75 |
        | **F7 Predição** | PCC + Precuneus + TPJ + ACC | Friston Free Energy; Clark | ≥0.71 |

        ### Funnel Section Mapping

        | Section | Primary Filters |
        |---------|----------------|
        | HOOK (0–10%) | F1 Atenção + F7 Predição |
        | PROBLEMA (10–30%) | F2 Emoção + F3 Memória |
        | SOLUÇÃO (30–55%) | F3 Memória + F5 Linguagem + F7 Predição |
        | PROVA (55–75%) | F3 Memória + F4 Decisão |
        | OFERTA/CTA (75–100%) | F4 Decisão + F6 Recompensa + F7 Predição |

        ### Why F7 is the Key Differentiator

        F7 (Predictive Processing) is unique to Copy Brain OS. Based on Karl Friston's
        Free Energy Principle — the brain is an active prediction machine.
        High-converting copy generates productive expectation violations that force
        belief updating. F7 captures this: posterior cingulate + precuneus (prediction
        generation) + anterior cingulate (prediction error). No other ad scoring system
        has this filter.
        """)

    with gr.Tab("Setup"):
        gr.Markdown(f"""
        ## Setup Requirements

        ```bash
        # 1. Install TRIBE v2 (from this repo)
        pip install -e ".[plotting]"

        # 2. Install additional dependencies
        pip install nilearn gradio gtts langdetect

        # 3. Authenticate with HuggingFace (TRIBE uses LLaMA 3.2 — gated)
        huggingface-cli login
        # Accept terms at: https://huggingface.co/meta-llama/Llama-3.2-3B

        # 4. Run locally
        python app.py
        # or
        gradio app.py
        ```

        ### HuggingFace Spaces Deployment

        1. Create a new Space (GPU recommended: A10G)
        2. Push this repository
        3. Add secret: `HF_TOKEN` with your HuggingFace token
        4. First run downloads model (~1GB) to cache

        ### Reference HF Space
        - `vishnuverse-in/ad-brain-scorer` — original ad scoring Space with TRIBE v2
        - Copy Brain OS adds 7 persuasion filters + F7 + section scoring + A/B neural test

        ---
        **License:** CC BY-NC-4.0 — non-commercial use only.
        Built on TRIBE v2 by Meta FAIR (d'Ascoli et al., 2026).
        """)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
    )
