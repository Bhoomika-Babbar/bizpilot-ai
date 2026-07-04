import pandas as pd
from pathlib import Path

DATASET_DIR = Path(__file__).parent.parent / "datasets"

def read_csv(filename):
    """
    Reads a CSV file from the datasets folder.

    Args:
        filename (str): Name of the CSV file.

    Returns:
        pandas.DataFrame
    """
    file_path = DATASET_DIR / filename
    return pd.read_csv(file_path)