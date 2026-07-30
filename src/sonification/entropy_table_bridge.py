"""Bridge between sonification and entropy-table (optional [stack] dependency)."""

from __future__ import annotations

from pathlib import Path


class SonificationBridge:
    """Persist sonification domain relations via entropy-table.

    Requires the ``[stack]`` optional dependencies to be installed.
    Import is deferred so the package is usable without them.

    Raises:
        ImportError: if ``entropy-table`` is not installed at all.
        RuntimeError: if ``entropy-table`` is installed but its API no
            longer matches what this bridge expects (see below).
    """

    def __init__(self) -> None:
        from importlib.metadata import PackageNotFoundError
        from importlib.metadata import version as _version

        try:
            _installed_version: str | None = _version("entropy-table")
        except PackageNotFoundError:
            _installed_version = None

        try:
            from entropy_table import EntropyTable  # type: ignore

            self._table = EntropyTable(domain="sonification")
        except ImportError as exc:
            if _installed_version is None:
                raise ImportError(
                    "entropy-table is not installed. "
                    "Run `pip install genesisaeon-sonification[stack]` "
                    "to enable stack integration."
                ) from exc
            # entropy-table >=2.0 removed the EntropyTable class entirely
            # in favor of a different "contract-first" case/claim-ID data
            # model. This bridge was written against the pre-2.0 API and
            # was never updated, so it previously raised a misleading
            # "not installed" error even when a real, installed
            # entropy-table package was present -- and even that message
            # never actually fired, since it only caught
            # ModuleNotFoundError, not the plain ImportError Python raises
            # when a name (not the module) can't be found. Found via an
            # ecosystem-wide sweep of sibling bridge files after the same
            # bug was confirmed in climate-dashboard.
            raise RuntimeError(
                f"entropy-table {_installed_version} is installed, but its API no "
                "longer matches what this bridge expects (no EntropyTable class "
                "-- entropy-table >=2.0 replaced the domain-relation model "
                "entirely). This bridge needs updating for the current "
                "entropy-table API; it is not simply a missing dependency."
            ) from exc

    def add_sound(self, key: str, value: str) -> None:
        """Add a key→value relation to the sonification domain."""
        self._table.add_relation(key, value)

    def export(self, filepath: Path | str = "domains.yaml") -> Path:
        """Export the domain table to a YAML file."""
        self._table.export(filepath)
        return Path(filepath)
