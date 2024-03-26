---
# Flood Risk Calculator

The Flood Risk Calculator is a tool designed to estimate the expected damage caused by floods based on flood depths, vulnerability curves, and other factors.

## Installation and env setup

To install the Flood Risk Calculator, follow these steps on bash or terminal:

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/arunmak10/flood_risk
    ```

2. Navigate to the project directory:

    ```
    cd flood_risk
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```
4. Set the $PYTHONPATH
    ```
    export PYTHONPATH="./flood_risk/src/:$PYTHONPATH"
    ```

## Usage

To use the Flood Risk Calculator, follow these steps:

1. Ensure you have Python installed on your machine.

2. Run the `main.py` script:

    ```
    python main.py
    ```

3. Follow the on-screen prompts to enter the postcode, percentage of inundated area.

4. The program will calculate the expected damage and display the result.

**Note:** If no input is provided, default values will be used for postcode and inundated area percentage.

### Testing and HTML Coverage Report:

For testing and generating an HTML coverage report, additional steps can be followed. The provided script automates these steps:

1. **Testing:** The script runs tests using the `pytest` framework along with coverage analysis. It ensures the correctness of the application's functionality.

2. **HTML Coverage Report:** After running the tests, two HTML coverage reports are generated and opened in default browser, providing insights into the test coverage and code quality.

**Note:** Ensure that all dependencies are installed before running the script.



## Configuration

The Flood Risk Calculator allows for configuration through environment variables or configuration files. Below are the available configuration options:

- `LOG_LEVEL`: Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR). Default is INFO.

- `DEFAULT_POSTCODE`: Set the default postcode to use if none is provided by the user. Default is "PR1 8HU".

- `INUNDATED_AREA_DEFAULT`: Set the default percentage of inundated area if none is provided by the user. Default is 75.


## Acknowledgements

The Flood Risk Calculator project is built using Python and various libraries. The data used is dummy data set.


## Note

Please note that other advanced features such as Apache Spark(PySpark) were not utilised in this project. 
This decision was made to keep the scope of the assessment manageable and to maintain simplicity for the purpose of showcasing the work done. Additionally, integrating Apache Spark could increase the complexity of project maintenance and potentially introduce environment compatibility issues for evaluators.

Instead, the multiprocessing `Pool` module was used to parallelize the processing of data chunks of default size 10k, resulting in improved performance. When using a large file containing 100,000 rows, the time difference in processing was reduced by approximately 7 seconds compared to the original sequential processing, resulting in an improvement of around 35%.

