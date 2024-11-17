
import cv2 
from utils.generalutils import *
from utils.graphutils import calcHists, plotGrayOnly
from utils.colorutils import exphisColor, combine_bgr
from utils.graphutils import plothists


nomeimagem = select_imagem()    
    
imagem = cv2.imread(nomeimagem)


print("lenght: ")

print(imagem.shape[1])

print("height: ")
print(imagem.shape[0])


print("Channels: ")
print(imagem.shape[2])
        
gray, blue, green, red = split_colors(imagem)

base, data, blue_hist, green_hist, red_hist = calcHists(gray, blue, green, red, imagem)

# Original dataset (grey)
plothists(base, blue_hist, green_hist, red_hist, data)


blue_img = exphisColor(blue, 0)
green_img = exphisColor(green, 1)
red_img = exphisColor(red, 2)


new_img = combine_bgr(imagem, blue_img, green_img, red_img)
cv2.imshow("Combined", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()



cv2.imwrite("out.jpg", imagem)