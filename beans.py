import cv2 
from utils import *

nomeimagem = select_imagem()    
    
imagem = cv2.imread(nomeimagem)


print("lenght: ")

print(imagem.shape[1])

print("height: ")
print(imagem.shape[0])


print("Channels: ")
print(imagem.shape[2])
        
gray, blue, green, red = grayFunction(imagem)

base, data, _, _, _ = calcHists(gray, blue, green, red, imagem)

plotGrayOnly(base, data)

blackwhiteimg = blackandwhite(gray, 116)

cv2.imshow("Blackandwhite", blackwhiteimg)

cv2.waitKey(0)
cv2.destroyAllWindows()



cv2.imwrite("out.jpg", imagem)