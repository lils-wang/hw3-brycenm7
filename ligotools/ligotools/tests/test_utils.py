from ligotools.utils import write_wavfile, reqshift
import numpy as np
from scipy.io import wavfile


def test_write_wavdata(tmp_path):
    n = 1000
    test_data = np.random.normal(0, 1, n)
    test_file = tmp_path / "test_output.wav"
    write_wavfile(test_file, n, test_data)

    assert test_file.exists()


def test_reqshift():
    n = 1000
    data = np.random.normal(0, 1, n)
    new_data = reqshift(data)

    assert isinstance(new_data, np.ndarray)
    assert not np.array_equal(data, new_data)