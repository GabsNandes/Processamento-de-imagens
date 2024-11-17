import cv2 
import os
import numpy as np
import matplotlib.pyplot as plt

def combine_bgr(imagem, blue, green, red):
    new_img = np.zeros((imagem.shape[0],imagem.shape[1],imagem.shape[2]), dtype = np.uint8)

    new_img[:,:,0] = blue[:,:,0]
    new_img[:,:,1] = green[:,:,1]
    new_img[:,:,2] = red[:,:,2]

    return new_img

def normalized_color(gray, color_hist):

    normalized_hist = [0]*256
    pixels = (gray.shape[0]*gray.shape[1])

    for i in range(256):
    
        normalized_hist[i] = color_hist[i]/pixels

    return normalized_hist



def generate_normalized_colored_img(imagem, normalized_hist, pos):

    normalized_img = np.zeros((imagem.shape[0],imagem.shape[1],imagem.shape[2]), dtype = np.uint8)

    gray_level = [0]*256
    accumulated_hist = [0]*256
    acc = 0

    for i in range(256):
        gray_level[i] = i/256
    
    for j in range(256):
        acc = normalized_hist[j] + acc
        accumulated_hist[j] = acc


    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):

            current = int(imagem[i,j, pos])
            acc_value = accumulated_hist[current]



            for k in range((current-1),256):

                if(k<255):
                    diff = np.abs(acc_value - gray_level[k])
                    nextdiff =  np.abs(acc_value - gray_level[k+1])
                    
                    if(nextdiff>diff):
                        normalized_img[i,j, pos] = k
                        break
                
                else:
                    normalized_img[i,j, pos] = 255
            
    return normalized_img, accumulated_hist

def negative_color(color, index):

    neg_color = np.zeros((color.shape[0],color.shape[1],color.shape[2]), dtype = np.uint8)


    for i in range(color.shape[0]):
        for j in range(color.shape[1]):

            neg_color[i,j, index] = np.abs(color[i,j,index] - 255)


    return neg_color


