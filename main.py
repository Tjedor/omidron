from tello import Tello
import time
import cv2
import pyttsx3


def stream():
    faceCascade = cv2.CascadeClassifier("model.xml")
    cap = cv2.VideoCapture("udp://" + "192.168.10.1" + ":11111")
    # Runs while 'stream_state' is True
    while True:
        c = 0
        ret, last_frame = cap.read()
        gray = cv2.cvtColor(last_frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("DJI Tello", gray)

        # Video Stream is closed if escape key is pressed
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


drone = Tello()
drone.send_command("streamon")
stream()

# drone.takeoff()

# drone.enable_mission_pad()
# drone.up(70)
# drone.get_height()
# drone.do_a_nigga_flip("l")

# drone.land()
