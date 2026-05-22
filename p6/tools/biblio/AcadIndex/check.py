import pandas as pd
import os

FULL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "machine_learning_techniques_and_medical_images_output")
DATE_PATH = os.path.join(FULL_PATH, "2024-06-12-16-32-18")
PAPERS = os.path.join(DATE_PATH, "scraped_papers.xlsx") 
TITLES = os.path.join(DATE_PATH, "titles.txt")

def read_titles_from_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        titles = [line.strip().lower() for line in file]
    return titles

# Read titles from text file
file_titles = read_titles_from_file(TITLES)

# Example DataFrame
data = {'title': ['Title 1', 'Title 2', 'Title 3']}
df = pd.read_excel(PAPERS)

# Extract titles from DataFrame into a set
df_titles = set(df['Title'])

df_titles = {title.lower() for title in df_titles}

# Find titles in the text file that are not in the DataFrame
missing_titles = [title for title in file_titles if title not in df_titles]


print(len(missing_titles))
# Output the results
if missing_titles:
    print("Titles in the text file not present in the DataFrame:")
    for title in missing_titles:
        print(title)
else:
    print("All titles from the text file are present in the DataFrame.")