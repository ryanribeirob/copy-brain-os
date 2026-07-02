#!/bin/bash
# Copy Brain OS — Installation Script
# License: CC BY-NC-4.0 (non-commercial use only)
# Prerequisites: Python 3.11+, pip

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "========================================"
echo " COPY BRAIN OS — Installation"
echo " Built on TRIBE v2 (Meta FAIR)"
echo "========================================"
echo ""

# ── 1. System dependencies ──────────────────────────────────────────────────
echo "[1/6] Checking system dependencies..."
if command -v apt-get &> /dev/null; then
    sudo apt-get install -y ffmpeg libsndfile1 2>/dev/null || echo "  (apt-get install skipped — may need manual install of ffmpeg)"
elif command -v brew &> /dev/null; then
    brew install ffmpeg 2>/dev/null || echo "  (brew install skipped)"
fi
echo "  ✓ System deps checked"

# ── 2. Python base packages ─────────────────────────────────────────────────
echo "[2/6] Upgrading pip..."
pip install --upgrade pip --quiet
echo "  ✓ pip upgraded"

# ── 3. TRIBE v2 (this repo) ─────────────────────────────────────────────────
echo "[3/6] Installing TRIBE v2 + Copy Brain OS (this repo)..."
cd "$SCRIPT_DIR"

MODE="${1:-basic}"
if [[ "$MODE" == "full" ]]; then
    pip install -e ".[plotting,training]" --quiet
    echo "  ✓ tribev2[plotting,training] installed (full mode)"
else
    pip install -e ".[plotting]" --quiet
    echo "  ✓ tribev2[plotting] installed"
fi

# ── 4. Additional Copy Brain OS dependencies ────────────────────────────────
echo "[4/6] Installing Copy Brain OS dependencies..."
pip install \
    nilearn \
    gtts \
    langdetect \
    gradio \
    --quiet
echo "  ✓ Copy Brain OS deps installed (nilearn, gtts, langdetect, gradio)"

# ── 5. HuggingFace authentication ──────────────────────────────────────────
echo ""
echo "[5/6] HuggingFace Authentication"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  TRIBE v2 uses LLaMA 3.2-3B (gated model on HuggingFace)."
echo ""
echo "  Required steps:"
echo "  1. Accept terms: https://huggingface.co/meta-llama/Llama-3.2-3B"
echo "  2. Create read token: https://huggingface.co/settings/tokens"
echo "  3. Run: huggingface-cli login"
echo ""

if python -c "from huggingface_hub import HfApi; HfApi().whoami()" 2>/dev/null; then
    echo "  ✓ Already authenticated with HuggingFace"
else
    read -r -p "  Run huggingface-cli login now? (y/n): " DO_LOGIN
    if [[ "$DO_LOGIN" =~ ^[Yy]$ ]]; then
        huggingface-cli login
    else
        echo "  ⚠️  Remember to run 'huggingface-cli login' before first use"
    fi
fi

# ── 6. Verify installation ─────────────────────────────────────────────────
echo ""
echo "[6/6] Verifying installation..."
python -c "
import sys
errors = []
warnings = []

def check(name, import_str):
    try:
        exec(import_str)
        print(f'  ✓ {name}')
    except ImportError as e:
        errors.append(f'  ✗ {name}: {e}')

check('tribev2', 'import tribev2')
check('tribev2.copy_brain', 'from tribev2.copy_brain import CopyBrainScorer, CopyBrainResult')
check('tribev2.copy_brain.report', 'from tribev2.copy_brain.report import generate_html_report')
check('nilearn', 'from nilearn import datasets')
check('gtts', 'from gtts import gTTS')
check('gradio', 'import gradio')
check('matplotlib', 'import matplotlib.pyplot as plt')
check('numpy', 'import numpy as np')

if errors:
    print()
    print('ERRORS:')
    for e in errors:
        print(e)
    sys.exit(1)
else:
    print()
    print('  ✓ All checks passed!')
"

echo ""
echo "========================================"
echo " USAGE:"
echo ""
echo " # Score copy (Python):"
echo " from tribev2.copy_brain import CopyBrainScorer"
echo " scorer = CopyBrainScorer.load()   # ~1GB download first time"
echo " result = scorer.score_copy('Your copy text here...', segment=True)"
echo " print(result.summary())"
echo ""
echo " # HTML visualization:"
echo " from tribev2.copy_brain import open_html_report"
echo " open_html_report(result)          # opens in browser"
echo ""
echo " # Interactive Gradio app:"
echo " python app.py"
echo " # → http://localhost:7860"
echo ""
echo " # Notebook demo:"
echo " jupyter notebook copy_brain_demo.ipynb"
echo "========================================"
