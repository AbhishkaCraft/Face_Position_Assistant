import cv2

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        print("Camera not reading frames")
        break

    height, width, _ = frame.shape
    #draw center point
    center_x = width//2
    center_y = height//2

    cv2.circle(frame, (center_x , center_y),5, (0,0,255), -1)

    cv2.rectangle(frame, (200,150),(400,350),(0,255,0),2)


    cv2.imshow("Live Camera", frame)

#EXIT
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()