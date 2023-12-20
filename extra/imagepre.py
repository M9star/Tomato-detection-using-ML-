import cv2
import numpy as np

def get_image(filename):
  """Gets the image from the file."""
  image = cv2.imread(filename)
  return image


def convert_to_hsi(image):
  """Converts the image to HSI space."""
  # Convert the image to float32 for accurate calculations.
  image = image.astype(np.float32) / 255.0

  # Separate the channels.
  B, G, R = image[:, :, 0], image[:, :, 1], image[:, :, 2]

  # Calculate Intensity (I).
  I = (R + G + B) / 3.0

  # Calculate Saturation (S).
  min_val = np.minimum(np.minimum(R, G), B)
  max_val = np.maximum(np.maximum(R, G), B)
  delta = max_val - min_val
  S = delta / max_val

  # Calculate Hue (H).
  H = np.zeros_like(I)
  H[delta == 0] = 0
  H[max_val == R] = (60 * ((G - B) / delta) % 360)[max_val == R]
  H[max_val == G] = (60 * ((B - R) / delta) + 120)[max_val == G]
  H[max_val == B] = (60 * ((R - G) / delta) + 240)[max_val == B]

  # Normalize H to be in the range [0, 1] if needed.
  H /= 360.0

  # Stack the HSI channels.
  hsi = np.stack((H, S, I), axis=-1)

  return hsi

def enhance_image(hsi):
  """Enhances the image using the CLAHE method."""
  clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
  enhanced_i = clahe.apply(hsi[:, :, 2])
  hsi[:, :, 2] = enhanced_i
  return hsi

def main():
  """The main function."""
  image = get_image("image.jpg")
  hsi = convert_to_hsi(image)
  enhanced_image = enhance_image(hsi)
  cv2.imshow("Original Image", image)
  cv2.imshow("Enhanced Image", enhanced_image)
  cv2.waitKey(0)

if __name__ == "__main__":
  main()