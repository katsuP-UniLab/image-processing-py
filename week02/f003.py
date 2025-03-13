import cv2
import os


def main():
    input_folder = "src/week02/input"
    output_folder = "src/week02/output"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    target_size = (1600, 900)

    for i, filename in enumerate(os.listdir(input_folder)):
        if filename.endswith((".jpg", ".png", ".jpeg")):
            img_path = os.path.join(input_folder, filename)
            image = cv2.imread(img_path)

        if image is not None:
            # ปรับขนาดภาพ
            resized_image = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)

            # บันทึกภาพใหม่
            output_path = os.path.join(output_folder, f"resized_{i+1}.jpg")
            cv2.imwrite(output_path, resized_image)

            print(f"Resized and saved: {output_path}")
        else:
            print(f"Failed to load: {image_path}")


print("✅ Resize completed!")
