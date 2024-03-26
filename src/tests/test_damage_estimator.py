import pytest
import pandas as pd
import numpy as np
from damage_estimator import DamageEstimator
from calc_risk import Risk
from flood_event import FloodEvent
from . import test_vulnerability_curve_data, test_flood_depths_data

@pytest.fixture
def risk():
    # Create a Risk object for testing
    return Risk(test_vulnerability_curve_data)

@pytest.fixture
def flood_event():
    # Create a FloodEvent object for testing
    return FloodEvent("PR1 8HU", test_flood_depths_data, 0.75)

def test_damage_estimator_initialization(risk, flood_event):
    # Test initialization of DamageEstimator object
    damage_estimator = DamageEstimator(risk, flood_event)
    assert damage_estimator.risk == risk
    assert damage_estimator.flood_event == flood_event
    assert damage_estimator.damage_value == 0
    assert damage_estimator.damage_set == False

def test_calculate_damage(risk, flood_event):
    # Test calculate_damage method of DamageEstimator
    damage_estimator = DamageEstimator(risk, flood_event)
    expected_damage = 150.0  # Expected damage value
    assert damage_estimator.calculate_damage() == expected_damage

def test_string_representation(risk, flood_event):
    # Test string representation of DamageEstimator object
    damage_estimator = DamageEstimator(risk, flood_event)
    expected_string = "PostCode: PR1 8HU, Damage: £150.0"  # Expected string representation
    assert str(damage_estimator) == expected_string
