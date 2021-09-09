from constant import TEST_CSV_PATH
import pytest
import csv


@pytest.fixture
def rentals_data():
    return list(csv.DictReader(open(TEST_CSV_PATH, "r")))
