import pandas as p

def substring_replace(dataFrame: p.DataFrame, column: str, sub_str1: str, sub_str2: str) -> p.DataFrame:
    modified_entries = []
    
    def replace_and_track(cell_value):
        if isinstance(cell_value, str):
            replaced_count = cell_value.count(sub_str1)
            if replaced_count > 0:
                modified_entries.append((cell_value, cell_value.replace(sub_str1, sub_str2), replaced_count))
            return cell_value.replace(sub_str1, sub_str2)
        return cell_value 
    
    dataFrame.loc[:, column] = dataFrame[column].apply(replace_and_track)
    total_replacements = sum(count for _, _, count in modified_entries)

    modified_df = p.DataFrame(modified_entries, columns=["Original", "Replaced", "Count"])
    modified_df.to_csv(f'data/isolated/ceb_roots_{sub_str1}_to_{sub_str2}.csv', index=False)
    print(f'Replaced {total_replacements} instances of substring [{sub_str1}] to [{sub_str2}]...')
    
    return dataFrame