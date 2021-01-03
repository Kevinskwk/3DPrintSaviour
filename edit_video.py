import cv2

cap = cv2.VideoCapture('detachment.mp4')
out = cv2.VideoWriter('detachment_new.avi', cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), 10.0, (1640, 1232))
font = cv2.FONT_HERSHEY_SIMPLEX
RED = (0, 0, 255)
ORANGE = (0, 128, 255)
YELLOW = (0, 255, 255)

i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame, (1640, 1232))
        i += 1
        print(i)
        if i > 123:
            #if defect == 'SPAGHETTI' or spaghetti:
            cv2.rectangle(frame, (25, 25), (1615, 1207), ORANGE, 50)
            cv2.putText(frame, 'DETACHMENT', (100, 1150), font, 7, ORANGE, 20)
            
            #if defect == 'DETACHMENT' or detached >= 1:
            #cv2.rectangle(frame, (8, 8), (632, 345), ORANGE, 16)
            #cv2.putText(frame, 'DETACHMENT', (50, 300), font, 2.5, ORANGE, 7)
            
            #if defect == 'AIR PRINT' or air:
            #    cv2.rectangle(curr_img, (25, 25), (1615, 1207), YELLOW, 50)
            #    cv2.putText(curr_img, 'AIR PRINT', (100, 1150), font, 8, YELLOW, 20)

        out.write(frame)

    else:
        break

out.release()

