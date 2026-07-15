from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load pre-trained model
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

# Load image
image = Image.open("sample.jpg").convert("RGB")

# Process image
inputs = processor(images=image, return_tensors="pt")

# Generate caption
output = model.generate(**inputs)

# Print caption
caption = processor.decode(output[0], skip_special_tokens=True)

print("Generated Caption:")
print(caption)
