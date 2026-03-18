# sonification

**The auditory layer of the GenesisAeon stack** – turn entropy waves, UTAC thresholds, cosmic moments and mandala resonance into audible tones, rhythms and soundscapes.

## Install

```bash
pip install sonification
# or
uv tool install sonification
```

With full stack integration:

```bash
pip install sonification[stack]
```

## Quickstart

```bash
# φ-based entropy sine tone → WAV
soni wave --freq 1.618 --duration 5

# UTAC β threshold → MIDI
soni entropy-gate --beta 0.0625

# Mandala resonance → rhythm pattern
soni mandala --bpm 120
```

## Stack position

```
fieldtheory → sigillin → utac-core → mandala-visualizer → sonification
```

| Source | Output |
|--------|--------|
| Entropy wave (φ) | Sine tone → WAV |
| UTAC β threshold | Pitch sequence → MIDI |
| Mandala resonance | Rhythm pattern |

## Citation

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19086583.svg)](https://doi.org/10.5281/zenodo.19086583)

If you use this software in your research, please cite it:

```bibtex
@software{genesisaeon_sonification,
  author    = {GenesisAeon Team},
  title     = {sonification},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.19086583},
  url       = {https://doi.org/10.5281/zenodo.19086583}
}
```
