import cv2
import pyttsx3
engine=pyttsx3.init()
fd=cv2.CascadeClassifier('C:\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
cam=cv2.VideoCapture(0)
while True:
    r,i=cam.read()
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    face=fd.detectMultiScale(j)
    'ek frame me ek se jada face detect krne ke liye) aur j pe detect krke i pe show krenge'
    for (x,y,w,h) in face:
        cv2.rectangle(i,(x,y),(x+w,y+h),(0,0,255),2)
        '''i image pe x and y co ordinate se shuru krke x+w and y+h tak banana h rectangle
           with colour 0,0,255 and border width 4 or for filled rectangle ke liye -1)'''
    cv2.imshow('image1',i)
    K=cv2.waitKey(40)
    if(K==ord('q')):
        cv2.destroyAllWindows()
        del cam
        'variable delete kr diya'
        break
    print(face)
    for i in face :
        if(i[1]<100):
            engine.say("please keep distance. you are too close")
        elif(i[1]>150):
            engine.say("come close")
        else:
            engine.say("you are at the correct position")
            
    engine.runAndWait()
         
    
    
