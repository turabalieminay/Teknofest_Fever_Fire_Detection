import cv2
import numpy as np


fire_cascade = cv2.CascadeClassifier('ates.xml')

video = cv2.VideoCapture(0)

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))


forma = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("atestespiti.avi", forma , 30 , (width,height))

while True: 

    onay,frame = video.read()
    
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    
    ates = fire_cascade.detectMultiScale(frame , 1.2 , 3)

    cv2.putText(frame, "G-Robotics", (42,55) , cv2.FONT_HERSHEY_COMPLEX_SMALL ,0.75,(0,0,0),1)
    
    cv2.rectangle(frame,(40,40),(600,440),(0,255,0),1)
  
    for (x,y,w,h) in ates:
        
        cv2.rectangle(frame , (x-20,y-20),(x+w+20,y+h+20),(0,255,225),2)
        cv2.putText(frame, "Hedef Tespit Edildi", (42,435) , cv2.FONT_HERSHEY_COMPLEX_SMALL ,0.75,(0,0,0),1)
        frame_kor = frame[y:y+h , x:x+w]
        gray_kor = gray[y:y+h , x:x+w]
        print("Servolar Açıldı")
   
 
    
    out.write(frame)
    cv2.imshow("G-Robotics", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



video.release()
out.release()    
cv2.destroyAllWindows()        
cv2.waitKey(0)
   
