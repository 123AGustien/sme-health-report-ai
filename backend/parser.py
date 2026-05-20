import pandas as pd
import io

def parse_file(file_bytes):
    """
    Converts uploaded Excel file into a pandas DataFrame
    """
    df = pd.read_excel(io.BytesIO(file_bytes))
    return df
