import os
import shutil

def flatten_inplace(folder, label, extensions=[".wav", ".flac"]):
    files_to_copy = []

    for root, _, files in os.walk(folder):
        for f in files:
            if any(f.endswith(ext) for ext in extensions):
                src = os.path.join(root, f)
                if root != folder:
                    files_to_copy.append(src)

    print(f"Found {len(files_to_copy)} files to flatten in {folder}")

    count = 1
    for src in files_to_copy:
        ext = os.path.splitext(src)[1]
        dest = os.path.join(folder, f"{label}_{count}{ext}")
        shutil.copy2(src, dest)
        count += 1

    print(f"✅ Flattened: {count - 1} files copied directly to {folder}")

# -------------------------------
# Use both extensions
flatten_inplace("./data/fluent", "fluent")
flatten_inplace("./data/stuttered", "stuttered")


