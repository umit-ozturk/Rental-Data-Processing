from utils import filter_by_lease_years
from collections import OrderedDict
import pytest


@pytest.fixture
def filter_data_by_lease_years():
    return [
        OrderedDict(
            [
                ("Property Name", "Seacroft Gate (Chase) - Block 2"),
                ("Property Address [1]", "Telecomms Apparatus"),
                ("Property  Address [2]", "Leeds"),
                ("Property Address [3]", ""),
                ("Property Address [4]", "LS14"),
                ("Unit Name", "Seacroft Gate (Chase) block 2-Telecom App."),
                ("Tenant Name", "Vodafone Ltd."),
                ("Lease Start Date", "30 Jan 2004"),
                ("Lease End Date", "29 Jan 2029"),
                ("Lease Years", "25"),
                ("Current Rent", "12250.00"),
            ]
        ),
        OrderedDict(
            [
                ("Property Name", "Queenswood Heights"),
                ("Property Address [1]", "Queenswood Heights"),
                ("Property  Address [2]", "Queenswood Gardens"),
                ("Property Address [3]", "Headingley"),
                ("Property Address [4]", "Leeds"),
                ("Unit Name", "Queenswood Hgt-Telecom App."),
                ("Tenant Name", "Vodafone Ltd"),
                ("Lease Start Date", "08 Nov 2004"),
                ("Lease End Date", "07 Nov 2029"),
                ("Lease Years", "25"),
                ("Current Rent", "9500.00"),
            ]
        ),
        OrderedDict(
            [
                ("Property Name", "Armley - Burnsall Grange"),
                ("Property Address [1]", "Armley"),
                ("Property  Address [2]", "LS13"),
                ("Property Address [3]", ""),
                ("Property Address [4]", ""),
                ("Unit Name", "Burnsall Grange CSR 37865"),
                ("Tenant Name", "O2 (UK) Ltd"),
                ("Lease Start Date", "26 Jul 2007"),
                ("Lease End Date", "25 Jul 2032"),
                ("Lease Years", "25"),
                ("Current Rent", "12000.00"),
            ]
        ),
        OrderedDict(
            [
                ("Property Name", "Seacroft Gate (Chase) - Block 2"),
                ("Property Address [1]", "Telecomms Apparatus"),
                ("Property  Address [2]", "Leeds"),
                ("Property Address [3]", ""),
                ("Property Address [4]", "LS14"),
                ("Unit Name", "Seacroft Gate (Chase) - Block 2, WYK 0414"),
                (
                    "Tenant Name",
                    "Hutchinson3G Uk Ltd&Everything Everywhere Ltd",
                ),
                ("Lease Start Date", "21 Aug 2007"),
                ("Lease End Date", "20 Aug 2032"),
                ("Lease Years", "25"),
                ("Current Rent", "12750.00"),
            ]
        ),
    ]


@pytest.fixture
def total_rent():
    return 46500.0


def test_filter_by_lease_years(
    rentals_data, filter_data_by_lease_years, total_rent
):
    assert filter_by_lease_years(rentals_data)[0] == filter_data_by_lease_years

    assert filter_by_lease_years(rentals_data)[1] == total_rent
