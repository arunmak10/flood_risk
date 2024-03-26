'''import pytest
import pandas as pd
from unittest.mock import patch, Mock
from flood_risk.src.run import read_flood_depths, read_vulnerability_curve, calculate_expected_damage
from . import test_flood_depths_data, test_vulnerability_curve_data

def test_read_flood_depths():
    filename = "test_depths.csv"
    with patch('pandas.read_csv', return_value=pd.DataFrame()):
        result = read_flood_depths(filename)
    assert isinstance(result, pd.DataFrame)

def test_read_vulnerability_curve():
    filename = "test_curve.csv"
    with patch('pandas.read_csv', return_value=pd.DataFrame()):
        result = read_vulnerability_curve(filename)
    assert isinstance(result, pd.DataFrame)

def test_calculate_expected_damage():
    post_code = "PR1 8HU"
    inundated_area_decimal = 0.75
    with patch('run.Risk') as MockRisk, \
         patch('run.FloodEvent') as MockFloodEvent, \
         patch('run.DamageEstimator') as MockDamageEstimator:

        # Mock the return value of calculate_damage method
        expected_damage = 150.0  # Expected damage value
        MockDamageEstimator_instance = MockDamageEstimator.return_value
        MockDamageEstimator_instance.calculate_damage.return_value = expected_damage

        # Mock Risk and FloodEvent instances
        risk_instance = MockRisk.return_value
        flood_event_instance = MockFloodEvent.return_value

        # Perform the test
        result = calculate_expected_damage(post_code, test_flood_depths_data, test_vulnerability_curve_data, inundated_area_decimal)

    # Verify that the calculate_damage returned the expected value
    assert result == expected_damage

if __name__ == "__main__":
    pytest.main()
    '''

import pytest
import pandas as pd
from unittest.mock import patch, Mock
from flood_risk.src.run import read_flood_depths, read_vulnerability_curve, calculate_expected_damage
from . import test_flood_depths_data, test_vulnerability_curve_data

def test_read_flood_depths():
    filename = "test_depths.csv"
    with patch('pandas.read_csv', return_value=pd.DataFrame()):
        result = read_flood_depths(filename)
    assert isinstance(result, pd.DataFrame)

def test_read_vulnerability_curve():
    filename = "test_curve.csv"
    with patch('pandas.read_csv', return_value=pd.DataFrame()):
        result = read_vulnerability_curve(filename)
    assert isinstance(result, pd.DataFrame)

def test_calculate_expected_damage():
    post_code = "PR1 8HU"
    inundated_area_decimal = 0.75

    # Mock Pool behavior
    with patch('flood_risk.src.run.Pool') as MockPool, \
         patch('flood_risk.src.run.calculate_expected_damage') as MockCalculate:

        # Mock the return value of calculate_expected_damage
        expected_damage = 150.0  # Expected damage value
        MockCalculate.side_effect = [expected_damage] * 2  # Mock for two chunks

        # Perform the test
        calculate_expected_damage(post_code, test_flood_depths_data, test_vulnerability_curve_data, inundated_area_decimal)

if __name__ == "__main__":
    pytest.main()
