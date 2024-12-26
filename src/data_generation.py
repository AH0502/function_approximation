import pandas as pd
import numpy as np

def generate_sin_data(num_samples=10000, output_file="data/sin_data.csv"):
    """
    Generates a dataset for sin(x) and saves it to a CSV file.

    Args:
        num_samples (int): Number of data points to generate.
        output_file (string): Path to the output file.
    """
    x = np.random.uniform(low=-np.pi, high=(2*np.pi, num_samples))
    y = np.sin(x)

    data = pd.DataFrame({'x': x, 'y': y})
    data.to_csv(output_file, index=False)



    