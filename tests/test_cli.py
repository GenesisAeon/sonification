"""Tests for the sonification CLI commands."""

from typer.testing import CliRunner

from sonification.cli import app

runner = CliRunner()


def test_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.output


def test_wave_command(tmp_path):
    output = tmp_path / "test.wav"
    result = runner.invoke(
        app, ["wave", "--freq", "440.0", "--duration", "1.0", "--output", str(output)]
    )
    assert result.exit_code == 0, result.output
    assert output.exists()
    assert "Saved" in result.output


def test_wave_command_default_output(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(app, ["wave", "--duration", "0.5"])
    assert result.exit_code == 0, result.output
    assert (tmp_path / "entropy_wave.wav").exists()


def test_entropy_gate_command(tmp_path):
    output = tmp_path / "test.mid"
    result = runner.invoke(
        app, ["entropy-gate", "--beta", "0.5", "--notes", "4", "--output", str(output)]
    )
    assert result.exit_code == 0, result.output
    assert output.exists()
    assert "UTAC MIDI saved" in result.output


def test_entropy_gate_default_output(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(app, ["entropy-gate"])
    assert result.exit_code == 0, result.output
    assert (tmp_path / "utac_midi.mid").exists()


def test_mandala_command():
    result = runner.invoke(app, ["mandala", "--bpm", "90"])
    assert result.exit_code == 0, result.output
    assert "Mandala rhythm" in result.output
    assert "90 BPM" in result.output
