import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Disable scientific notation
np.set_printoptions(suppress=True)

# Load model
model = load_model("keras_Model.h5", compile=False)

# Load labels
with open("labels.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# Open webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Read frame
    ret, frame = camera.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Resize for model input
    image = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)

    # Prepare image for prediction
    input_image = np.asarray(image, dtype=np.float32)
    input_image = (input_image / 127.5) - 1
    input_image = np.expand_dims(input_image, axis=0)

    # Predict
    prediction = model.predict(input_image, verbose=0)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = float(prediction[0][index])

    # Display prediction
    text = f"{class_name} ({confidence_score * 100:.2f}%)"

    cv2.putText(
        frame,
        text,
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
    )

    cv2.imshow("Webcam Classification", frame)

    # Print to terminal
    print(f"Class: {class_name}")
    print(f"Confidence Score: {confidence_score * 100:.2f}%")

    # Press ESC to quit
    key = cv2.waitKey(1)
    if key == 27:
        break

# Cleanup
camera.release()
cv2.destroyAllWindows()
