"""Sonification CLI – data to sound for the GenesisAeon stack."""

from __future__ import annotations

import typer
from rich.console import Console

from .core import (
    entropy_wave_to_audio,
    mandala_resonance_to_rhythm,
    save_wave,
    utac_to_midi,
)

app = typer.Typer(
    name="soni",
    help="Sonification CLI – data to sound for the GenesisAeon stack.",
    add_completion=False,
)
console = Console()


@app.command()
def version() -> None:
    """Show the installed sonification version."""
    from . import __version__

    console.print(f"[bold]sonification[/] {__version__}")


@app.command()
def wave(
    freq: float = typer.Option(1.618, help="Frequency in Hz (default φ)."),
    duration: float = typer.Option(5.0, help="Duration in seconds."),
    output: str = typer.Option("entropy_wave.wav", help="Output WAV filename."),
    amplitude: float = typer.Option(0.5, help="Peak amplitude in [0, 1]."),
) -> None:
    """Generate an entropy-wave sine tone and save it as a WAV file."""
    audio = entropy_wave_to_audio(freq=freq, duration=duration, amplitude=amplitude)
    save_wave(audio, filename=output)
    console.print(f"[bold green]Saved[/] {output}  ({freq} Hz, {duration}s)")


@app.command()
def entropy_gate(
    beta: float = typer.Option(0.0625, help="UTAC β threshold in (0, 1]."),
    notes: int = typer.Option(8, help="Number of MIDI notes."),
    tempo: int = typer.Option(120, help="Tempo in BPM."),
    output: str = typer.Option("utac_midi.mid", help="Output MIDI filename."),
) -> None:
    """Sonify a UTAC entropy-gate threshold as a MIDI sequence."""
    midi_file = utac_to_midi(beta=beta, notes=notes, tempo=tempo, filename=output)
    console.print(f"[bold cyan]UTAC MIDI saved to[/] {midi_file}  (β={beta}, {notes}n)")


@app.command()
def mandala(
    bpm: int = typer.Option(120, help="BPM for rhythm mapping."),
) -> None:
    """Sonify mandala resonance as a rhythm pattern (placeholder)."""
    import numpy as np

    # Placeholder resonance – integrate with mandala-visualizer via [stack] extra
    resonance = np.abs(np.sin(np.linspace(0, 4 * np.pi, 64)))
    beats = mandala_resonance_to_rhythm(resonance, bpm=bpm)
    console.print(f"[bold magenta]Mandala rhythm:[/] {len(beats)} beat(s) at {bpm} BPM")
    for i, t in enumerate(beats[:8]):
        console.print(f"  beat {i + 1:02d}: {t:.4f}s")


if __name__ == "__main__":
    app()
