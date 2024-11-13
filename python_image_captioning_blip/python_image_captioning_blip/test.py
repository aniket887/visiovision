from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load the pre-trained model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Function to generate caption and description from image path
def generate_caption_from_path(image_path):
    # Open the image using the provided path
    img_input = Image.open(image_path)
    
    # Preprocess the image and feed it into the model
    inputs = processor(img_input, return_tensors="pt")
    
    # Generate caption with max_new_tokens for better control over length
    out = model.generate(**inputs, max_new_tokens=50)  # Set max_new_tokens to desired length
    
    # Decode the generated output to get the caption
    caption = processor.decode(out[0], skip_special_tokens=True)
    
    return caption

# Example of using the function
image_path = r"E:\hachthon\ideathon\code\img.jpg"  # Replace with the path to your image
caption = generate_caption_from_path(image_path)
print("Generated Caption:", caption)
