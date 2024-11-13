import cv2
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load the pre-trained model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Function to generate caption and description from image
def generate_caption_from_image(img_input):
    # Preprocess the image and feed it into the model
    inputs = processor(img_input, return_tensors="pt")
    
    # Generate caption with max_new_tokens for better control over length
    out = model.generate(**inputs, max_new_tokens=50)  # Set max_new_tokens to desired length
    
    # Decode the generated output to get the caption
    caption = processor.decode(out[0], skip_special_tokens=True)
    
    return caption

# Open the camera
cap = cv2.VideoCapture(0)  # 0 is the default camera

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Display the resulting frame
    cv2.imshow('Press "p" to capture photo', frame)
    
    # Wait for the keypress event
    key = cv2.waitKey(1) & 0xFF
    
    # If 'p' key is pressed, capture the image and generate the caption
    if key == ord('p'):
        # Convert the frame to a PIL image
        img_input = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        
        # Generate the caption for the captured image
        caption = generate_caption_from_image(img_input)
        
        # Display the generated caption
        print("Generated Caption:", caption)
        
        # Optionally, save the captured image (you can comment this out if not needed)
        cv2.imwrite('captured_image.jpg', frame)

    # If 'q' is pressed, break the loop and close the camera
    if key == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
