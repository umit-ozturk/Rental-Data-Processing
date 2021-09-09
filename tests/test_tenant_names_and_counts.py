from utils import get_tenant_names_and_counts
import pytest


@pytest.fixture
def tenant_names_and_counts():
    return [
        {"Tenant Name": "Arqiva Services ltd", "Count": 1},
        {"Tenant Name": "Arqiva Ltd", "Count": 1},
        {"Tenant Name": "Vodafone Ltd.", "Count": 1},
        {"Tenant Name": "Vodafone Ltd", "Count": 1},
        {"Tenant Name": "O2 (UK) Ltd", "Count": 1},
        {
            "Tenant Name": "Hutchinson3G Uk Ltd&Everything Everywhere Ltd",
            "Count": 1,
        },
        {"Tenant Name": "Everything Everywhere Ltd", "Count": 4},
        {
            "Tenant Name": "Everything Everywhere Ltd & Hutchinson 3G UK",
            "Count": 3,
        },
        {
            "Tenant Name": "EverythingEverywhere Ltd & Hutchinson3GUK Ltd",
            "Count": 1,
        },
        {
            "Tenant Name": "Everything Everywhere Ltd&Hutchison 3G UK Ltd",
            "Count": 6,
        },
        {
            "Tenant Name": "Everything Everywhere Ltd&Hutchison 3G UK LTd",
            "Count": 1,
        },
        {
            "Tenant Name": "Everything Everywhere Ltd&Hutchsion 3G UK Ltd",
            "Count": 1,
        },
        {
            "Tenant Name": "Everything Everywhere Ltd&Hutchsion 3G Ltd",
            "Count": 1,
        },
        {
            "Tenant Name": "Everything Everywhere Ltd & Hutchison 3G Ltd",
            "Count": 1,
        },
        {
            "Tenant Name": "Cornerstone Telecommunications Infrastructure",
            "Count": 16,
        },
    ]


def test_tenant_names_and_counts(rentals_data, tenant_names_and_counts):
    assert get_tenant_names_and_counts(rentals_data) == tenant_names_and_counts
