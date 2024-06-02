import pandas as pd
import matplotlib.pyplot as plt

def read_data(file_path):
    return pd.read_csv(file_path)

def generate_histogram(data, output_path):
    plt.figure()
    plt.hist(data['optical_density'], bins=30, edgecolor='black')
    plt.xlabel('Optical Density')
    plt.ylabel('Frequency')
    plt.title('Histogram of Optical Density')
    plt.savefig(output_path)
    plt.close()

def calculate_statistics(data):
    stats = data.groupby('amino_acid_sequence')['optical_density'].agg(['min', 'max', 'mean']).reset_index()
    stats['mean'] = stats['mean'].round(1)
    return stats

def save_statistics(stats, output_path):
    stats.to_csv(output_path, index=False)