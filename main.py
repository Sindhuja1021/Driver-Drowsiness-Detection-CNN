"""
Driver Drowsiness Detection using OpenCV + MediaPipe.

Steps:
 1. Read a frame from the webcam.
 2. Find the face and eye landmarks using MediaPipe Face Mesh.
 3. Calculate the EAR for both eyes and take the average.
 4. If EAR stays below the threshold for many frames -> ring the alarm.
 5. Show everything on the screen. Press 'q' to quit.
"""

import cv2
import mediapipe as mp

import config
from alarm import Alarm
from eye_utils import LEFT_EYE, RIGHT_EYE, calculate_ear, get_eye_points


def main():
    camera = cv2.VideoCapture(config.CAMERA_INDEX)
    if not camera.isOpened():
        print("Error: Could not open the camera.")
        return

    face_mesh = mp.solutions.face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
    )
    alarm = Alarm()

    closed_frames = 0   # how many frames in a row the eyes were closed
    alert_count = 0     # how many times the alarm was triggered
    alarm_active = False

    print("Started. Press 'q' in the video window to quit.")

    while True:
        success, frame = camera.read()
        if not success:
            print("Error: Could not read from the camera.")
            break

        frame = cv2.flip(frame, 1)  # mirror view
        height, width = frame.shape[:2]

        # MediaPipe needs RGB images, but OpenCV gives BGR
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb_frame)

        if result.multi_face_landmarks:
            landmarks = result.multi_face_landmarks[0].landmark

            left_points = get_eye_points(landmarks, LEFT_EYE, width, height)
            right_points = get_eye_points(landmarks, RIGHT_EYE, width, height)

            ear = (calculate_ear(left_points) + calculate_ear(right_points)) / 2.0

            # Draw small green dots on the eyes
            for point in left_points + right_points:
                cv2.circle(frame, point, 2, (0, 255, 0), -1)

            if ear < config.EAR_THRESHOLD:
                closed_frames += 1
            else:
                closed_frames = 0

            if closed_frames >= config.CLOSED_FRAMES_LIMIT:
                if not alarm_active:
                    alert_count += 1
                    alarm_active = True
                alarm.start()
                cv2.putText(frame, "DROWSINESS ALERT!", (20, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
            else:
                alarm_active = False
                alarm.stop()

            cv2.putText(frame, f"EAR: {ear:.2f}", (20, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
        else:
            # No face found, so reset everything
            closed_frames = 0
            alarm_active = False
            alarm.stop()
            cv2.putText(frame, "No face detected", (20, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 165, 255), 2)

        cv2.putText(frame, f"Alerts: {alert_count}", (20, height - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow("Driver Drowsiness Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    alarm.stop()
    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
