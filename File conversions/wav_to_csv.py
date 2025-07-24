import numpy as np
from scipy.io import wavfile
import pandas as pd

# Load the .wav file
sample_rate, data = wavfile.read(r"path_to_.wav")

# If stereo, convert to mono
if len(data.shape) == 2:
    data = data.mean(axis=1)

# Convert to DataFrame and save
df = pd.DataFrame(data, columns=["Amplitude"])
df.to_csv(r"path_to_output.csv", index=False)

print("Conversion complete. Saved to output.csv")
