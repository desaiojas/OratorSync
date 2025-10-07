import sounddevice as sd
import numpy as np
import librosa
import joblib
import cv2

# Load model
model = joblib.load('rf_stutter_model.pkl')

# Create a persistent window
cv2.namedWindow("Speech Classifier")

while True:
    # Record small chunk
    audio = sd.rec(int(1.5 * 16000), samplerate=16000, channels=1, dtype='float32')
    sd.wait()
    audio = audio.flatten()

    # Extract features
    mfcc = librosa.feature.mfcc(y=audio, sr=16000, n_mfcc=13)
    features = np.mean(mfcc.T, axis=0).reshape(1, -1)

    # Predict
    pred = model.predict(features)[0]

    # Show one window, update color
    color = (0, 0, 255) if pred else (0, 255, 0)
    label = "STUTTERED" if pred else "FLUENT"

    screen = np.zeros((500, 800, 3), dtype=np.uint8)
    screen[:] = color
    cv2.putText(screen, label, (220, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)

    cv2.imshow("Speech Classifier", screen)

    # Wait briefly for key press (q to quit)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

