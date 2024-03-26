import logging
import pandas as pd
import time
from damage_estimator import DamageEstimator
from flood_event import FloodEvent
from calc_risk import Risk
from multiprocessing import Pool


# Configure logging, change to desired level ERROR etc
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to read flood depths from CSV file
def read_flood_depths(filename):
    """
    Read flood depths from a CSV file.

    Args:
        filename (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing flood depths data.
    """
    try:
        logger.info("Reading flood depths from file: %s", filename)
        return pd.read_csv(filename, chunksize=10000)
    except FileNotFoundError as e:
        logger.error("File not found: %s", filename)
        raise

# Function to read vulnerability curve from CSV file
def read_vulnerability_curve(filename):
    """
    Read vulnerability curve from a CSV file.

    Args:
        filename (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing vulnerability curve data.
    """
    try:
        logger.info("Reading vulnerability curve from file: %s", filename)
        return pd.read_csv(filename)
    except FileNotFoundError as e:
        logger.error("File not found: %s", filename)
        raise

# Function to calculate expected damage
def calculate_expected_damage(post_code, flood_depths, vulnerability_curve, inundated_area_decimal):
    """
    Calculate the expected damage based on flood depths, vulnerability curve, and inundated area.

    Args:
        post_code (str): Postcode of the location.
        flood_depths (pd.DataFrame): DataFrame containing flood depths data.
        vulnerability_curve (pd.DataFrame): DataFrame containing vulnerability curve data.
        inundated_area_decimal (float): Decimal value representing the percentage of inundated area.

    Returns:
        float: Expected damage value.
    """
    logger.info("Calculating expected damage")

    # Log the shape of the vulnerability curve
    logger.info("Shape of vulnerability curve: %s", vulnerability_curve.shape)

    start_time = time.time()  # Record the start time

    risk = Risk(vulnerability_curve)
    flood_event = FloodEvent(post_code, flood_depths, inundated_area_decimal)

    # Perform calculations here
    damage_estimator = DamageEstimator(risk, flood_event)
    expected_damage = damage_estimator.calculate_damage()

    end_time = time.time()  # Record the end time
    time_taken = end_time - start_time

    # Log the time taken to calculate expected damage
    logger.info("Time taken to calculate expected damage: %.6f seconds", time_taken)

    return expected_damage

# Main function
def start():
    logger.info("Starting the program")

    default_postcode = "PR1 8HU"
    postcode = input("Enter the postcode: ")

    # Set default value for inundated_area_decimal
    inundated_area_decimal = 0.75

    inundated_area_input = input("Enter the '%' of inundated area (e.g., 75 or 80): ")

    try:
        # Convert input to float
        inundated_area_percentage = float(inundated_area_input)

        # Check if the input is within the valid range (0 to 100)
        if 0 <= inundated_area_percentage <= 100:
            # Convert percentage to decimal
            inundated_area_decimal = inundated_area_percentage / 100
            logger.info("Inundated area percentage:%s", inundated_area_percentage)
            logger.info("Inundated area decimal:%s", inundated_area_decimal)
        else:
            logger.info("Wrong Input using default value")

    except ValueError:
        logger.exception("Invalid input. Please enter a valid percentage.")
        logger.info("Wrong Input using default value in decimal : %s", inundated_area_decimal)

    logger.info("Postcode entered: %s", postcode)
    postcode = postcode if postcode else default_postcode

    flood_depths_chunks = read_flood_depths("./flood_risk/data/depths.csv")
    vulnerability_curve = read_vulnerability_curve("./flood_risk/data/vulnerability_curve.csv")

    # Process chunks in parallel
    start_time = time.time()  # Record the start time
    
    with Pool() as pool:
        results = pool.starmap(
            calculate_expected_damage,
            [(postcode, chunk, vulnerability_curve, inundated_area_decimal) for chunk in flood_depths_chunks]
        )
    expected_damage = sum(results)
    end_time = time.time()  # Record the end time
    time_taken = end_time - start_time

    # Log the time taken to calculate expected damage
    logger.info("Time taken to calculate expected damage with parallel proc: %.6f seconds", time_taken)

    # Show the overall result
    logger.info("Expected damage for postcode %s: %s", postcode, expected_damage)
    print("Expected damage for postcode", postcode, ":", expected_damage)

    logger.info("Program completed successfully")
    