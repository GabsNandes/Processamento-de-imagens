
import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import glob

def select_imagem():

    basepath =  Path(__file__).resolve().parent.parent.parent
    
    basepath = basepath /'images'

    os.chdir(basepath)

    python_files = glob.glob("*")


    file_num = 0
    running = True


    while running:
        file_num = 0
        for file in python_files:

            print(file_num,"-",file)
            file_num+=1


        file_choice=int(input("Pick number to select a file,"))

        if(file_choice>=len(python_files)):
            print("Inavlid file....")
            running = False
        else:
            nomeimagem = basepath/python_files[file_choice]

        return str(nomeimagem)

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