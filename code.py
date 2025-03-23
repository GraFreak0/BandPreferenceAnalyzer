import os
from collections import defaultdict, Counter

def parse_input(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file not found: {file_path}")
    
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    try:
        num_lines = int(lines[0].strip())
    except ValueError:
        raise ValueError(f"Invalid number of lines in the input file: {lines[0].strip()}")
    
    band_preferences = defaultdict(list)
    
    for line in lines[1:num_lines + 1]:
        line = line.strip()
        if not line or ":" not in line:
            continue
        
        name, bands = line.split(": ", 1)
        band_list = bands.split(", ")
        
        for band in band_list:
            band_preferences[band].append(name)
    
    return band_preferences

def find_top_liked_bands(band_preferences):
    band_count = Counter({band: len(fans) for band, fans in band_preferences.items()})
    
    max_counts = sorted(band_count.values(), reverse=True)[:2]  # Top 2 most frequent counts
    top_bands = [band for band, count in band_count.items() if count in max_counts]
    
    return top_bands

def display_band_fans(band_preferences):
    for band in sorted(band_preferences.keys()):  # Sorting for consistent output
        print(f"{band}: {', '.join(sorted(band_preferences[band]))}")

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "inputs.txt")
    band_preferences = parse_input(file_path)
    
    # Problem 1: Find and display the top liked bands
    top_bands = find_top_liked_bands(band_preferences)
    for band in top_bands:
        print(band)
    
    print() 
    
    # Problem 2: Display bands and their fans
    display_band_fans(band_preferences)