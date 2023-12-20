import cv2
import numpy as np

def resize_image(image, width, height):
  """Resizes an image using the bicubic interpolation algorithm."""
  resized_image = cv2.resize(image, dsize=(width, height), interpolation=cv2.INTER_CUBIC)
  return resized_image

def main():
  """The main function."""
  image = cv2.imread("image.jpg")
  width = 360
  height = 202
  resized_image = resize_image(image, width, height)
  cv2.imshow("Original Image", image)
  cv2.imshow("Resized Image", resized_image)
  cv2.waitKey(0)

if __name__ == "__main__":
  main()