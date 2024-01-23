import torch
from torchvision import transforms
from yolov4_tiny import YOLOv4Tiny



#
# # Load pre-trained YOLOv4 Tiny model
# model = YOLOv4Tiny(pretrained=True)
#
# # Load an image for inference
# image_path = 'path/to/your/image.jpg'
# image = transforms.ToTensor()(Image.open(image_path).convert('RGB')).unsqueeze(0)
#
# # Perform inference
# with torch.no_grad():
#     detections = model(image)
#
# # Display results
# print("Detected objects:")
#
# for detection in detections[0]:
#     class_id, confidence, bbox = detection[0], detection[1], detection[2:]
#     print(f"Class ID: {int(class_id)}, Confidence: {confidence:.2f}, Bounding Box: {bbox}")
#
# # Note: Adjust the image_path variable to the path of your test image

# Check PyTorch and torchvision
try:
    import torch
    import torchvision
    print("PyTorch and torchvision are installed.")
except ImportError:
    print("PyTorch and/or torchvision are not installed.")

# Check Numpy
try:
    import numpy
    print("Numpy is installed.")
except ImportError:
    print("Numpy is not installed.")

# Check Pillow
try:
    from PIL import Image
    print("Pillow (PIL) is installed.")
except ImportError:
    print("Pillow (PIL) is not installed.")

# Check Matplotlib
try:
    import matplotlib
    print("Matplotlib is installed.")
except ImportError:
    print("Matplotlib is not installed.")

# Check OpenCV
try:
    import cv2
    print("OpenCV is installed.")
except ImportError:
    print("OpenCV is not installed.")
