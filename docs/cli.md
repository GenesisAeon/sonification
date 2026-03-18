# CLI Reference

## `soni wave`

Generate an entropy-wave sine tone and save it as a WAV file.

```
Usage: soni wave [OPTIONS]

Options:
  --freq      FLOAT  Frequency in Hz (default φ = 1.618)
  --duration  FLOAT  Duration in seconds [default: 5.0]
  --output    TEXT   Output WAV filename [default: entropy_wave.wav]
  --amplitude FLOAT  Peak amplitude in [0, 1] [default: 0.5]
```

**Examples**

```bash
soni wave
soni wave --freq 440.0 --duration 2.0 --output tone_440.wav
soni wave --freq 1.618 --amplitude 0.8
```

---

## `soni entropy-gate`

Map a UTAC β threshold to a MIDI pitch sequence.

```
Usage: soni entropy-gate [OPTIONS]

Options:
  --beta    FLOAT  UTAC β threshold in (0, 1] [default: 0.0625]
  --notes   INT    Number of MIDI notes [default: 8]
  --tempo   INT    Tempo in BPM [default: 120]
  --output  TEXT   Output MIDI filename [default: utac_midi.mid]
```

**Examples**

```bash
soni entropy-gate
soni entropy-gate --beta 0.5 --notes 16
```

---

## `soni mandala`

Extract a rhythm pattern from a mandala resonance signal.

```
Usage: soni mandala [OPTIONS]

Options:
  --bpm  INT  BPM for rhythm mapping [default: 120]
```

**Examples**

```bash
soni mandala
soni mandala --bpm 90
```

---

## `soni version`

Print the installed version.

```bash
soni version
```
