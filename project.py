import cv2

face_det=cv2.CascadeClassifier('/home/kobra/dspproject/haarcascade_frontalface_alt.xml')
eye_det=cv2.CascadeClassifier('/home/kobra/dspproject/haarcascade_eye.xml')
smile_det=cv2.CascadeClassifier('/home/kobra/dspproject/haarcascade_smile.xml')
#print('hey')
cam=cv2.VideoCapture(0)

while(1):
    #print('running')
    ret,frame=cam.read()
    cv2.imshow('camera',frame)
    k=cv2.waitKey(1) # The function only works if there is at least one HighGUI
    # window created and the window is active. Delay in milliseconds

    if(k==ord(' ')):
        #SPACE pressed
        img_name='opencv_frame_0.png'
        print('Image clicked!')

        #taking a screenshot
        cv2.imwrite(img_name,frame)

        #reading the image
        i=cv2.imread(img_name)

        #converting into a grayscale image
        j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)

        #detect faces,eyes,smiles
        faces=face_det.detectMultiScale(j)
        eyes=eye_det.detectMultiScale(j,minNeighbors=15,scaleFactor=1.2)
        smile=smile_det.detectMultiScale(j,minNeighbors=15,scaleFactor=1.2)

        #drawing a rectangle
        for (x,y,w,h) in faces:
            f=cv2.rectangle(i,(x,y),(x+w,y+h),(255,0,0),4)
            for (x1,y1,w1,h1) in eyes:
                if(x1>x and y1>y and x1+w1<x+w and y1+h1<y+h):
                    cv2.rectangle(i,(x1,y1),(x1+w1,y1+h1),(0,0,255),4)
            for (x2,y2,w2,h2) in smile:
                if(x2>x and y2>y and x2+w2<x+w and y2+h2<y+h):
                    cv2.rectangle(i,(x2,y2),(x2+w2,y2+h2),(0,0,255),4)
        
        cv2.imshow('image',i)
        
    elif(k==ord('x')):
        #X pressed
        cam.release()
        cv2.destroyAllWindows()
        break
