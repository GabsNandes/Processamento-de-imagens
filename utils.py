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

    nomeimagem = nomeimagem+filetype


    access = os.path.exists(nomeimagem)


    while(access == False):
        nomeimagem = input("Nome da imagem: ")
        tipoimagem  = input("1 -> jpg, 2 -> png, 3 -> jpeg")


        filetype = dicttypes[tipoimagem]
        nomeimagem = nomeimagem+filetype
        
        access = os.path.exists(nomeimagem)

    return nomeimagem

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

def plothists(base, blue_hist, green_hist, red_hist, data):
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Different Datasets Histograms', fontsize=16)

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

def plot(f1, f2, f3, gray, neg, parbol):
    fig, axs = plt.subplots(2, 3, figsize=(12, 10))
    fig.suptitle('Different Datasets Histograms', fontsize=16)

    axs[0, 0].plot(gray, f1, color='b', linestyle='-', linewidth=2, markersize=6)
    axs[0, 0].set_title('F1')
    axs[0, 0].set_xlabel('X')
    axs[0, 0].set_ylabel('y')

    # Blue dataset
    axs[0, 1].plot(gray, f2, color='b', linestyle='-', linewidth=2, markersize=6)
    axs[0, 1].set_title('F2')
    axs[0, 1].set_xlabel('X')
    axs[0, 1].set_ylabel('Y')

    # Green dataset
    axs[1, 0].plot(gray, f3, color='b', linestyle='-', linewidth=2, markersize=6)
    axs[1, 0].set_title('F3')
    axs[1, 0].set_xlabel('X')
    axs[1, 0].set_ylabel('Y')

    # Red dataset
    axs[1, 1].plot(gray, gray, color='b', linestyle='-', linewidth=2, markersize=6)
    axs[1, 1].set_title('Original')
    axs[1, 1].set_xlabel('X')
    axs[1, 1].set_ylabel('Y')

    axs[0, 2].plot(neg, neg, color='b', linestyle='-', linewidth=2, markersize=6)
    axs[0, 2].set_title('Negative')
    axs[0, 2].set_xlabel('X')
    axs[0, 2].set_ylabel('Y')

    # Red dataset
    axs[1, 2].plot(gray, parbol, color='b', linestyle='-', linewidth=2, markersize=6)
    axs[1, 2].set_title('Parabolica')
    axs[1, 2].set_xlabel('X')
    axs[1, 2].set_ylabel('Y')

    # Adjust layout for better appearance
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

def plotGrayOnly(base, data):
    

    plt.bar(base, data, color='grey')
    plt.plot(base, data, color='blue', marker='o', linestyle='-', label='Line Graph')
    plt.suptitle('Grey Dataset')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    # Blue dataset

    # Adjust layout for better appearance
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

def detectvaley(base, data):

    plt.bar(base, data, color='grey')
    plt.plot(base, data, color='blue', linestyle='-', label='Line Graph')
    plt.suptitle('Grey Dataset')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    # Blue dataset

    # Adjust layout for better appearance
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()


def blackandwhite(blackandwhiteimg):

    cutOffPoint = int(input("Inisra ponto de corte: "))

    for i in range(blackandwhiteimg.shape[0]):
        for j in range(blackandwhiteimg.shape[1]):
            
            value = blackandwhiteimg[i,j]

            if value>cutOffPoint:
                blackandwhiteimg[i,j] = 255
            else:
                blackandwhiteimg[i,j] = 0
    
    return blackandwhiteimg

def erase(gray):

    eraseWho = int(input("Quem Voce quer apagar 1-(255), 2-(0), 3-(Three Cuts)"))

    if (eraseWho == 1):
        cutOffPoint = int(input("Inisra ponto de corte: "))
        erased255 = eraserFunc255(gray, cutOffPoint) 
        cv2.imshow("erased255", erased255) 

    if(eraseWho == 2):
        cutOffPoint = int(input("Inisra ponto de corte: "))
        erased0 = eraserFunc0(gray, cutOffPoint)
        cv2.imshow("erased0", erased0) 

    if(eraseWho == 3):
        cutOffPoint1 = int(input("Inisra ponto de corte: "))
        cutOffPoint2 = int(input("Inisra ponto de corte: "))
        eraseT = eraseThree(gray, cutOffPoint1, cutOffPoint2)
        cv2.imshow("erasedT", eraseT) 




def eraserFunc255(erased255, cutOffPoint):
    
    for i in range(erased255.shape[0]):
        for j in range(erased255.shape[1]):

            value = erased255[i,j]            
            if value>cutOffPoint:
                erased255[i,j] = 255
    
    return erased255

def eraserFunc0(erased0, cutOffPoint):
    
    for i in range(erased0.shape[0]):
        for j in range(erased0.shape[1]):

            value = erased0[i,j]            
            if value<cutOffPoint:
                erased0[i,j] = 0
            
    return erased0

def eraseThree(erasedT, cutOffPoint1, cutOffPoint2):
    for i in range(erasedT.shape[0]):
        for j in range(erasedT.shape[1]):

            value = erasedT[i,j]            
            if cutOffPoint1<value<cutOffPoint2:
                erasedT[i,j] = value
            else:
                erasedT[i,j] = 255
                
            
    return erasedT


def contraste(imagem, gray):

    f1 =  np.zeros( (imagem.shape[0], imagem.shape[1]), dtype = np.uint8 )
    f2 =  np.zeros( (imagem.shape[0], imagem.shape[1]), dtype = np.uint8 )
    f3 =  np.zeros( (imagem.shape[0], imagem.shape[1]), dtype = np.uint8 )

    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):

            f1[i,j] = gray[i,j]
            
            if(gray[i,j]*2>255):
                f2[i,j] = 255
            else:
                f2[i,j] = gray[i,j]*2

            if(gray[i,j]+100>255):
                f3[i,j] = 255
            else:
                f3[i,j] = gray[i,j]+100

    return f1, f2, f3


def negativo(imagem, gray):
    negativo =  np.zeros( (imagem.shape[0], imagem.shape[1]), dtype = np.uint8 )

    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):

            negativo[i,j] = np.abs(gray[i,j]-255)

    return negativo


def parboltone(imagem, gray):
    parbol =  np.zeros( (imagem.shape[0], imagem.shape[1]), dtype = np.uint8 )

    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):

            parbol[i,j] = ((((1/256)*gray[i,j]))**2)*255

    return parbol


def exphis(imagem, gray):
    expanded =  np.zeros( (imagem.shape[0], imagem.shape[1]), dtype = np.uint8 )

    r1 = int(input("r1: "))
    r2 = int(input("r2: "))

    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):

            if(gray[i,j]<=r1):
                expanded[i,j] = 0
            if(gray[i,j]>=r2):
                expanded[i,j]=255
            else:
                expanded[i,j] = 255*np.abs((gray[i,j]-r1)/(r2-r1))


    return expanded


