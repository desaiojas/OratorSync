import os
import random
from pydub import AudioSegment
from pydub.silence import split_on_silence

INPUT_FOLDER = "./data/fluent"
OUTPUT_FOLDER = "./data/stuttered_prolonged_block"

SILENCE_THRESH = -40
MIN_SILENCE_LEN = 150

# Stutter, Prolong, Block settings
STUTTER_PROB = 0.8      
PROLONG_PROB = 0.5      
BLOCK_PROB = 0.5        
MIN_CHUNKS = 2
MAX_CHUNKS = 4
PART_REPEAT = (2, 4)
PROLONG_FACTOR = (1.5, 3.0)

BLOCK_DURATION = (200, 800)  # regular block
BLOCK_PROLONG_DURATION = (1000, 3000)  # prolonged block

BLOCK_PROLONG_PROB = 0.3  # chance to choose long block instead of short
BLOCK_REPEAT = (1, 2)  # number of times to repeat block

PAUSE_BETWEEN = 30

def stutter_prolong_block(chunk):
    duration = len(chunk)
    n_parts = random.randint(MIN_CHUNKS, MAX_CHUNKS)
    part_len = duration // n_parts

    output = AudioSegment.silent(duration=0)

    for i in range(n_parts):
        start = i * part_len
        end = start + part_len if i < n_parts - 1 else duration
        piece = chunk[start:end]

        # Prolong
        if random.random() < PROLONG_PROB:
            stretch_factor = random.uniform(*PROLONG_FACTOR)
            piece = piece._spawn(piece.raw_data, overrides={
                "frame_rate": int(piece.frame_rate / stretch_factor)
            }).set_frame_rate(piece.frame_rate)

        repeats = random.randint(*PART_REPEAT)

        for _ in range(repeats):
            output += piece
            output += AudioSegment.silent(duration=PAUSE_BETWEEN)

        # Insert block inside word parts
        if random.random() < BLOCK_PROB:
            # choose prolonged block or normal
            if random.random() < BLOCK_PROLONG_PROB:
                block_len = random.randint(*BLOCK_PROLONG_DURATION)
            else:
                block_len = random.randint(*BLOCK_DURATION)

            block_repeats = random.randint(*BLOCK_REPEAT)
            for _ in range(block_repeats):
                output += AudioSegment.silent(duration=block_len)

    return output

def process_file(input_path, output_path):
    try:
        audio = AudioSegment.from_file(input_path)
        words = split_on_silence(
            audio,
            silence_thresh=SILENCE_THRESH,
            min_silence_len=MIN_SILENCE_LEN,
            keep_silence=50
        )

        result = AudioSegment.silent(duration=0)

        for word in words:
            # Block before the word
            if random.random() < BLOCK_PROB:
                if random.random() < BLOCK_PROLONG_PROB:
                    block_len = random.randint(*BLOCK_PROLONG_DURATION)
                else:
                    block_len = random.randint(*BLOCK_DURATION)

                block_repeats = random.randint(*BLOCK_REPEAT)
                for _ in range(block_repeats):
                    result += AudioSegment.silent(duration=block_len)

            if random.random() < STUTTER_PROB:
                processed = stutter_prolong_block(word)
                result += processed
            else:
                result += word

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        result.export(output_path, format="wav")

    except Exception as e:
        print(f"❌ Error processing {input_path}: {e}")

# Process all files
for root, _, files in os.walk(INPUT_FOLDER):
    for fname in files:
        if fname.lower().endswith((".wav", ".flac", ".mp3")):
            rel_dir = os.path.relpath(root, INPUT_FOLDER)
            output_dir = os.path.join(OUTPUT_FOLDER, rel_dir)
            input_file = os.path.join(root, fname)
            output_file = os.path.join(output_dir, f"stuttered_{fname}")

            print(f"🔄 {input_file} ➜ {output_file}")
            process_file(input_file, output_file)

print("\n✅ Done! Check:", OUTPUT_FOLDER)