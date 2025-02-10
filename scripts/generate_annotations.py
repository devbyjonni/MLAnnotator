import os
import json
import cv2
import tkinter as tk
from tkinter import filedialog
from matplotlib.widgets import RectangleSelector
import matplotlib.pyplot as plt

# Global variables
annotations = []
current_image = None
top_left_corner = None
bottom_right_corner = None

def line_select_callback(clk, rls):
    global top_left_corner, bottom_right_corner
    top_left_corner = (int(clk.xdata), int(clk.ydata))
    bottom_right_corner = (int(rls.xdata), int(rls.ydata))

def save_annotation(image_filename, label):
    global top_left_corner, bottom_right_corner, annotations
    if top_left_corner and bottom_right_corner:
        annotation = {
            "imagefilename": image_filename,
            "annotations": [
                {
                    "label": label,
                    "coordinates": {
                        "x": (top_left_corner[0] + bottom_right_corner[0]) // 2,
                        "y": (top_left_corner[1] + bottom_right_corner[1]) // 2,
                        "width": abs(top_left_corner[0] - bottom_right_corner[0]),
                        "height": abs(top_left_corner[1] - bottom_right_corner[1])
                    }
                }
            ]
        }
        annotations.append(annotation)

def annotate_image(image_path):
    global current_image

    current_image = os.path.basename(image_path)

    # Automatically use the filename (without .png) as the label
    label = current_image.replace(".png", "")

    image = cv2.imread(image_path)
    height, width, _ = image.shape  # Get image dimensions

    annotation = {
        "imagefilename": current_image,
        "annotations": [
            {
                "label": label,
                "coordinates": {
                    "x": width // 2,
                    "y": height // 2,
                    "width": width,
                    "height": height
                }
            }
        ]
    }

    annotations.append(annotation)
    print(f"✅ Auto-labeled {current_image} as '{label}' with full image bounding box.")

def onkeypress(event):
    if event.key == 'q':  # Press 'q' to confirm bounding box
        label = input(f"Enter label for {current_image}: ")
        save_annotation(current_image, label)
        plt.close()

def save_annotations_json(output_path):
    with open(output_path, "w") as f:
        json.dump(annotations, f, indent=4)
    print(f"✅ Annotations saved to {output_path}")

def main():
    root = tk.Tk()
    root.withdraw()
    
    print("🟢 Selecting image folder...")
    image_folder = filedialog.askdirectory(title="Select Image Folder")
    
    if not image_folder:
        print("❌ No folder selected. Exiting.")
        return

    print(f"📂 Selected image folder: {image_folder}")
    
    image_files = [f for f in os.listdir(image_folder) if f.endswith(".png")]
    if not image_files:
        print("❌ No PNG images found in the selected folder.")
        return

    print(f"🟢 Found {len(image_files)} images. Starting annotation...")

    for image_file in image_files:
        print(f"🖼 Opening: {image_file}")
        annotate_image(os.path.join(image_folder, image_file))
    
    output_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if output_path:
        save_annotations_json(output_path)

    print("✅ Annotation process complete!")

# ✅ Ensure the script runs when executed
if __name__ == "__main__":
    main()