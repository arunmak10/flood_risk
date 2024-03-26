# common_package/__init__.py

import pandas as pd

test_flood_depths_data = pd.DataFrame({'Depth (m)': [1, 2, 3]})

test_vulnerability_curve_dict = {
    "DepthLowerBound (m)": [0, 1, 2, 3],
    "DepthUpperBound (m)": [1, 2, 3, 4],
    "Damage (GBP)": [100, 200, 300, 400]
}
test_vulnerability_curve_data = pd.DataFrame(test_vulnerability_curve_dict)
