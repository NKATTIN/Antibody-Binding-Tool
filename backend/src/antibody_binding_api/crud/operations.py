from ..utils.antibody_analysis import read_data, generate_histogram, calculate_statistics, save_statistics

def process_file(file_location: str):
    data = read_data(file_location)
    histogram_path = "temp/histogram.png"
    generate_histogram(data, histogram_path)
    stats = calculate_statistics(data)
    stats_path = "temp/stats.csv"
    save_statistics(stats, stats_path)
    return histogram_path, stats_path
