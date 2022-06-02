import cv2
import numpy as np
from time import sleep
import time
import serial

counter = 15
start = time.time()

largura_min=80 
altura_min=80 

offset=6   

pos_linha=550  

delay= 60

detec = []
carros= 0
carros1= 0
carros2= 0
carros3= 0

led1 =0
led2 =0
led3 =0
led4 =1

arduino = serial.Serial('COM13',9600,timeout = 1)
time.sleep(2)

def pega_centro(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx,cy
    
#https://drive.google.com/file/d/1iWqLaqBCYgx7wSBZ3PIvX1ODzs9GjcTq/view?usp=sharing
cap = cv2.VideoCapture('video.mp4')
subtracao = cv2.bgsegm.createBackgroundSubtractorMOG()

cap1 = cv2.VideoCapture('video1.mp4')
subtracao1 = cv2.bgsegm.createBackgroundSubtractorMOG()

cap2 = cv2.VideoCapture('video2.mp4')
subtracao2 = cv2.bgsegm.createBackgroundSubtractorMOG()

cap3 = cv2.VideoCapture('video3.mp4')
subtracao3 = cv2.bgsegm.createBackgroundSubtractorMOG()

print("lane 4 is on")
while True:
    time.sleep(0.1)
    if(led1!=1):
    
        ret,frame1=cap.read()
        tempo = float(1/delay)
        sleep(tempo) 
        grey = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(grey,(3,3),5)
        img_sub = subtracao.apply(blur)
        dilat = cv2.dilate(img_sub,np.ones((5,5)))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        dilatada = cv2.morphologyEx (dilat, cv2. MORPH_CLOSE , kernel)
        dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
            
        contorno,h = cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (255,127,0), 3) 
        for(i,c) in enumerate(contorno):
            (x,y,w,h) = cv2.boundingRect(c)
            validar_contorno = (w >= largura_min) and (h >= altura_min)
            if not validar_contorno:
                continue

            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)        
            centro = pega_centro(x, y, w, h)
            detec.append(centro)
            cv2.circle(frame1, centro, 4, (0, 0,255), -1)
 
            for (x,y) in detec:
                if y<(pos_linha+offset) and y>(pos_linha-offset):
                    carros+=1
                    cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (0,127,255), 3)  
                    detec.remove((x,y))
                    #print("No of vehicles detected1: "+str(carros))
            
       
        cv2.putText(frame1, "Vehicles: "+str(carros), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
        cv2.imshow("Video Original" , frame1)
        cv2.imshow("Detector",dilatada)
    
      

    if(led2!=1):
    
        ret,frame1=cap1.read()
        tempo = float(1/delay)
        sleep(tempo) 
        grey = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(grey,(3,3),5)
        img_sub = subtracao1.apply(blur)
        dilat = cv2.dilate(img_sub,np.ones((5,5)))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        dilatada = cv2.morphologyEx (dilat, cv2. MORPH_CLOSE , kernel)
        dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
            
        contorno,h = cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (255,127,0), 3) 
        for(i,c) in enumerate(contorno):
            (x,y,w,h) = cv2.boundingRect(c)
            validar_contorno = (w >= largura_min) and (h >= altura_min)
            if not validar_contorno:
                continue

            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)        
            centro = pega_centro(x, y, w, h)
            detec.append(centro)
            cv2.circle(frame1, centro, 4, (0, 0,255), -1)
 
            for (x,y) in detec:
                if y<(pos_linha+offset) and y>(pos_linha-offset):
                    carros1+=1
                    cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (0,127,255), 3)  
                    detec.remove((x,y))
                    #print("No of vehicles detected2: "+str(carros1))
            
       
        cv2.putText(frame1, "Vehicles1: "+str(carros1), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
        cv2.imshow("Video Original1" , frame1)
        cv2.imshow("Detector1",dilatada)      

    if(led3!=1):
        ret , frame1 = cap2.read()
        tempo = float(1/delay)
        sleep(tempo) 
        grey = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(grey,(3,3),5)
        img_sub = subtracao2.apply(blur)
        dilat = cv2.dilate(img_sub,np.ones((5,5)))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        dilatada = cv2.morphologyEx (dilat, cv2. MORPH_CLOSE , kernel)
        dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
            
        contorno,h = cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (255,127,0), 3) 
        for(i,c) in enumerate(contorno):
            (x,y,w,h) = cv2.boundingRect(c)
            validar_contorno = (w >= largura_min) and (h >= altura_min)
            if not validar_contorno:
                continue

            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)        
            centro = pega_centro(x, y, w, h)
            detec.append(centro)
            cv2.circle(frame1, centro, 4, (0, 0,255), -1)

            for (x,y) in detec:
                if y<(pos_linha+offset) and y>(pos_linha-offset):
                    carros2+=1
                    cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (0,127,255), 3)  
                    detec.remove((x,y))
                    #print("No of vehicles detected3: "+str(carros2))
            
               
        cv2.putText(frame1, "Vehicles2: "+str(carros2), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
        cv2.imshow("Video Original2" , frame1)
        cv2.imshow("Detector2",dilatada)
    
    if(led4!=1):
        ret , frame1 = cap3.read()
        tempo = float(1/delay)
        sleep(tempo) 
        grey = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(grey,(3,3),5)
        img_sub = subtracao3.apply(blur)
        dilat = cv2.dilate(img_sub,np.ones((5,5)))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        dilatada = cv2.morphologyEx (dilat, cv2. MORPH_CLOSE , kernel)
        dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
            
        contorno,h = cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (255,127,0), 3) 
        for(i,c) in enumerate(contorno):
            (x,y,w,h) = cv2.boundingRect(c)
            validar_contorno = (w >= largura_min) and (h >= altura_min)
            if not validar_contorno:
                continue

            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)        
            centro = pega_centro(x, y, w, h)
            detec.append(centro)
            cv2.circle(frame1, centro, 4, (0, 0,255), -1)

            for (x,y) in detec:
                if y<(pos_linha+offset) and y>(pos_linha-offset):
                    carros3+=2
                    cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (0,127,255), 3)  
                    detec.remove((x,y))
                    #print("No of vehicles detected4: "+str(carros3))
            
               
        cv2.putText(frame1, "Vehicles3: "+str(carros3), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
        cv2.imshow("Video Original3" , frame1)
        cv2.imshow("Detector3",dilatada)
    if time.time() - start > 1:
        start = time.time()
        counter = counter - 1

        ### This will be updated once per second
        print ("%s seconds remaining" % counter)

        ### Countdown finished, ending loop
        if counter <= 0:
            #counter = 31;
            if led1==1:
                led1=0;
                carros = 0;
                print("No of vehicles detected1: "+str(carros))
                print("No of vehicles detected2: "+str(carros1))
                print("No of vehicles detected3: "+str(carros2))
                print("No of vehicles detected4: "+str(carros3))
                if (carros1 > carros2) and (carros1 > carros3):
                    command = str.encode('2')
                    arduino.write(command)
                    time.sleep(1.5)
                    led2=1;
                    print("lane 2 is on")
                    counter = 2*carros1;
                elif (carros2 > carros1) and (carros2 > carros3):
                    command = str.encode('3')
                    arduino.write(command)
                    time.sleep(1.5)
                    led3=1;
                    print("lane 3 is on")
                    counter = 2*carros2;
                else:
                    command = str.encode('4')
                    arduino.write(command)
                    time.sleep(1.5)
                    led4=1;
                    print("lane 4 is on")
                    counter = 2*carros3;
                continue;
            if led2==1:
                led2=0;
                carros1=0;
                print("No of vehicles detected1: "+str(carros))
                print("No of vehicles detected2: "+str(carros1))
                print("No of vehicles detected3: "+str(carros2))
                print("No of vehicles detected4: "+str(carros3))
                if (carros > carros2) and (carros > carros3):
                    command = str.encode('1')
                    arduino.write(command)
                    time.sleep(1.5)
                    led1=1;
                    print("lane 1 is on")
                    counter = 2*carros;
                elif (carros2 > carros) and (carros2 > carros3):
                    command = str.encode('3')
                    arduino.write(command)
                    time.sleep(1.5)
                    led3=1
                    print("lane 3 is on")
                    counter = 2*carros2;
                else:
                    command = str.encode('4')
                    arduino.write(command)
                    time.sleep(1.5)
                    led4=1;
                    print("lane 4 is on")
                    counter = 2*carros3;
                continue;
            if led3==1:
                led3=0;
                carros2=0;
                print("No of vehicles detected1: "+str(carros))
                print("No of vehicles detected2: "+str(carros1))
                print("No of vehicles detected3: "+str(carros2))
                print("No of vehicles detected4: "+str(carros3))
                if (carros > carros1) and (carros > carros3):
                    command = str.encode('1')
                    arduino.write(command)
                    time.sleep(1.5)
                    led1=1;
                    print("lane 1 is on")
                    counter = 2*carros;
                elif (carros1 > carros) and (carros1 > carros3):
                    command = str.encode('2')
                    arduino.write(command)
                    time.sleep(1.5)
                    led2=1
                    print("lane 2 is on")
                    counter = 2*carros1;
                else:
                    command = str.encode('4')
                    arduino.write(command)
                    time.sleep(1.5)
                    led4=1
                    print("lane 4 is on")
                    counter = 2*carros3;
                continue;
            if led4==1:
                led4=0;
                carros3=0;
                print("No of vehicles detected1: "+str(carros))
                print("No of vehicles detected2: "+str(carros1))
                print("No of vehicles detected3: "+str(carros2))
                print("No of vehicles detected4: "+str(carros3))
                if (carros > carros1) and (carros > carros2):
                    command = str.encode('1')
                    arduino.write(command)
                    time.sleep(1.5)
                    led1=1;
                    print("lane 1 is on")
                    counter = 2*carros;
                elif (carros1 > carros) and (carros1 > carros2):
                    command = str.encode('2')
                    arduino.write(command)
                    time.sleep(1.5)
                    led2=1
                    print("lane 2 is on")
                    counter = 2*carros1;
                else:
                    command = str.encode('3')
                    arduino.write(command)
                    time.sleep(1.5)
                    led3=1
                    print("lane 3 is on")
                    counter = 2*carros2;
                continue
           
            
            
    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()
cap.release()
