import pandas as pd

class Risk:
    """
    The Risk class represents the risk associated with flood events.

    Attributes:
        vulnerability_curve (pd.DataFrame): DataFrame representing the vulnerability curve.
    """

    def __init__(self, vulnerability_curve: pd.DataFrame):
        """
        Initializes a Risk object with the given vulnerability curve.

        Args:
            vulnerability_curve (pd.DataFrame): DataFrame representing the vulnerability curve.

        Raises:
            ValueError: If the vulnerability_curve DataFrame is not in the expected format.
        """
        # Validate vulnerability_curve DataFrame
        if not isinstance(vulnerability_curve, pd.DataFrame) or \
           "DepthLowerBound (m)" not in vulnerability_curve.columns or \
           "DepthUpperBound (m)" not in vulnerability_curve.columns or \
           "Damage (GBP)" not in vulnerability_curve.columns:
            raise ValueError("vulnerability_curve DataFrame must contain columns: 'DepthLowerBound (m)', 'DepthUpperBound (m)', and 'Damage (GBP)'")

        # Make a copy to avoid modifying the original DataFrame
        self.vulnerability_curve = vulnerability_curve.copy()

        # Use interval index for faster calculations
        self.vulnerability_curve["depth_interval"] = pd.IntervalIndex.from_arrays(
            vulnerability_curve["DepthLowerBound (m)"],
            vulnerability_curve["DepthUpperBound (m)"],
            closed="right",
        )

        # Set index to the depth interval
        self.vulnerability_curve.set_index("depth_interval", inplace=True)

    def calculate_damage(self, depth: float) -> float:
        """
        Calculates the damage associated with a given depth of flooding.

        Args:
            depth (float): The depth of flooding.

        Returns:
            float: The calculated damage in GBP.

        Raises:
            ValueError: If the depth is out of bounds.
        """
        # If depth is 0, return 0 damage
        if depth == 0:
            return 0

        try:
            interval_index = self.vulnerability_curve.index.get_loc(depth)
            return self.vulnerability_curve.iloc[interval_index]["Damage (GBP)"]
        except KeyError:
            raise ValueError("Depth out of bounds")
