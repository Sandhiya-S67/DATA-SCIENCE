from PIL import Image
import matplotlib.pyplot as plt 

img = Image.open("IMAGE.png")
plt.imshow(img)
plt.show()
