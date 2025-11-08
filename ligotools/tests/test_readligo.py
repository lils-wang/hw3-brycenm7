from ligotools import read_hdf5, loaddata
import numpy as np


def test_read_hdf5():
    data = read_hdf5("data/H-H1_LOSC_4_V2-1126259446-32.hdf5")
    assert isinstance(data, tuple)


def test_loaddata():
    strain, meta, channel_dict = loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5")

    assert isinstance(strain, np.ndarray)
