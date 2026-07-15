import cv2
import os
import sys


def load_face_detector():
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

    face_detector = cv2.CascadeClassifier(cascade_path)

    if face_detector.empty():
        print("Error: Face detection model could not be loaded.")
        sys.exit()

    return face_detector


def detect_faces(image, face_detector):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray_image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40, 40)
    )

    return faces


def draw_face_boxes(image, faces):
    for number, (x, y, width, height) in enumerate(faces, start=1):
        cv2.rectangle(
            image,
            (x, y),
            (x + width, y + height),
            (0, 255, 0),
            2
        )

        cv2.putText(
            image,
            f"Face {number}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    return image


def detect_faces_from_image(face_detector):
    image_path = input("Enter the image path: ").strip().strip('"')

    if not os.path.exists(image_path):
        print("Error: Image file not found.")
        return

    image = cv2.imread(image_path)

    if image is None:
        print("Error: Unable to read the image.")
        return

    faces = detect_faces(image, face_detector)
    output_image = draw_face_boxes(image.copy(), faces)

    print(f"\nTotal faces detected: {len(faces)}")

    output_path = "detected_faces_output.jpg"
    cv2.imwrite(output_path, output_image)

    print(f"Output saved as: {output_path}")
    print("Press any key to close the image window.")

    cv2.imshow("Face Detection Result", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def detect_faces_from_webcam(face_detector):
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Webcam could not be accessed.")
        return

    print("\nWebcam started.")
    print("Press 'Q' to quit.")

    while True:
        success, frame = camera.read()

        if not success:
            print("Error: Unable to capture video frame.")
            break

        faces = detect_faces(frame, face_detector)
        output_frame = draw_face_boxes(frame, faces)

        cv2.putText(
            output_frame,
            f"Faces Detected: {len(faces)}",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.imshow("Real-Time Face Detection", output_frame)

        pressed_key = cv2.waitKey(1) & 0xFF

        if pressed_key == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


def display_menu():
    print("=" * 55)
    print("        AI FACE DETECTION SYSTEM")
    print("=" * 55)
    print("1. Detect faces from an image")
    print("2. Detect faces using webcam")
    print("3. Exit")


def main():
    face_detector = load_face_detector()

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            detect_faces_from_image(face_detector)

        elif choice == "2":
            detect_faces_from_webcam(face_detector)

        elif choice == "3":
            print("\nThank you for using the Face Detection System.")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
