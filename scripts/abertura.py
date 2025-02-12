import cv2 
from utils.generalutils import *
from utils.grayutils import blackandwhite, add_black_border, erosao, dilatacao
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

bw_res = cv2.resize(bw, target_size)
cv2.imshow("Combined Image", bw_res)
cv2.waitKey(0)
cv2.destroyAllWindows()


border_img = add_black_border(bw,3)


erodedimg = erosao(border_img, 3, 2, True)

cv2.imshow("Combined Image", erodedimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

dilatedimg = dilatacao(erodedimg, 3, 2, True)

dilatedimg_res = cv2.resize(dilatedimg, target_size)

top_row = cv2.hconcat([bw_res, dilatedimg_res])

combined_image = cv2.vconcat([top_row])


cv2.imshow("Combined Image", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Done.")