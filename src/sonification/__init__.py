"""Sonification – auditory layer for the GenesisAeon stack."""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _version

try:
    __version__ = _version("genesisaeon-sonification")
except PackageNotFoundError:  # pragma: no cover - not installed, e.g. running from source
    __version__ = "0.0.0+unknown"

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

