import cv2
import numpy as np
import KeyPress_Module as kp
from djitellopy import Tello
from time import sleep
from threading import thread
global img
#YOLO Video Stream for DJI Tello

net = cv2.dnn.readNet('yolov3_custom2_last.weights', 'yolov3_custom2.cfg')
classes = []
with open('obj.names', 'r') as f:
    classes = f.read().splitlines()

kp.init()
tello = Tello()
tello.connect()
tello.streamon()
'''
def getkeyboardinput():
    lr, fb, ud, yv = 0,0,0,0
    speed = 20
    if kp.getkey("LEFT"): lr = -speed
    elif kp.getkey("RIGHT"): lr = speed

    if kp.getkey("UP"): fb = speed
    elif kp.getkey("DOWN"): fb = -speed

    if kp.getkey("w"): ud = speed
    elif kp.getkey("s"): ud =-speed

    if kp.getkey("a"): yv = speed
    elif kp.getkey("d"): yv = -speed

    if kp.getkey("q"): tello.land() ; time.sleep(3)
    if kp.getkey("e"): tello.takeoff()

    if kp.getkey("z"):
        cv2.imwrite(f'/Users/stevenchandra/PycharmProjects/DJITello/Resources/Images/{time.time()}.jpg',img)
        time.sleep(0.3)
    return[lr,fb, ud, yv]
'''

'''
while True:
    frame_read = tello.get_frame_read()
    image = frame_read.frame
    height, width, _ = image.shape

    blob = cv2.dnn.blobFromImage(image, 1/255, (416,416), (0,0,0), swapRB=True, crop = False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)

    boxes =[]
    confidences = []
    class_ids = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x,y,w,h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))

    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i], 2))
            color = colors[i]
            cv2.rectangle(image, (x,y), (x+w, y+h), color, 10)
            cv2.putText(image, label + " " + confidence, (x, y+20), font, 5, (255,255,255), 5)

        cv2.imshow("Image", image)
        key = cv2.waitKey(1)
        if key == 27:
            break

frame_read.release()
cv2.destroyAllWindows()
'''

#YOLO Video Stream for Videos
'''
net = cv2.dnn.readNet('yolov3_custom2_last.weights', 'yolov3_custom2.cfg')
classes = []
with open('obj.names', 'r') as f:
    classes = f.read().splitlines()

#Object Detection Using Videos
cap = cv2.VideoCapture('udp://@0.0.0.0:11111')
while True:
    _, image = cap.read()
    height, width, _ = image.shape

    blob = cv2.dnn.blobFromImage(image, 1/255, (416,416), (0,0,0), swapRB=True, crop = False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)

    boxes =[]
    confidences = []
    class_ids = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x,y,w,h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))

    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i], 2))
            color = colors[i]
            cv2.rectangle(image, (x,y), (x+w, y+h), color, 10)
            cv2.putText(image, label + " " + confidence, (x, y+20), font, 5, (255,255,255), 5)

        cv2.imshow("Image", image)
        key = cv2.waitKey(1)
        if key == 27:
            break

cap.release()
cv2.destroyAllWindows()

'''



#Object Detection Using Images
'''
image = cv2.imread('X.JPG')
height, width, _ = image.shape

blob = cv2.dnn.blobFromImage(image, 1/255, (416,416), (0,0,0), swapRB=True, crop = False)
net.setInput(blob)
output_layers_names = net.getUnconnectedOutLayersNames()
layerOutputs = net.forward(output_layers_names)

boxes =[]
confidences = []
class_ids = []

for output in layerOutputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0]*width)
            center_y = int(detection[1]*height)
            w = int(detection[2]*width)
            h = int(detection[3]*height)

            x = int(center_x - w/2)
            y = int(center_y - h/2)

            boxes.append([x,y,w,h])
            confidences.append((float(confidence)))
            class_ids.append(class_id)

print(len(boxes))
indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
print(indexes.flatten())

font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size=(len(boxes), 3))

for i in indexes.flatten():
    x, y, w, h = boxes[i]
    label = str(classes[class_ids[i]])
    confidence = str(round(confidences[i], 2))
    color = colors[i]
    cv2.rectangle(image, (x,y), (x+w, y+h), color, 10)
    cv2.putText(image, label + " " + confidence, (x, y+20), font, 5, (255,255,255), 5)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
dji = tello.Tello()
dji.connect()
print(dji.get_battery())
dji.streamon()

def Stream():
    while True:
        img = dji.get_frame_read().frame
        # img = cv2.resize(img, (360,240))
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

stream = Thread(target=Stream)
stream.start()
'''

#Video Record DJI Tello
'''
tello = Tello()
tello.connect()
print(tello.get_battery())

keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()

def videoRecorder():
    # create a VideoWrite object, recoring to ./video.avi
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        cv2.imshow("Video", frame_read.frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()

# we need to run the recorder in a seperate thread, otherwise blocking options
#  would prevent frames from getting added to the video
recorder = Thread(target=videoRecorder)
recorder.start()

'''

#Basic Movements
'''
dji = tello.Tello()
dji.connect()
print(dji.get_battery())

dji.streamon()
dji.takeoff()

dji.send_rc_control(0,0,15,0)
sleep(7)
dji.send_rc_control(0,0,15,0)
sleep(7)
dji.send_rc_control(0,0,15,0)
sleep(7)
dji.land()
'''

#Capture Image DJI Tello
'''
from djitellopy import tello
import cv2


dji = tello.Tello()
dji.connect()
print(dji.get_battery())

dji.streamon()

while True:
    img = dji.get_frame_read().frame
    #img = cv2.resize(img, (360,240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
'''

#Keypress Control
'''
import pygame

def init():
    pygame.init()
    winds = pygame.display.set_mode((720, 720))

def getkey(keyname):
    ans = False
    for eve in pygame.event.get():
        pass
    keyinput = pygame.key.get_pressed()
    mykey = getattr(pygame, 'K_{}'.format(keyname))
    if keyinput[mykey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getkey("LEFT"):
        print("Left Key Pressed")
    if getkey("RIGHT"):
        print("Right Key Pressed")



if __name__ == '__main__': #If you run this file as the main file, run it
    init()
    while True:
        main()
'''

