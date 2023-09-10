import mediapipe as mp
import cv2 as cv
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
cap = cv.VideoCapture(0)
hands = mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)
while True:
    success, image = cap.read()
    if not success:
      continue
    image.flags.writeable = False
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    results = hands.process(cv.flip(image, 1))
    imageHeight, imageWidth, _ = image.shape
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,hand_landmarks,mp_hands.HAND_CONNECTIONS)
    cv.imshow('MediaPipe Hands', cv.cvtColor(cv.flip(image, 1), cv.COLOR_RGB2BGR))
    if cv.waitKey(10) == ord('q'):
      break
cap.release()
cv.destroyAllWindows()