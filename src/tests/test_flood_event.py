import pytest
import pandas as pd
from flood_event import FloodEvent
from . import test_vulnerability_curve_data, test_flood_depths_data

def test_flood_event_initialization():
    # Test initialization of FloodEvent object
    postcode = "PR1 8HU"
    #flood_event_data = pd.DataFrame({'Depth (m)': [0.5, 1.5, 2.5]})
    amount_covered = 0.75
    flood_event = FloodEvent(postcode, test_flood_depths_data, amount_covered)
    assert flood_event.postcode == postcode
    assert isinstance(flood_event.data, pd.DataFrame)
    assert flood_event.amount_covered == amount_covered

def test_flood_event_invalid_amount_covered():
    # Test initialization with invalid amount_covered
    with pytest.raises(ValueError):
        FloodEvent("PR1 8HU", pd.DataFrame(), -0.5)
    with pytest.raises(ValueError):
        FloodEvent("PR1 8HU", pd.DataFrame(), 1.5)

def test_flood_event_get_non_inundated_count():
    # Test get_non_inundated_count method
    postcode = "PR1 8HU"
    amount_covered = 0.75
    flood_event = FloodEvent(postcode, test_flood_depths_data, amount_covered)
    expected_count = 1  # Expected non-inundated count
    assert flood_event.get_non_inundated_count() == expected_count
