import cv2
from cvzone.HandTrackingModule import HandDetector

cap=cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8,maxHands=2)

class Button():
    def __init__(self,pos,text,size=[85,85]):
        self.pos = pos
        self.size=size
        self.text=text

    def draw(self,frame):
        x,y = self.pos
        w,h = self.size

        cv2.rectangle(frame,
                      self.pos,
                      (x + w, y + h),
                    (255,0,255),
                    cv2.FILLED)
        cv2.putText(frame,self.text,
                    (x + 20, y + 65),
                    cv2.FONT_HERSHEY_PLAIN,4,
                    (255,255,255),4)
        return frame

myButton = Button([100,100],"Q")

while cap.isOpened():
    ret,frame = cap.read()
    hands,frame = detector.findHands(frame)
    myButton.draw(frame)
    cv2.imshow("frame",frame)


    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
    