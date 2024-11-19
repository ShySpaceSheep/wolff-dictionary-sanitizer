import pandas as pd

def sanitize_all_markers(dataFrame: pd.DataFrame) -> pd.DataFrame:
    accent_map = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'
    }
    
    # Iterate through each column of the DataFrame
    dataFrame['head'] = dataFrame['head'].replace(accent_map, regex=True)
    return dataFrame