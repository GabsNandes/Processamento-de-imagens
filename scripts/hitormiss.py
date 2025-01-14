import cv2 
from utils.generalutils import *
from utils.grayutils import blackandwhite, hitormiss, invert_img
from utils.graphutils import singleHists, plotGrayOnly

nomeimagem = select_imagem()    
    
imagem = cv2.imread(nomeimagem)


print("lenght: ")

print(imagem.shape[1])

print("height: ")
print(imagem.shape[0])


print("Channels: ")
print(imagem.shape[2])
        
gray, blue, green, red = split_colors(imagem)

#blackwhiteimg = blackandwhite(gray)

#cv2.imshow("Blackandwhite", blackwhiteimg)

bw = blackandwhite(gray)



base, data = singleHists(bw)


target_size = (200, 200)

hitormiss(bw, 5)


print("Done.")