import numpy as np
from calc_risk import Risk
from flood_event import FloodEvent

class DamageEstimator:
    """
    The DamageEstimator class calculates the damage of a flood event based on risk and flood event data.

    Attributes:
        risk (Risk): Risk object containing vulnerability curve data.
        flood_event (FloodEvent): FloodEvent object containing flood event data.
        damage_value (float): The calculated damage value.
        damage_set (bool): Indicates whether the damage value has been calculated.
    """

    def __init__(self, risk: Risk, flood_event: FloodEvent):
        """
        Initializes a DamageEstimator object with risk and flood event data.

        Args:
            risk (Risk): Risk object containing vulnerability curve data.
            flood_event (FloodEvent): FloodEvent object containing flood event data.
        """
        self.risk = risk
        self.flood_event = flood_event
        self.damage_value = 0
        self.damage_set = False

    def calculate_damage(self) -> float:
        """
        Calculates the damage of the flood event based on risk and flood event data.

        Returns:
            float: The calculated damage value.
        """
        # If damage value has already been calculated, return it
        if self.damage_set:
            return self.damage_value

        depth = self.flood_event.data["Depth (m)"]

        # Calculating the sum of each depth risk
        flooded_damage_sum = np.sum(depth.apply(self.risk.calculate_damage))
        non_inundated_count = self.flood_event.get_non_inundated_count()

        # Calculate the average damage
        total_count = len(depth) + non_inundated_count
        self.damage_value = flooded_damage_sum / total_count

        self.damage_set = True
        return self.damage_value

    def __str__(self) -> str:
        """
        Returns a string representation of the DamageEstimator object.

        Returns:
            str: A string representation of the object.
        """
        damage = self.damage_value
        if not self.damage_set:
            damage = self.calculate_damage()

        return f"PostCode: {self.flood_event.postcode}, Damage: £{damage}"
