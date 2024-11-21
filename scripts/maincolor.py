
import cv2 
from utils.generalutils import *
from utils.graphutils import calcHists
from utils.colorutils import make_blue, make_red, make_green



nomeimagem = select_imagem()    
    
imagem = cv2.imread(nomeimagem)


print("lenght: ")

print(imagem.shape[1])

print("height: ")
print(imagem.shape[0])


print("Channels: ")
print(imagem.shape[2])
        
gray, blue, green, red = split_colors(imagem)


pick_color = int(input("Escolha a cor para tingir a imagem 1-azul, 2-verde, 3-vermelho: "))
choice = int(input("Escolha a itensidade 1, 2 ou 3: "))

if(pick_color ==1):
    new_img = make_blue(imagem, blue, green, red, choice)

if(pick_color ==2):
    new_img = make_green(imagem, blue, green, red, choice)

if(pick_color ==3):
    new_img = make_red(imagem, blue, green, red, choice)

cv2.imshow("Combined", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
