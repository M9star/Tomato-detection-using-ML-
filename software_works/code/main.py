import torch
from torchvision import transforms
from PIL import Image
from yolov4_tiny import YOLOv4Tiny  # Import YOLOv4Tiny class

# Load pre-trained YOLOv4 Tiny model
model = YOLOv4Tiny(pretrained=True)

# Load an image for inference
image_path = r'C:\Users\M9\Desktop\Major_project\TomatoHarvesting\software_works\tomato58.jpg'
image = transforms.ToTensor()(Image.open(image_path).convert('RGB')).unsqueeze(0)

# Perform inference
with torch.no_grad():
    detections = model(image)

# Display results
print("Detected objects:")
for detection in detections[0]:
    class_id, confidence, bbox = detection[0], detection[1], detection[2:]
    print(f"Class ID: {int(class_id)}, Confidence: {confidence:.2f}, Bounding Box: {bbox}")
