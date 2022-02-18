# -*- coding: utf-8 -*-
"""
@date Created on Mon May 25 2020
@author martin_g for Eomys
"""

# Third party imports
import numpy as np
import matplotlib.pyplot as plt
import pytest
from pandas import ExcelFile, read_excel

# Local application imports
from mosqito.sq_metrics import loudness_zwtv
from mosqito.functions.shared.load import load
from validations.loudness_zwicker.validation_loudness_zwicker_time import (
    check_compliance,
)


@pytest.mark.loudness_zwtv  # to skip or run only loudness zwicker time-varying tests
def test_loudness_zwicker_time():
    """Test function for the script loudness_zwicker_time

    Test function for the script loudness_zwicker_time with
    .wav file as input. The input file is provided by ISO 532-1 annex
    B4 and B5, the compliance is assessed according to section 6.1 of the
    standard. One .png compliance plot is generated.

    Parameters
    ----------
    None

    Outputs
    -------
    None
    """
    # Test signal as input for time-varying loudness
    # (from ISO 532-1 annex B4)
    signal = {
        "data_file": "tests/input/Test signal 10 (tone pulse 1 kHz 10 ms 70 dB).wav",
        "xls": "tests/input/Results and tests for synthetic signals (time varying loudness).xlsx",
        "tab": "Test signal 10",
        "N_specif_bark": 8.5,
        "field": "free",
    }

    # Load signal and compute third octave band spectrum
    sig, fs = load(signal["data_file"], calib=2 * 2 ** 0.5)

    # Compute Loudness
    N, N_spec, bark_axis, _ = loudness_zwtv(sig, fs, signal["field"])
    loudness = {
        "name": "Loudness",
        "values": N,
        "specific values": N_spec,
        "freqs": bark_axis,
    }

    # Check ISO 532-1 compliance
    assert check_compliance(loudness, signal, "./tests/output/")


# test de la fonction
if __name__ == "__main__":
    test_loudness_zwicker_time()
