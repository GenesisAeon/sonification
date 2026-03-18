"""Sonification – auditory layer for the GenesisAeon stack."""

__version__ = "0.1.0"

from .core import (
    entropy_wave_to_audio,
    mandala_resonance_to_rhythm,
    save_wave,
    utac_to_midi,
)

__all__ = [
    "__version__",
    "entropy_wave_to_audio",
    "save_wave",
    "utac_to_midi",
    "mandala_resonance_to_rhythm",
]
