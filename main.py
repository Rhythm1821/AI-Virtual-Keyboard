import cv2
from cvzone.HandTrackingModule import HandDetector

cap=cv2.VideoCapture(0)
screen_width = 1920
screen_height = 1080
cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

detector = HandDetector(detectionCon=0.8,maxHands=2)

keys = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',';'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']
]

def drawAll(frame,buttonList):
        for button in buttonList:
            x,y = button.pos
            w,h = button.size
            cv2.rectangle(frame,
                        button.pos,
                        (x + w, y + h),
                        (255,0,255),
                        cv2.FILLED)
            cv2.putText(frame,button.text,
                        (x + 15, y + 35),
                        cv2.FONT_HERSHEY_PLAIN,2,
                        (255,255,255),2)
        return frame

class Button():
    def __init__(self,pos,text,size=[50,50]):
        self.pos = pos
        self.size=size
        self.text=text




buttonList = []

for i in range(len(keys)):
    for j,key in enumerate(keys[i]):
        buttonList.append(Button([50 * j + j * 15, 50 * i + 50 + i * 15],key))

while cap.isOpened():
    ret,frame = cap.read()
    hands,frame = detector.findHands(frame)
    drawAll(frame,buttonList)

 
    cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()