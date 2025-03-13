import cv2


def main():
    image = cv2.imread("src/week02/image1.jpg")
    half = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    half = cv2.resize(half, (0, 0), fx=0.4, fy=0.4)

    cv2.imwrite("src/week02/image1_resize.jpg", half)

    cv2.imshow("Display Window", half)

    # cap.release()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
