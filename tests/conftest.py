import pytest

from jschon import create_catalog
from jschon_translation.catalog import initialize


@pytest.fixture(autouse=True)
def catalog():
    catalog = create_catalog('2020-12')
    initialize(catalog)
    return catalog
