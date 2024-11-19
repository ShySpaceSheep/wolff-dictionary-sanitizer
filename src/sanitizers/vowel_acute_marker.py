import unicodedata
import pandas as pd

def acute_markers(dataFrame: pd.DataFrame) -> pd.DataFrame:
    modifiable_entries = 0
    ignored_entries = 0
    closed_syllables = 0
    open_syllables = 0

    print("Marking 'head' column with accute accent marks...")
    def modify_to_acute_vowel(word_string):
        nonlocal modifiable_entries, ignored_entries, closed_syllables, open_syllables

        if not isinstance(word_string, str):
            return word_string
        
        normalized_word = unicodedata.normalize('NFC', word_string)

        if any(char in 'áéíóúÁÉÍÓÚ' for char in normalized_word):
            ignored_entries += 1
            return word_string 

        modifiable_entries += 1
        last_vowel_pos = -1
        vowels = 'aeiouAEIOU'
        word_string = list(word_string)

        for i in range(len(word_string) - 1, -1, -1):
            if (word_string[i]) in vowels:
                last_vowel_pos = i
                break

        # Closed condition > open condition
        if last_vowel_pos > 1 and word_string[last_vowel_pos - 1] not in vowels and word_string[last_vowel_pos - 2] not in vowels:
            penultimate_vowel_pos = -1
            for i in range(last_vowel_pos - 1, -1, -1):
                if word_string[i] in vowels:
                    penultimate_vowel_pos = i
                    break
            
            if penultimate_vowel_pos != -1:
                closed_syllables += 1
                word_string[penultimate_vowel_pos] = word_string[penultimate_vowel_pos] + '́' 
        else:
            open_syllables += 1
            word_string[last_vowel_pos] = word_string[last_vowel_pos] + '́' 

        return ''.join(word_string)
    
    original_and_modified = pd.DataFrame({
        'head': dataFrame['head'],
        'modified_head': dataFrame['head'].apply(modify_to_acute_vowel)
    })

    original_and_modified.to_csv('data/isolated/ceb_roots_accute_markers.csv', index=False)

    dataFrame['head'] = dataFrame['head'].apply(modify_to_acute_vowel)
    print(f'Ignored {ignored_entries} entries which already have an acute accent marker...')
    print(f'Modified vowels of {closed_syllables} closed-condition syllables and {open_syllables} open-condition syllables across {modifiable_entries} modifiable entries.')

    return dataFrame