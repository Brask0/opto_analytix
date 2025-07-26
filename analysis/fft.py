import numpy as np

def compute_fft(data, sampling_rate):
    freqs = np.fft.rfftfreq(len(data), d=1./sampling_rate)
    fft_vals = np.abs(np.fft.rfft(data))
    return list(zip(freqs, fft_vals))
