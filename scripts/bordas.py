import cv2 
from utils.generalutils import *
from utils.grayutils import blackandwhite, add_black_border, erosao, subtracao
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


border_img = add_black_border(bw,3)

plt.imshow(bw, cmap = "gray")
plt.show()


erodedimg = erosao(border_img, 5, 2, True, True)



plt.imshow(border_img, cmap = "gray")
plt.show()

plt.imshow(erodedimg, cmap = "gray")
plt.show()

print("lenght: ")

print(erodedimg.shape[1])

print("height: ")
print(erodedimg.shape[0])


subimg = subtracao(erodedimg, bw)


fig, axs = plt.subplots(2, 1, figsize=(12, 10))
fig.suptitle('Different Datasets Histograms', fontsize=16)

axs[0].imshow(bw, cmap = "gray")
axs[0].set_title('Grey Dataset')


# Blue dataset
axs[1].imshow(subimg, cmap = "gray")
axs[1].set_title('Blue Dataset')

plt.show()

print("Done.")