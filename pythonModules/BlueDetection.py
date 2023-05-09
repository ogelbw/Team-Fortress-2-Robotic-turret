import cv2


def getLargestBlueCenter(image:cv2.Mat, Threshold:int, debug:bool = False) -> tuple[int,int] : 
    blue = image.copy()
    blue[:, :, 2] = 0
    blue[:, :, 1] = 0

    #bgra
    low = (0,0,0,0)
    high = (255, Threshold, Threshold, 255)
    threshold = cv2.inRange(image, low, high)

    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    q = []

    for c in contours:
        #finding center of moment
        q.append((cv2.contourArea(c), c))
        m = cv2.moments(c)
        x = int(m["m10"]/(m["m00"]+1e-5))
        y = int(m["m01"]/(m["m00"]+1e-5))

        if debug:
            cv2.line(original, (x,0), (x,threshold.shape[0]), (0,70,160), thickness=3)
            cv2.line(original, (0,y), (threshold.shape[1],y), (0,70,160), thickness=3)

    contours = None

    # sort by the size of the contor
    q.sort(key=lambda e: e[0], reverse=True)
    c = q[0][1]


    m = cv2.moments(c)

    x = int(m["m10"]/(m["m00"]+1e-5))
    y = int(m["m01"]/(m["m00"]+1e-5))


    if debug:
        cv2.line(original, (x,0), (x,threshold.shape[0]), (0,255,0), thickness=3)
        cv2.line(original, (0,y), (threshold.shape[1],y), (0,255,0), thickness=3)
        print(f"Area {q[0][0]}")
        cv2.drawContours(original, c, -1, (0,255,0), 5)

        cv2.imshow("Original image", original)
        cv2.imshow("Blue image", blue)
        cv2.imshow("Threshold image", threshold)

    return (x,y)

if __name__ == "__main__":
    import os
    Threshold = 90

    for file in os.listdir(r"C:\Users\jed39\Documents\Team-Fortress-2-Robotic-turret\python code modules\test images"):
        original = cv2.imread(os.path.join(r"C:\Users\jed39\Documents\Team-Fortress-2-Robotic-turret\python code modules\test images", file), cv2.IMREAD_UNCHANGED)
        getLargestBlueCenter(original, Threshold, True)
        cv2.waitKey(0)

