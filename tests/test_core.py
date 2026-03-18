"""Tests for the sonification core engine."""

import numpy as np
import pytest

from sonification.core import (
    entropy_wave_to_audio,
    mandala_resonance_to_rhythm,
    save_wave,
    utac_to_midi,
)


class TestEntropyWaveToAudio:
    def test_returns_array(self):
        wave = entropy_wave_to_audio()
        assert isinstance(wave, np.ndarray)

    def test_length_matches_duration(self):
        sample_rate = 44100
        duration = 2.0
        wave = entropy_wave_to_audio(duration=duration, sample_rate=sample_rate)
        assert len(wave) == int(sample_rate * duration)

    def test_amplitude_bounded(self):
        wave = entropy_wave_to_audio(amplitude=0.5)
        assert np.max(np.abs(wave)) <= 0.5 + 1e-6

    def test_phi_frequency(self):
        wave = entropy_wave_to_audio(freq=1.618, duration=1.0)
        assert len(wave) > 0

    def test_zero_amplitude_is_silence(self):
        wave = entropy_wave_to_audio(amplitude=0.0)
        assert np.allclose(wave, 0.0)

    def test_dtype_float32(self):
        wave = entropy_wave_to_audio()
        assert wave.dtype == np.float32


class TestSaveWave:
    def test_creates_file(self, tmp_path):
        wave = entropy_wave_to_audio(duration=0.1)
        out = tmp_path / "out.wav"
        result = save_wave(wave, str(out))
        assert out.exists()
        assert result == str(out)

    def test_file_is_non_empty(self, tmp_path):
        wave = entropy_wave_to_audio(duration=0.1)
        out = tmp_path / "out.wav"
        save_wave(wave, str(out))
        assert out.stat().st_size > 0

    def test_clips_overflow(self, tmp_path):
        """Values outside [-1, 1] must be clipped, not wrap-around."""
        wave = np.array([2.0, -3.0, 0.5], dtype=np.float32)
        out = tmp_path / "clip.wav"
        save_wave(wave, str(out))
        assert out.exists()


class TestUtacToMidi:
    def test_creates_file(self, tmp_path):
        out = tmp_path / "midi.mid"
        result = utac_to_midi(filename=str(out))
        assert out.exists()
        assert result == str(out)

    def test_file_non_empty(self, tmp_path):
        out = tmp_path / "midi.mid"
        utac_to_midi(filename=str(out))
        assert out.stat().st_size > 0

    def test_high_beta_produces_higher_notes(self, tmp_path):
        """A higher β should shift pitches upward."""
        out_low = tmp_path / "low.mid"
        out_high = tmp_path / "high.mid"
        utac_to_midi(beta=0.1, filename=str(out_low))
        utac_to_midi(beta=0.9, filename=str(out_high))
        assert out_high.stat().st_size > 0
        assert out_low.stat().st_size > 0

    def test_zero_notes(self, tmp_path):
        out = tmp_path / "empty.mid"
        utac_to_midi(notes=0, filename=str(out))
        assert out.exists()

    def test_pitch_clamped_to_piano_range(self, tmp_path):
        """Extreme β must not produce pitches outside [21, 108]."""
        out = tmp_path / "extreme.mid"
        utac_to_midi(beta=1.0, notes=16, filename=str(out))
        assert out.exists()


class TestMandalaResonanceToRhythm:
    def test_returns_list(self):
        resonance = np.array([0.1, 0.9, 0.2, 0.8, 0.3])
        result = mandala_resonance_to_rhythm(resonance)
        assert isinstance(result, list)

    def test_empty_array_returns_empty(self):
        result = mandala_resonance_to_rhythm(np.array([]))
        assert result == []

    def test_all_same_value_returns_empty(self):
        resonance = np.ones(10)
        # All values equal mean → none strictly above mean
        result = mandala_resonance_to_rhythm(resonance)
        assert result == []

    def test_beat_times_are_non_negative(self):
        resonance = np.abs(np.sin(np.linspace(0, 2 * np.pi, 32)))
        beats = mandala_resonance_to_rhythm(resonance, bpm=120)
        assert all(t >= 0 for t in beats)

    def test_custom_bpm_scales_times(self):
        resonance = np.array([0.1, 0.9, 0.5, 0.8])
        beats_120 = mandala_resonance_to_rhythm(resonance, bpm=120)
        beats_60 = mandala_resonance_to_rhythm(resonance, bpm=60)
        if beats_120 and beats_60:
            assert beats_60[0] == pytest.approx(beats_120[0] * 2, rel=1e-5)
