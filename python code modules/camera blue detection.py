import cv2
import os

for file in os.listdir(r"C:\Users\jed39\Documents\Team-Fortress-2-Robotic-turret\python code modules\test images"):
    original = cv2.imread(os.path.join(r"C:\Users\jed39\Documents\Team-Fortress-2-Robotic-turret\python code modules\test images", file), cv2.IMREAD_UNCHANGED)

    blue = original.copy()
    blue[:, :, 2] = 0
    blue[:, :, 1] = 0

    red = original.copy()
    red[:, :, 0] = 0
    red[:, :, 1] = 0

    green = original.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0



    #bgra
    low = (0,0,0,0)
    high = (255,100,100,255)
    threshold = cv2.inRange(original, low, high)

    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # m = [None]*len(contours)
    # for i in range(len(contours)):
    #     m[i] = cv2.moments(contours[i])
    q = []

    for c in contours:
        q.append((cv2.contourArea(c), c))
        m = cv2.moments(c)
        #finding center of moment
        x = int(m["m10"]/(m["m00"]+1e-5))
        y = int(m["m01"]/(m["m00"]+1e-5))
        cv2.line(original, (x,0), (x,threshold.shape[0]), (0,70,160), thickness=3)
        cv2.line(original, (0,y), (threshold.shape[1],y), (0,70,160), thickness=3)

    contours = None

    q.sort(key=lambda e: e[0], reverse=True)
    c = q[0][1]


    m = cv2.moments(c)

    x = int(m["m10"]/(m["m00"]+1e-5))
    y = int(m["m01"]/(m["m00"]+1e-5))

    cv2.line(original, (x,0), (x,threshold.shape[0]), (0,255,0), thickness=3)
    cv2.line(original, (0,y), (threshold.shape[1],y), (0,255,0), thickness=3)
    print(f"Area {q[0][0]}")

    cv2.imshow("Original image", original)
    cv2.imshow("Red image", red)
    cv2.imshow("Green image", green)
    cv2.imshow("Blue image", blue)
    cv2.imshow("Threshold image", threshold)
    cv2.waitKey(0)
