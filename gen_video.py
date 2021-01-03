import cv2
import glob

img_names = glob.glob('img/*.jpg')
img_names.sort()
n = len(img_names)

out = cv2.VideoWriter('1.avi', cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), 10.0, (1640, 1232))
log = open('img/detected_result.txt')
font = cv2.FONT_HERSHEY_SIMPLEX
RED = (0, 0, 255)
ORANGE = (0, 128, 255)
YELLOW = (0, 255, 255)
spaghetti = False
detached = 0
air = False

for i in range(n):
    curr_file = img_names[i]
    print(curr_file)
    curr_img = cv2.imread(curr_file)
    curr_img = cv2.resize(curr_img, (1640, 1232))
    # cv2.imshow('w', curr_img)
    if i > 6:
        detection = log.readline()
        if detection != None and detection.strip() != '':
            defect = ''
            if 'BUT' in detection:
                defect = 'SPAGHETTI'
                spaghetti = True

            if detection[0] == '*':
                if detection[13:15] == 'Po':
                    defect = 'BREAKAGE'
                elif detection[13:15] == 'Fi':
                    defect = 'AIR PRINT'
                    air = True
                elif detection[13:15] == 'Pr':
                    defect = 'DETACHMENT'
                    detached += 1
                elif detection[13:15] == 'Sp':
                    defect = 'SPAGHETTI'
                    spaghetti = True
            
            #if defect == 'SPAGHETTI' or spaghetti:
            #    cv2.rectangle(curr_img, (25, 25), (1615, 1207), RED, 50)
            #    cv2.putText(curr_img, 'SPAGHETTI', (100, 1150), font, 8, RED, 20)
            
            #if detached >= 1:
            #    cv2.rectangle(curr_img, (25, 25), (1615, 1207), ORANGE, 50)
            #    cv2.putText(curr_img, 'DETACHMENT', (100, 1150), font, 7, ORANGE, 20)
            
            if defect == 'AIR PRINT' or air:
                cv2.rectangle(curr_img, (25, 25), (1615, 1207), YELLOW, 50)
                cv2.putText(curr_img, 'AIR PRINT', (100, 1150), font, 8, YELLOW, 20)
        
        elif air:
            cv2.rectangle(curr_img, (25, 25), (1615, 1207), YELLOW, 50)
            cv2.putText(curr_img, 'AIR PRINT', (100, 1150), font, 8, YELLOW, 20)

    out.write(curr_img)

out.release()
log.close()

