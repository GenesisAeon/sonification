# API Reference

## `sonification.core`

### `entropy_wave_to_audio`

```python
entropy_wave_to_audio(
    freq: float = 1.618,
    duration: float = 5.0,
    sample_rate: int = 44100,
    amplitude: float = 0.5,
) -> np.ndarray
```

Convert an entropy frequency to a sine-wave audio array (float32).

| Parameter | Description |
|-----------|-------------|
| `freq` | Frequency in Hz — default φ = 1.618 |
| `duration` | Duration in seconds |
| `sample_rate` | Audio sample rate in Hz |
| `amplitude` | Peak amplitude in [0, 1] |

---

### `save_wave`

```python
save_wave(
    wave: np.ndarray,
    filename: str = "entropy_wave.wav",
    sample_rate: int = 44100,
) -> str
```

Save a float32 wave array as a 16-bit WAV file. Values outside `[-1, 1]` are clipped.

---

### `utac_to_midi`

```python
utac_to_midi(
    beta: float = 0.0625,
    notes: int = 8,
    tempo: int = 120,
    filename: str = "utac_midi.mid",
) -> str
```

Map a UTAC β value to a MIDI note sequence. Higher β → higher pitches, clamped to the standard piano range [21, 108].

---

### `mandala_resonance_to_rhythm`

```python
mandala_resonance_to_rhythm(
    resonance: np.ndarray,
    bpm: int = 120,
) -> list[float]
```

Extract beat-time offsets (seconds) from peaks in a mandala resonance signal.

---

## `sonification.entropy_table_bridge`

### `SonificationBridge`

Optional [stack] integration with entropy-table. Requires `pip install sonification[stack]`.

```python
from sonification.entropy_table_bridge import SonificationBridge

bridge = SonificationBridge()
bridge.add_sound("phi_freq", "1.618")
bridge.export("domains.yaml")
```
