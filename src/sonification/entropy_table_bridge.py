"""Bridge between sonification and entropy-table (optional [stack] dependency)."""

from __future__ import annotations

from pathlib import Path


class SonificationBridge:
    """Persist sonification domain relations via entropy-table.

    Requires the ``[stack]`` optional dependencies to be installed.
    Import is deferred so the package is usable without them.
    """

    def __init__(self) -> None:
        try:
            from entropy_table import EntropyTable  # type: ignore[import]

            self._table = EntropyTable(domain="sonification")
        except ModuleNotFoundError as exc:
            raise ImportError(
                "entropy-table is not installed. "
                "Run `pip install sonification[stack]` to enable stack integration."
            ) from exc

    def add_sound(self, key: str, value: str) -> None:
        """Add a key→value relation to the sonification domain."""
        self._table.add_relation(key, value)

    def export(self, filepath: Path | str = "domains.yaml") -> Path:
        """Export the domain table to a YAML file."""
        self._table.export(filepath)
        return Path(filepath)
