import pandas as pd

class FloodEvent:
    """
    The FloodEvent class represents a flood event and stores relevant data.
    
    Attributes:
        postcode (str): The postcode associated with the flood event.
        data (pd.DataFrame): DataFrame containing flood data.
        amount_covered (float): The proportion of land covered by the flood event (default is 1).
    """

    def __init__(self, postcode: str, data: pd.DataFrame, amount_covered: float = 1):
        """
        Initializes a FloodEvent object with the given postcode, data, and amount covered.

        Args:
            postcode (str): The postcode associated with the flood event.
            data (pd.DataFrame): DataFrame containing flood data.
            amount_covered (float): The proportion of land covered by the flood event (default is 1).

        Raises:
            ValueError: If the amount_covered is not between 0 and 1 (inclusive).
        """
        self.postcode = postcode
        self.data = data

        # Validate amount_covered
        if not 0 <= amount_covered <= 1:
            raise ValueError(
                "The amount covered must be between 0 and 1, inclusive. It was: "
                + str(amount_covered)
            )

        self.amount_covered = amount_covered

    def get_non_inundated_count(self) -> int:
        """
        Calculates the count of non-inundated areas based on the flood data.

        Returns:
            int: The count of non-inundated areas.
        """
        total_flooded_count = self.data["Depth (m)"].count()
        total_count = int(total_flooded_count / self.amount_covered)
        return total_count - total_flooded_count
