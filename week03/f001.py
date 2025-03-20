import cv2
import os


def main():
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    cap = cv2.VideoCapture(0)

    user_id = input("Enter user ID: ")
    dataset_path = "dataset"

    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path)

    count = 0
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for x, y, w, h in faces:
            count += 1
            face = gray[y : y + h, x : x + w]
            cv2.imwrite(f"{dataset_path}/{user_id}_{count}.jpg", face)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("Face Capture", frame)
        if count >= 50 or cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
