import pandas as pd
import unicodedata

def accentless_numerical_syntax(dataFrame: pd.DataFrame) -> pd.DataFrame:
    def append_numeric_to_syllable(word_string):
        if not isinstance(word_string, str):
            return word_string
        
        vowels = 'aeiouáéíóú'
        accented_vowels = 'áéíóú'
        normalize_word = unicodedata.normalize('NFC', word_string)
        syllables = []
        syllable_count = 0

        # Extract all syllables before the last syllables
        last_vowel_pos = -1
        current_vowel_pos = -1
        special = False
        for pointer in range(len(normalize_word) - 1, -1, -1):
            if (normalize_word[pointer] in vowels or normalize_word[pointer] in accented_vowels):
                current_vowel_pos = pointer

                # Mark the last instance of a vowel.
                if last_vowel_pos == -1:
                    last_vowel_pos = pointer

                # Decide the syllable form (CVC or CV) based on closedness or openness.
                if current_vowel_pos > 1 and normalize_word[current_vowel_pos - 1] in vowels:
                    # Finds a possible VC or V syllable from here. Usually at the end.
                    special = True
                    syllables.insert(syllable_count, normalize_word[current_vowel_pos - 2: current_vowel_pos])
                    syllable_count += 1
                elif current_vowel_pos > 3 and normalize_word[current_vowel_pos - 1] not in vowels and normalize_word[current_vowel_pos - 2] not in vowels:
                    # Finds a CVC syllable form here.
                    syllables.insert(syllable_count, normalize_word[current_vowel_pos - 4: current_vowel_pos - 1])
                    syllable_count += 1
                elif current_vowel_pos > 2 and normalize_word[current_vowel_pos - 1] not in vowels:
                    # Finds a CV syllable form here.
                    syllables.insert(syllable_count, normalize_word[current_vowel_pos - 3: current_vowel_pos - 1])
                    syllable_count += 1

        # Extract last syllable
        if special:
            # Ensure no out of range errors when slicing
            if last_vowel_pos + 2 <= len(normalize_word):
                syllables.insert(0, normalize_word[last_vowel_pos: last_vowel_pos + 2])
            else:
                syllables.insert(0, normalize_word[last_vowel_pos:])
        else:
            # Ensure no out of range errors when slicing
            if last_vowel_pos + 2 <= len(normalize_word):
                syllables.insert(0, normalize_word[last_vowel_pos - 1: last_vowel_pos + 2])
            else:
                syllables.insert(0, normalize_word[last_vowel_pos - 1:])
            syllable_count += 1

        # Analyze each syllables
        syllables.reverse()
        processed_syllables = []
        for syllable in syllables:
            if isinstance(syllable, str) and syllable:  # fuck Python
                if syllable[0] in vowels:
                    syllable = ''.join(('q', syllable))

            if any(char in accented_vowels for char in syllable):
                if syllable == syllables[len(syllables) - 1]:
                    syllable = syllable + "1"
                elif syllable == syllables[len(syllables) - 2]:
                    syllable = syllable + "2"
            else:
                syllable = syllable + "0"
            processed_syllables.append(syllable)

        return ''.join(processed_syllables)

    # Create a new DataFrame with the modified words
    original_and_modified = pd.DataFrame({
        'head': dataFrame['head'],
        'modified_head': dataFrame['head'].apply(append_numeric_to_syllable)
    })

    # Save the modified data to CSV
    original_and_modified.to_csv('data/isolated/ceb_roots_accentless_numerical_syntax.csv', index=False)

    # Apply the modification to the original DataFrame
    dataFrame['head'] = dataFrame['head'].apply(append_numeric_to_syllable)
    print("Successfully added numerical syntax 0 to accentless syllables!")
    return dataFrame