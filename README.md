# sonification

**The auditory layer of the GenesisAeon stack** – turn entropy waves, UTAC thresholds, cosmic moments and mandala resonance into audible tones, rhythms and soundscapes.

[![CI](https://github.com/GenesisAeon/sonification/actions/workflows/ci.yml/badge.svg)](https://github.com/GenesisAeon/sonification/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/sonification)](https://pypi.org/project/sonification/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19086583.svg)](https://doi.org/10.5281/zenodo.19086583)

---

## Install

```bash
pip install sonification
# or
uv tool install sonification
```

With full GenesisAeon stack integration:

```bash
pip install sonification[stack]
```

## Quick start

```bash
# Entropy wave → WAV (φ-based frequency, 5 seconds)
soni wave --freq 1.618 --duration 5

# UTAC threshold → MIDI sequence
soni entropy-gate --beta 0.0625

# Mandala resonance → rhythm pattern
soni mandala --bpm 120
```

## Python API

```python
import numpy as np
from sonification import entropy_wave_to_audio, save_wave, utac_to_midi

# Generate a φ-frequency sine tone
wave = entropy_wave_to_audio(freq=1.618, duration=5.0)
save_wave(wave, "entropy_wave.wav")

# Map a UTAC β value to a MIDI sequence
utac_to_midi(beta=0.0625, notes=8, filename="utac_midi.mid")
```

## Stack position

```
fieldtheory → sigillin → utac-core → mandala-visualizer → sonification
```

`sonification` is the **audio layer** – it listens to the stack and makes data audible.

| Source | Output |
|--------|--------|
| Entropy wave (φ) | Sine tone → WAV |
| UTAC β threshold | Pitch sequence → MIDI |
| Mandala resonance | Rhythm pattern |

## CLI reference

```
soni wave          Generate entropy-wave sine tone (WAV)
soni entropy-gate  Sonify UTAC threshold (MIDI)
soni mandala       Sonify mandala resonance (rhythm)
soni version       Show installed version
```

---

Built with [numpy](https://numpy.org/) · [scipy](https://scipy.org/) · [midiutil](https://github.com/MarkCWirt/MIDIUtil) · [Typer](https://typer.tiangolo.com/) · [Rich](https://rich.readthedocs.io/)

---

## Citation

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

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19086583.svg)](https://doi.org/10.5281/zenodo.19086583)
