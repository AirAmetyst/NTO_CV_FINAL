import os
import hashlib
from collections import defaultdict

def aggregate_names(names):
    return set(names)

def choose_name(names):
    # name_lengths = [len(name) for name in names]
    filtered_names = [name for name in names if '№' not in name]
    if filtered_names:
        return max(filtered_names, key=len)
    else:
        return max(names, key=len)
        
def replace_forbidden_chars(text):
    forbidden_chars = ['/', '\\', '?', '%', '*', ':', '|', '"', '<', '>', '.']
    for char in forbidden_chars:
        text = text.replace(char, '_')
    return text.rstrip()

def remove_duplicates(folder):
    file_hashes = defaultdict(list)
    
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        
        if os.path.isdir(filepath):
            continue
        
        with open(filepath, "rb") as f:
            file_hash = hashlib.md5(f.read()).hexdigest()
        
        file_hashes[file_hash].append(filepath)
    
    for files_list in file_hashes.values():
        if len(files_list) > 1:
            for file_to_remove in files_list[1:]:
                os.remove(file_to_remove)