"""Core sonification engine – data to sound mappings."""

from __future__ import annotations

import numpy as np
from midiutil import MIDIFile
from scipy.io import wavfile


def entropy_wave_to_audio(
    freq: float = 1.618,
    duration: float = 5.0,
    sample_rate: int = 44100,
    amplitude: float = 0.5,
) -> np.ndarray:
    """Convert an entropy frequency to a sine-wave audio array.

    Args:
        freq: Frequency in Hz (default φ = 1.618).
        duration: Duration in seconds.
        sample_rate: Audio sample rate in Hz.
        amplitude: Peak amplitude in [0, 1].

    Returns:
        1-D float32 array of audio samples.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    return wave.astype(np.float32)


def save_wave(
    wave: np.ndarray,
    filename: str = "entropy_wave.wav",
    sample_rate: int = 44100,
) -> str:
    """Save a float32 wave array as a 16-bit WAV file.

    Args:
        wave: Audio samples in [-1, 1].
        filename: Output path.
        sample_rate: Audio sample rate in Hz.

    Returns:
        The filename written.
    """
    pcm = (np.clip(wave, -1.0, 1.0) * 32767).astype(np.int16)
    wavfile.write(filename, sample_rate, pcm)
    return filename


def utac_to_midi(
    beta: float = 0.0625,
    notes: int = 8,
    tempo: int = 120,
    filename: str = "utac_midi.mid",
) -> str:
    """Map a UTAC β value to a MIDI sequence and write it to disk.

    Higher β → higher pitches, spanning two octaves above middle C.

    Args:
        beta: UTAC logistic threshold in (0, 1].
        notes: Number of notes in the sequence.
        tempo: BPM for the MIDI track.
        filename: Output path.

    Returns:
        The filename written.
    """
    midi = MIDIFile(1)
    track, channel, time = 0, 0, 0
    midi.addTempo(track, time, tempo)

    for i in range(notes):
        pitch = int(60 + 24 * beta * i)  # C4 base + β-scaled offset
        pitch = max(21, min(108, pitch))  # clamp to standard piano range
        midi.addNote(track, channel, pitch, time + i, 1, 100)

    with open(filename, "wb") as f:
        midi.writeFile(f)
    return filename


def mandala_resonance_to_rhythm(
    resonance: np.ndarray,
    bpm: int = 120,
) -> list[float]:
    """Extract beat times from a mandala resonance signal.

    Peaks above the mean are converted to beat-time offsets (in seconds).

    Args:
        resonance: 1-D array of resonance values.
        bpm: Beats per minute for time-mapping.

    Returns:
        List of beat-time positions in seconds.
    """
    if resonance.size == 0:
        return []
    peaks = np.where(resonance > np.mean(resonance))[0]
    beat_duration = 60.0 / bpm
    return [float(p / len(resonance) * beat_duration) for p in peaks]
