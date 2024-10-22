# -*- coding: utf-8 -*-


import cv2 
import os
import numpy as np
import matplotlib.pyplot as plt

def grayFunction(imagem):
    
    blue = np.zeros((imagem.shape[0],imagem.shape[1],imagem.shape[2]), dtype = np.uint8)
    green = np.zeros((imagem.shape[0],imagem.shape[1],imagem.shape[2]), dtype = np.uint8)
    red = np.zeros((imagem.shape[0],imagem.shape[1],imagem.shape[2]), dtype = np.uint8)

    gray =  np.zeros( (imagem.shape[0], imagem.shape[1]), dtype = np.uint8 )

    blue[:,:,0] = imagem[:,:,0]
    green[:,:,1] = imagem[:,:,1]
    red[:,:,2] = imagem[:,:,2]

    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            gray[i,j] = blue[i,j,0]/3 + green[i,j,1]/3 + red[i,j,2]/3

            
    return gray, blue, green, red

def calcHists(gray, blue, green, red, imagem):
    arr0 = [0] * 256
    base = [0] * 256


    for b in range(256):
        base[b] = b
        
    for i in gray:
        for j in i:
            arr0[j] += 1
    data = arr0

    blue_hist= [0] * 256
    green_hist = [0] * 256
    red_hist = [0] * 256

    for i in range(imagem.shape[0]):
            for j in range(imagem.shape[1]):
                blue_hist[blue[i,j,0]] += 1
                green_hist[green[i,j,1]] += 1
                red_hist[red[i,j,2]] += 1

    return base, data, blue_hist, green_hist, red_hist

def plot(base, blue_hist, green_hist, red_hist, data):
    axs[0, 0].bar(base, data, color='grey')
    axs[0, 0].set_title('Grey Dataset')
    axs[0, 0].set_xlabel('Values')
    axs[0, 0].set_ylabel('Frequency')

    # Blue dataset
    axs[0, 1].bar(base, blue_hist, color='blue')
    axs[0, 1].set_title('Blue Dataset')
    axs[0, 1].set_xlabel('Values')
    axs[0, 1].set_ylabel('Frequency')

    # Green dataset
    axs[1, 0].bar(base, green_hist, color='green')
    axs[1, 0].set_title('Green Dataset')
    axs[1, 0].set_xlabel('Values')
    axs[1, 0].set_ylabel('Frequency')

    # Red dataset
    axs[1, 1].bar(base, red_hist, color='red')
    axs[1, 1].set_title('Red Dataset')
    axs[1, 1].set_xlabel('Values')
    axs[1, 1].set_ylabel('Frequency')

    # Adjust layout for better appearance
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()
        



dicttypes = {
    
    "1": ".jpg",
    "2": ".png",
    "3": ".jpeg"
    
    
    }


nomeimagem = input("Nome da imagem: ")

tipoimagem  = input("1 -> jpg, 2 -> png, 3 -> jpeg: ")

filetype = dicttypes[tipoimagem]

nomeimagem = nomeimagem+filetype


access = os.path.exists(nomeimagem)


while(access == False):
    nomeimagem = input("Nome da imagem: ")
    tipoimagem  = input("1 -> jpg, 2 -> png, 3 -> jpeg")


    filetype = dicttypes[tipoimagem]
    nomeimagem = nomeimagem+filetype
    
    access = os.path.exists(nomeimagem)
    
    
imagem = cv2.imread(nomeimagem)


print("lenght: ")

print(imagem.shape[1])

print("height: ")
print(imagem.shape[0])


print("Channels: ")
print(imagem.shape[2])
        
gray, blue, green, red = grayFunction(imagem)

target_size = (200, 200)  # Adjust this size as needed

# Resize each image to the target size
imagem_resized = cv2.resize(imagem, target_size)
blue_resized = cv2.resize(blue, target_size)
green_resized = cv2.resize(green, target_size)
red_resized = cv2.resize(red, target_size)
gray_resized = cv2.resize(gray, target_size)

# Stack images horizontally in pairs and then vertically to form a single image
top_row = cv2.hconcat([imagem_resized, blue_resized])
bottom_row = cv2.hconcat([green_resized, red_resized])
combined_image = cv2.vconcat([top_row, bottom_row])

# Display the combined image
cv2.imshow("Combined Image", combined_image)
cv2.imshow("gray", gray_resized)


# Repeating the process with a modified arrangement to match the request.



fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Different Datasets Histograms', fontsize=16)

# Plotting the histograms separately

base, data, blue_hist, green_hist, red_hist = calcHists(gray, blue, green, red, imagem)

# Original dataset (grey)
plot(base, blue_hist, green_hist, red_hist, data)



cv2.waitKey(0)
cv2.destroyAllWindows()



cv2.imwrite("out.jpg", imagem)

