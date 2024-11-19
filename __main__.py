import os, sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from sanitizers.non_singular_word import sanitize_compound_words
from sanitizers.syllables import substring_replace
from sanitizers.vowel_acute_marker import acute_markers
from sanitizers.numerical_syntax import accentless_numerical_syntax
from sanitizers.accent_marker_sanitizer import sanitize_all_markers

def main():
    dictionary_data = pd.read_csv("data/raw/ceb_roots.csv")
    filtered_data = sanitize_compound_words(dictionary_data)
    filtered_data = substring_replace(filtered_data, "head", 'ng', 'ŋ')
    filtered_data = substring_replace(filtered_data, "head", '-', 'q')

    filtered_data = substring_replace(filtered_data, "head", 'à', 'aq')
    filtered_data = substring_replace(filtered_data, "head", 'è', 'eq')
    filtered_data = substring_replace(filtered_data, "head", 'ì', 'iq')
    filtered_data = substring_replace(filtered_data, "head", 'ò', 'oq')
    filtered_data = substring_replace(filtered_data, "head", 'ù', 'uq')

    filtered_data = substring_replace(filtered_data, "head", 'â', 'áq')
    filtered_data = substring_replace(filtered_data, "head", 'ê', 'éq')
    filtered_data = substring_replace(filtered_data, "head", 'î', 'íq')
    filtered_data = substring_replace(filtered_data, "head", 'ô', 'óq')
    filtered_data = substring_replace(filtered_data, "head", 'û', 'úq')

    filtered_data = acute_markers(filtered_data)
    filtered_data = accentless_numerical_syntax(filtered_data)
    filtered_data = sanitize_all_markers(filtered_data)

    filtered_data.to_csv("data/exports/ceb_roots_filtered.csv", index=False)
    
    print("\nFiltered data saved to 'data/raw/ceb_roots_filtered.csv'")


if __name__ == "__main__":
    main()