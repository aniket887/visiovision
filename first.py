import pytesseract
from PIL import Image, ImageEnhance
import pyttsx3

# Path to Tesseract executable (change to your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    # Load the image from the path
    image = Image.open(image_path)

    # Convert image to grayscale
    image = image.convert('L')

    # Apply some enhancement to improve text extraction
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  # Adjust contrast for better text visibility

    return image

def image_to_text_to_speech(image_path):
    # Preprocess the image for better OCR results
    image = preprocess_image(image_path)

    # Extract text from the image
    text = pytesseract.image_to_string(image)

    # Print the extracted text
    print("Extracted Text:", text)

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties for the voice (optional)
    engine.setProperty('rate', 150)     # Speed of speech
    engine.setProperty('volume', 0.9)   # Volume level (0.0 to 1.0)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Usage Example
image_to_text_to_speech('txt.jpeg')
