import cv2 
from utils.generalutils import *
from utils.grayutils import blackandwhite, invert_img, dilatacao, equals, inter, combine
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

current = np.ones( (bw.shape[0], bw.shape[1]), dtype = np.uint8)

current = current *255

last = current.copy()

current[2,7] = 0

plt.imshow(bw, cmap = "gray")
plt.show()

plt.imshow(current, cmap = "gray")
plt.show()




while not equals(last, current):

    last = current.copy()
    current = dilatacao(current, 3, 1, False, True)
    current = inter(current, bw)

    

fig, axs = plt.subplots(2, 1, figsize=(12, 10))
fig.suptitle('Different Datasets Histograms', fontsize=16)

axs[0].imshow(bw, cmap = "gray")
axs[0].set_title('Grey Dataset')


# Blue dataset
axs[1].imshow(current, cmap = "gray")
axs[1].set_title('Blue Dataset')

plt.show()

print("Done.")