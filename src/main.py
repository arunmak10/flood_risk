import subprocess
import logging
from run import start

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_tests():
    try:
        # Run pytest with coverage
        subprocess.run(["pytest", "--cov=./flood_risk/src/", "--cov-report", "html", "--html=report.html"])
    except FileNotFoundError as e:
        logger.error(f"Error running tests: {e}")

def open_html_report():
    try:
        # Open the HTML coverage report
        subprocess.run(["open", "./htmlcov/index.html"])
        subprocess.run(["open", "report.html"])
    except FileNotFoundError as e:
        logger.error(f"Error opening HTML report: {e}")

if __name__ == "__main__":
    try:
        # Start the program
        start()
    except Exception as e:
        logger.error(f"Error starting the program: {e}")
    
    # Run tests
    run_tests()
    
    # Open HTML report
    open_html_report()
