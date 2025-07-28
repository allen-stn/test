import os
import pandas as pd
import subprocess

parquet_path = "path-to.parquet"
output_dir = "path-to./wav"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_parquet(parquet_path)

for _, row in df.iterrows():
    speaker_id = row['speaker_id']
    file_id = row['file_name']
    video_bytes = row['video']  # actual video file (mp4/webm/etc.)

    speaker_folder = os.path.join(output_dir, speaker_id)
    os.makedirs(speaker_folder, exist_ok=True)

    mp4_path = os.path.join(speaker_folder, f"{file_id}.mp4")
    wav_path = os.path.join(speaker_folder, f"{file_id}.wav")

    # Save video
    with open(mp4_path, "wb") as f:
        f.write(video_bytes)

    # Convert to wav
    subprocess.run([
        "ffmpeg", "-y", "-i", mp4_path, "-ar", "16000", "-ac", "1", wav_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Remove video after conversion
    os.remove(mp4_path)

    print(f"✅ Converted {file_id} from {speaker_id}")
