import cv2

#Read the image
img = cv2.imread("image.jpg")

cv2.circle(img, (200, 200), 50, (0, 0, 255), 2)

cv2.rectangle(img, (50, 50), (300, 300), (0, 255, 0), 2)

cv2.putText(img, "Hello OpenCV", (50, 400),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (255, 0, 0), 2)

#Display the image
cv2.imshow("image", img)


#Wait  until  a key is pressed
cv2.waitKey(0)

#Close the image window
cv2.destroyAllWindows()






