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
field-theory → sigillin → utac-core → mandala-visualizer → sonification
```

| Source | Output |
|--------|--------|
| Entropy wave (φ) | Sine tone → WAV |
| UTAC β threshold | Pitch sequence → MIDI |
| Mandala resonance | Rhythm pattern |
