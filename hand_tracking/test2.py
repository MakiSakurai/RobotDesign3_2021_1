import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)
    image_height, image_width, _ = image.shape
    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        for index, landmark in enumerate(hand_landmarks.landmark):
            if index == 3: #親指第一関節
                cx3,cy3 = landmark.x * image_width, landmark.y * image_height
                #print("index3 = ",end='')
                #print(cx3,cy3)

            if index == 7: #人差し指第一関節
                cx7,cy7 = landmark.x * image_width, landmark.y * image_height
                #print("index7 = ",end='')
                #print(cx7,cy7)

            if index == 11: #中指第一関節
                cx11,cy11 = landmark.x * image_width, landmark.y * image_height
                #print("index11 = ",end='')
                #print(cx11,cy11)

            if index == 15: #薬指第一関節
                cx15,cy15 = landmark.x * image_width, landmark.y * image_height
                #print("index15 = ",end='')
                #print(cx15,cy15)

            if index == 19: #小指第一関節
                cx19,cy19 = landmark.x * image_width, landmark.y * image_height
                #print("index19 = ",end='')
                #print(cx19,cy19)

        cx3_7,cy3_7 = (cx3+cx7)/2, (cy3+cy7)/2
        cx3_7 = int(cx3_7)
        cy3_7 = int(cy3_7)
        cv2.circle(image, (cx3_7,cy3_7), 5, (0, 255, 0), 2)

        cx7_11,cy7_11 = (cx7+cx11)/2, (cy7+cy11)/2
        cx7_11 = int(cx7_11)
        cy7_11 = int(cy7_11)
        cv2.circle(image, (cx7_11,cy7_11), 5, (0, 255, 0), 2)

        cx11_15,cy11_15 = (cx11+cx15)/2, (cy11+cy15)/2
        cx11_15 = int(cx11_15)
        cy11_15 = int(cy11_15)
        cv2.circle(image, (cx11_15,cy11_15), 5, (0, 255, 0), 2)

        cx15_19,cy15_19 = (cx15+cx19)/2, (cy15+cy19)/2
        cx15_19 = int(cx15_19)
        cy15_19 = int(cy15_19)
        cv2.circle(image, (cx15_19,cy15_19), 5, (0, 255, 0), 2)

        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
    