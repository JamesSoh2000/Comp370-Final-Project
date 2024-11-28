import pandas as pd
import matplotlib.pyplot as plt

# Load the TSV file with the data
file_path = 'reviews_tdidf_BTS.tsv'  # Update the file path if needed
data = pd.read_csv(file_path, sep='\t')

# Create a bar chart
plt.figure(figsize=(10, 5))
plt.bar(data['Word'], data['TF-IDF Score'], color='lightblue')

# Customize the chart
plt.title("Behind The Scenes")
plt.xlabel("Words")
plt.ylabel("TF-IDF Score")
plt.xticks(rotation=45, ha='right')

# Save the chart as a PNG file
output_image_path = 'movie_BTS_tfidf_chart.png'  # File name
plt.tight_layout()
plt.savefig(output_image_path)

# Confirmation message
print(f"Chart saved as {output_image_path}")


