"""Autograding script."""

import os


def test_01():
    """Test word count job."""

    assert os.path.exists("files/input/summary.csv")
    assert os.path.exists("files/input/top10_drivers.png")
