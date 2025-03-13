import cv2


def main():
    cascPath = "src/haarcascade_frontalface_default.xml"
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        image = frame
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faceCascade = cv2.CascadeClassifier(cascPath)
        faces = faceCascade.detectMultiScale(gray)

        print(f"There are {len(faces)} faces found.")

        for x, y, w, h in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("cam", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # cv2.imshow("Display Window", half)

    # cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()
