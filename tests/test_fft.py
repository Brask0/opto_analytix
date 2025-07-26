# Test du module analysis.fft
import numpy as np
from analysis import fft

def test_fft_compute_fft():
    # Signal sinusoïdal simple
    fs = 1000
    t = np.arange(0, 1, 1/fs)
    signal = np.sin(2 * np.pi * 50 * t)
    result = fft.compute_fft(signal, fs)
    assert isinstance(result, dict)
    assert 'freqs' in result and 'amplitudes' in result
    assert len(result['freqs']) == len(result['amplitudes'])
