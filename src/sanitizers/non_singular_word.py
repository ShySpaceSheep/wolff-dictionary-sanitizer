import pandas as p

def sanitize_compound_words(dataFrame) -> p.DataFrame:
    print("Sanitizing compound words from the data frame...")
    compound_word_pattern = r'\S+\s\S+'

    compound_words_rows = dataFrame['head'].str.contains(compound_word_pattern, na=False)
    compound_words = dataFrame[compound_words_rows]

    sanitized_dataframe = dataFrame[~compound_words_rows]
    print(f'Removed {compound_words.shape[0]} instances of compound word entries...')

    return sanitized_dataframe