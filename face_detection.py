import cv2

#Load pre-trained face model
face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)


cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        break

    height, width, _ = frame.shape

    screen_center_x = width // 2
    screen_center_y = height // 2

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.circle(frame, (screen_center_x, screen_center_y), 5, (255, 0 , 0), -1)

    faces = face_cascade.detectMultiScale(gray, 1.3 , 5)

    for(x, y , w, h) in faces:
        print(x,y,w,h)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)

        face_center_x = x + w //2
        face_center_y = y + h //2

        if face_center_x < screen_center_x -30:
             cv2.putText(frame, "Move Right",(30,50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                         1, (0,0,255) , 2)

        elif face_center_x > screen_center_x +30:
             cv2.putText(frame, "Move Left",(30,50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                         1, (0,0,255) , 2)

        else:
             cv2.putText(frame, "Perfect Position",(30,50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                         1, (0,255,0) , 2)
        if w < 180:

            cv2.putText(frame, "Come Closer", (30, 150),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 0, 0), 2)

        elif w > 260:
            cv2.putText(frame, "Move Back", (30, 150),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 0), 2)   

        cv2.circle(frame, (face_center_x, face_center_y),5,(0,0,255),-1)


    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()