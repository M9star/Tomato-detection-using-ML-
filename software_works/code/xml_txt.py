import xml.etree.ElementTree as ET
import os

def convert(xml_path, output_path, class_index, img_width, img_height):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    yolo_lines = []

    for obj in root.findall('object'):
        obj_name = obj.find('name').text
        if obj_name != 'tomato':
            continue

        bbox = obj.find('bndbox')
        xmin = float(bbox.find('xmin').text)
        ymin = float(bbox.find('ymin').text)
        xmax = float(bbox.find('xmax').text)
        ymax = float(bbox.find('ymax').text)

        x_center = (xmin + xmax) / (2 * img_width)
        y_center = (ymin + ymax) / (2 * img_height)
        box_width = (xmax - xmin) / img_width
        box_height = (ymax - ymin) / img_height

        yolo_line = f"{class_index} {x_center} {y_center} {box_width} {box_height}"
        yolo_lines.append(yolo_line)

    if yolo_lines:
        with open(output_path, 'w') as output_file:
            output_file.write('\n'.join(yolo_lines))

if __name__ == "__main__":
    input_folder = r"C:\Users\M9\Desktop\Dataset_tomato_kaggle\annotations"
    output_folder = r"C:\Users\M9\Desktop\Dataset_tomato_kaggle\annotations_txt"
    class_index = 0  # Assuming there is only one class 'tomato'
    img_width = 400
    img_height = 500

    os.makedirs(output_folder, exist_ok=True)

    for xml_file in os.listdir(input_folder):
        if xml_file.endswith(".xml"):
            xml_path = os.path.join(input_folder, xml_file)
            output_path = os.path.join(output_folder, xml_file.replace(".xml", ".txt"))

            convert(xml_path, output_path, class_index, img_width, img_height)

