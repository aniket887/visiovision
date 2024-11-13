import cv2
import pytesseract
from PIL import Image, ImageEnhance
import pyttsx3

# Path to Tesseract executable (change to your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to preprocess the image for better OCR results
def preprocess_image(image):
    # Convert the image to grayscale
    image = image.convert('L')

    # Apply some enhancement to improve text extraction
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  # Adjust contrast for better text visibility

    return image

# Function to extract text from the image and convert it to speech
def image_to_text_to_speech(image_path):
    # Load the image from the path
    image = Image.open(image_path)

    # Preprocess the image
    image = preprocess_image(image)

    # Extract text from the image using pytesseract
    text = pytesseract.image_to_string(image)

    # Print the extracted text
    print("Extracted Text:", text)

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties for the voice (optional)
    engine.setProperty('rate', 150)     # Speed of speech
    engine.setProperty('volume', 0.9)   # Volume level (0.0 to 1.0)

    # Speak the extracted text
    engine.say(text)
    engine.runAndWait()

# Initialize the camera
#cap = cv2.VideoCapture(1)  # Try index 0 or 1 if 0 doesn't work
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use DirectShow backend

# Check if the camera was opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame capture failed, skip this iteration
    if not ret:
        print("Error: Failed to grab frame.")
        continue

    # Display the resulting frame
    cv2.imshow('Press "p" to capture photo', frame)

    # Wait for the keypress event
    key = cv2.waitKey(1) & 0xFF

    # If 'p' key is pressed, capture the image and process it
    if key == ord('p'):
        # Convert the frame to a PIL image
        img_input = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Save the captured image
        img_path = 'captured_image.jpg'
        img_input.save(img_path)

        # Extract text from the captured image and speak it
        image_to_text_to_speech(img_path)

    # If 'q' is pressed, break the loop and close the camera
    if key == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
