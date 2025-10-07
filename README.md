# stutter_detector
This project provides tools for simulating, detecting, and classifying stuttering in speech audio. It includes scripts for generating stuttered audio, training machine learning models, real-time stutter detection, and dataset management, supporting research in speech analysis.


# Stutter Detection and Audio Processing Toolkit

## Overview

This project provides tools and models for detecting stuttering in speech audio files. It includes scripts for training machine learning models, real-time stutter detection, and utilities for processing and converting audio datasets. The toolkit is designed for researchers, developers, and practitioners working on speech fluency analysis and stutter detection.

## Features

- Real-time stutter detection from audio input
- Pre-trained Random Forest stutter detection model
- Audio dataset management and conversion utilities
- Jupyter notebooks for model training and experimentation

## Installation

1. **Clone the repository:**
   ```zsh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```zsh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required dependencies:**
   ```zsh
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is not present, install dependencies as needed, e.g., `numpy`, `scikit-learn`, `librosa`, `soundfile`, etc.)*

## Usage

### 1. Real-Time Stutter Detection

Run the real-time stutter detector:
```zsh
python realtime_stutter_detector.py
```

### 2. Model Training

Open and run the Jupyter notebook for training:
```zsh
jupyter notebook model_train.ipynb
```

### 3. Data Processing

Use the provided scripts to process and flatten audio datasets:
```zsh
python flatten_inplace.py
```

### 4. Converting Fluent to Stuttered Audio

Refer to the `fluent_to_stutter.ipynb` notebook for data augmentation or conversion steps.

### 5. Under Construction
The Website is under construction. So recommended option to use this project is via opening file by : python realtime_stutter_detector.py

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Open a pull request describing your changes.

Please ensure your code follows best practices and includes appropriate documentation and tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
