
import cv2 
from utils.generalutils import *
from utils.grayutils import add_black_border, convolucao
from utils.graphutils import calcHists, plotGrayOnly


nomeimagem = select_imagem()    
    
imagem = cv2.imread(nomeimagem)


print("lenght: ")

print(imagem.shape[1])

print("height: ")
print(imagem.shape[0])


print("Channels: ")
print(imagem.shape[2])

gray, blue, green, red = split_colors(imagem)
        
border_img = add_black_border(gray,3)

print("lenght: ")

print(border_img.shape[1])

print("height: ")
print(border_img.shape[0])




conv_img = convolucao(border_img,3)

base, data, _, _, _ = calcHists(conv_img, blue, green, red, imagem)
plotGrayOnly(base, data)


cv2.imshow("Combined Image", conv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()