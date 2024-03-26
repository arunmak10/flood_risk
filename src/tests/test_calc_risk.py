import pytest
import pandas as pd
from flood_risk.src.calc_risk import Risk
from . import  test_vulnerability_curve_data

def test_calculate_damage_within_bounds():
    risk = Risk(test_vulnerability_curve_data)
    assert risk.calculate_damage(0.5) == 100
    assert risk.calculate_damage(2.5) == 300


def test_calculate_damage_boundary_values():
    risk = Risk(test_vulnerability_curve_data)
    assert risk.calculate_damage(1.1) == 200
    assert risk.calculate_damage(3.1) == 400


def test_calculate_damage_out_of_bounds():
    risk = Risk(test_vulnerability_curve_data)
    with pytest.raises(ValueError):
        risk.calculate_damage(5)


def test_calculate_damage_zero_depth():
    risk = Risk(test_vulnerability_curve_data)
    assert risk.calculate_damage(0) == 0


if __name__ == "__main__":
    pytest.main()
