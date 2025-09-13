import cv2

url = "http://192.168.100.7:4747/video"
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read() 

    if not ret:
        print("Je ne reçois pas l'image.")
        break
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

   
    edges = cv2.Canny(blur, 50, 150)

    
    cv2.imshow("Image originale", frame)
    cv2.imshow("Gris", gray)
    cv2.imshow("Bords (Canny)", edges)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
