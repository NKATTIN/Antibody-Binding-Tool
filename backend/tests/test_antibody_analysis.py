import pandas as pd
from src.antibody_binding_api.utils.antibody_analysis import calculate_statistics

def test_calculate_statistics():
    data = pd.DataFrame({
        'index': [1, 2, 3],
        'optical_density': [0.5, 0.8, 0.9],
        'amino_acid_sequence': ['AA', 'AA', 'BB']
    })
    stats = calculate_statistics(data)
    print(stats)
    expected = pd.DataFrame({
        'amino_acid_sequence': ['AA', 'BB'],
        'min': [0.5, 0.9],
        'max': [0.8, 0.9],
        'mean': [0.6, 0.9]
    })
    pd.testing.assert_frame_equal(stats, expected, check_dtype=False)