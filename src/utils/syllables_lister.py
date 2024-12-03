import pandas as pd
import re
from collections import Counter

def count_syllables(dataFrame: pd.DataFrame) -> pd.DataFrame:    
    # Ensure all values in the 'head' column are strings
    dataFrame['head'] = dataFrame['head'].astype(str)
    
    # Extract syllables from each row
    syllable_counts = Counter()
    for syllable_string in dataFrame['head']:
        if syllable_string:  # Ensure the string is not empty
            # Use regex to match syllables (English letters followed by digits)
            syllables = re.findall(r'[a-zA-Z]+[0-9]', syllable_string)
            syllable_counts.update(syllables)
    
    # Convert the Counter to a DataFrame
    syllable_data = pd.DataFrame(syllable_counts.items(), columns=['syllable', 'instances'])

    # Sort by instances in descending order
    syllable_data = syllable_data.sort_values(by='instances', ascending=False).reset_index(drop=True)

    # Add IDs starting from 1 after sorting
    syllable_data['id'] = range(1, len(syllable_data) + 1)

    # Reorder the columns
    syllable_data = syllable_data[['id', 'syllable', 'instances']]

    return syllable_data