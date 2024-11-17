import cv2 
import os
import numpy as np
import matplotlib.pyplot as plt

def select_imagem():

    dicttypes = {
        
        "1": ".jpg",
        "2": ".png",
        "3": ".jpeg"
        
        
        }


    nomeimagem = input("Nome da imagem: ")

    tipoimagem  = input("1 -> jpg, 2 -> png, 3 -> jpeg: ")

    filetype = dicttypes[tipoimagem]

    nomeimagem = '/Users/regin/OneDrive/Documentos/Nova pasta/images/'+nomeimagem+filetype


    access = os.path.exists(nomeimagem)


    while(access == False):
        nomeimagem = input("Nome da imagem: ")
        tipoimagem  = input("1 -> jpg, 2 -> png, 3 -> jpeg")


        filetype = dicttypes[tipoimagem]
        nomeimagem = 'images/'+nomeimagem+filetype
        
        access = os.path.exists(nomeimagem)

    return nomeimagem

def split_colors(imagem):
    
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