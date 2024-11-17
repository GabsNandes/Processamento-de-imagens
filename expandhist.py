
import cv2 
from utils.generalutils import *
from utils.graphutils import calcHists, plotGrayOnly, exphis


nomeimagem = select_imagem()    
    
imagem = cv2.imread(nomeimagem)


print("lenght: ")

print(imagem.shape[1])

print("height: ")
print(imagem.shape[0])


print("Channels: ")
print(imagem.shape[2])
        
gray, blue, green, red = split_colors(imagem)

base, data, _, _, _ = calcHists(gray, blue, green, red, imagem)

plotGrayOnly(base, data)

expandedimage = exphis(imagem, gray)


cv2.imshow("Expanded", expandedimage)

cv2.waitKey(0)
cv2.destroyAllWindows()



cv2.imwrite("out.jpg", imagem)