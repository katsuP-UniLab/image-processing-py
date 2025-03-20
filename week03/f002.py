import cv2
import numpy as np


def main():
    # ตรวจสอบว่ามีโมดูล face หรือไม่
    if not hasattr(cv2, "face"):
        raise Exception(
            "OpenCV installation does not include 'face' module. Install 'opencv-contrib-python'"
        )

    # โหลดโมเดลที่ฝึกแล้ว
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    try:
        recognizer.read("src/week03/face_recognizer.yml")
    except Exception as e:
        print("Error loading model:", e)
        exit()

    # โหลดตัวตรวจจับใบหน้า
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # สร้าง dictionary สำหรับ map label กับชื่อผู้ใช้
    # label_names = {1: "Yao", 2: "Mesa"}  # คุณสามารถเพิ่มชื่อได้ตามต้องการ
    # โหลด dictionary สำหรับ map label กับชื่อผู้ใช้จากไฟล์ .npy
    label_names = np.load("src/week03/label_to_name.npy", allow_pickle=True).item()

    # ตรวจสอบว่าเปิดกล้องได้หรือไม่
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot access webcam")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50)
        )

        for x, y, w, h in faces:
            face = gray[y : y + h, x : x + w]
            try:
                label, confidence = recognizer.predict(face)
            except Exception as e:
                print("Error in prediction:", e)
                continue

            # ตรวจสอบว่า label มีอยู่ใน dictionary หรือไม่
            if label in label_names:
                name = label_names[label]
            else:
                name = "Unknown"

            if confidence < 70:  # ค่าความมั่นใจ ยิ่งต่ำยิ่งแม่นยำ
                text = f"{name} ({confidence:.2f})"
                color = (0, 255, 0)  # สีเขียวสำหรับที่รู้จัก
            else:
                text = "Unknown"
                color = (0, 0, 255)  # สีแดงสำหรับไม่รู้จัก

            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(
                frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2
            )

        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
