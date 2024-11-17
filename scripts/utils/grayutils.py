import cv2 
import os
import numpy as np
import matplotlib.pyplot as plt


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


def normalized_gray(gray, gray_hist):

    normalized_hist = [0]*256
    pixels = (gray.shape[0]*gray.shape[1])

    for i in range(256):
    
        normalized_hist[i] = gray_hist[i]/pixels

    return normalized_hist


def print_gray(gray):
    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):
            print(gray[i,j])



def generate_normalized_img(gray, normalized_hist):

    normalized_img = np.zeros( (gray.shape[0], gray.shape[1]), dtype = np.uint8 )

    gray_level = [0]*256
    accumulated_hist = [0]*256
    acc = 0

    for i in range(256):
        gray_level[i] = i/256
    
    for j in range(256):
        acc = normalized_hist[j] + acc
        accumulated_hist[j] = acc


    
    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):

            current = int(gray[i,j])
            acc_value = accumulated_hist[current]



            for k in range((current-1),256):

                if(k<255):
                    diff = np.abs(acc_value - gray_level[k])
                    nextdiff =  np.abs(acc_value - gray_level[k+1])
                    
                    if(nextdiff>diff):
                        normalized_img[i,j] = k
                        break
                
                else:
                    normalized_img[i,j] = 255
            
    return normalized_img, accumulated_hist