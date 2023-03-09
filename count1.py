import random
import cv2 as cv
import time
import handTrackingModule as htm
import math
def get_count():
    ctime=ptime=0
    cap=cv.VideoCapture(0)
    detector=htm.HandDetector()
    count=0
    flag=0
    while True:
        try:
            isTrue,frame=cap.read()
            ctime=time.time()
            fps=1/(ctime-ptime)
            ptime=ctime
            frame=cv.flip(frame,1)
            frame=detector.find_hands(frame,draw=True)
            lm_list=detector.find_pos(frame,draw=False)
            try:
                pos_pinky_tip=lm_list[19]
                pos_pinky_knuckle= lm_list[17]
                pos_ring_tip=lm_list[15]
                pos_ring_knuckle=lm_list[13]
                pos_mid_tip=lm_list[11]
                pos_mid_knuckle=lm_list[9]
                pos_index_tip=lm_list[7]
                pos_index_knuckle=lm_list[5]
                pos_thumb_tip=lm_list[4]
                if(math.fabs(pos_pinky_knuckle[2]-pos_pinky_tip[2])>35):
                    count+=1
                if (math.fabs(pos_ring_knuckle[2] - pos_ring_tip[2]) > 35):
                    count+=1
                if (math.fabs(pos_mid_knuckle[2] - pos_mid_tip[2]) > 35):
                    count+=1
                if (math.fabs(pos_index_knuckle[2] - pos_index_tip[2]) > 35):
                    count+=1
                if (math.fabs(pos_ring_knuckle[2] - pos_thumb_tip[2]) > 35):
                    count+=1
                if(count==4):
                    flag+=1
                if ((count == 2 or count == 5 or count == 0) and flag>10):
                    return(count)
                cv.putText(frame,str(count),(30,90),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),2)
                count=0

            except Exception as e:
                flag=0
            cv.putText(frame,str(int(fps)),(10,60),cv.FONT_HERSHEY_PLAIN,1,(0,255,0),2)
            cv.imshow("image",frame)
            if(cv.waitKey(1) & 0xff==ord('q')):
                break
        except Exception as e:
            break

    cap.release()
    cv.destroyAllWindows()

