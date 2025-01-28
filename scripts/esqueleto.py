import cv2 
from utils.generalutils import *
from utils.grayutils import blackandwhite, add_black_border, erosao, dilatacao, differ, combine, invert_img, esqueleto
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



notempty = True
i = 0

inverted = False
border_img = bw


if(inverted):
    newdifferimg = np.ones( (bw.shape[0], bw.shape[1]), dtype = np.uint8)
    newdifferimg = newdifferimg*255
else:
    newdifferimg = np.zeros( (bw.shape[0], bw.shape[1]), dtype = np.uint8)

differimg = newdifferimg


while(notempty):

    
    erodedimg = erosao(bw, 3, i, True, inverted)

    print("lenght: ")

    print(erodedimg.shape[1])

    print("height: ")
    print(erodedimg.shape[0])



    openimg = erosao(erodedimg, 3, 1, True, inverted)

    print("hey hey hey")

    print("lenght: ")

    print(openimg.shape[1])

    print("height: ")
    print(openimg.shape[0])



    dilatedimg = dilatacao(openimg, 3, 1, True, inverted)

    print("hey hey hey")


    print("lenght: ")

    print(dilatedimg.shape[1])

    print("height: ")
    print(dilatedimg.shape[0])

    if(inverted):
        value_to_check = 255
    else:
        value_to_check = 0

    # Check if all values are equal to the specific value
    if np.all(dilatedimg == value_to_check):
        notempty = False

    newdifferimg = differ(erodedimg, dilatedimg, inverted)

    

    differimg = combine(differimg, newdifferimg, inverted)
    
    cv2.imshow("Combined Image", differimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    

    i+=1


esqueletoimg = esqueleto(bw, differimg, inverted)
    



cv2.imshow("Combined Image", esqueletoimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Done.")
