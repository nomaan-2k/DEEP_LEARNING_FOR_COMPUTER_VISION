from PIL import Image
import numpy as np
img_w, img_h = 200, 200
data = np.zeros((img_h, img_w, 3), dtype=np.uint8)
for i in range (50,81):
    for j in range(50,81):
        data[j, i] = [255, 255, 255]
        data[j, 200-i] = [255, 255, 255]

for k in range(150,161):
    for z in range(60,140):
        data[k, z] = [255, 255, 255]
img = Image.fromarray(data, 'RGB')
img.save('test.png')
img.show() 