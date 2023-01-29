import os
import cv2
import numpy as np

def get_image(name, url):
    if not os.path.exists(name):
        os.mkdir(name)
    for i in range(32):
        for j in range(32):
            if os.path.exists(os.path.join(os.getcwd(), name, f"{i}_{j}.jpeg")):
                continue
            img_whl = []
            for a in range(16):
                img_col = []
                for b in range(16):
                    print(16*i+a, 16*j+b)
                    try:
                        os.system(f"curl {url}/{16*i+a}/{16*j+b} -o {16*i+a}_{16*j+b}.jpeg -f")
                    except:
                        pass
                    if os.path.exists(f"{16*i+a}_{16*j+b}.jpeg"):
                        img_col.append(cv2.imread(f"{16*i+a}_{16*j+b}.jpeg"))
                        os.remove(f"{16*i+a}_{16*j+b}.jpeg")
                    else:
                        img_col.append(np.full((256, 256, 3), 255))
                img_whl.append(np.concatenate(img_col, axis=0))
            image = np.concatenate(img_whl, axis=1)
            cv2.imwrite(os.path.join(os.getcwd(), name, f"{i}_{j}.jpeg"), image)
