import os
import cv2
import numpy as np


if __name__ == '__main__':
    originPath = r"C:\"
    resultPath = r"C:\"

    files = os.listdir(originPath)
    angles = [90, 180, 270]

    for filename in files:
        print(filename)
        img = cv2.imread(originPath + "\\" + filename)

        h, w = img.shape[:2]
        # print(h, w)
        padding = abs(w - h) // 2
        center = (max(w, h) // 2, max(w, h) // 2)

        img_padded = np.zeros(shape=(max(w, h), max(w, h), 3), dtype=np.uint8)

        if h > w:
            img_padded[:, padding:padding + w, :] = img
        else:
            img_padded[padding:padding + h, :, :] = img



        for angle in angles:
            if angle == 180:
                output = np.rot90(img, 2)
            else:
                M = cv2.getRotationMatrix2D(center, angle, 1)
                rotated_padded = cv2.warpAffine(img_padded, M, (max(w, h), max(w, h)))
                if h > w:
                    output = rotated_padded[padding:padding + w, :, :]
                else:
                    output = rotated_padded[:, padding:padding + h, :]

            cv2.imwrite(resultPath + "\\" + filename.rstrip(".jpg") + "_" + str(angle) + ".jpg", output)