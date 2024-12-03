import cv2 
import os
import numpy as np
import matplotlib.pyplot as plt


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
    plt.suptitle('Grey Dataset')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    # Blue dataset

    # Adjust layout for better appearance
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

def compareplotGrayOnly(base, gray_hist, normalized_hist):
    

    fig, axs = plt.subplots(2, 1, figsize=(12, 10))
    fig.suptitle('Different Datasets Histograms', fontsize=16)

    axs[0].bar(base, gray_hist, color='g')
    axs[0].set_title('F1')
    axs[0].set_xlabel('X')
    axs[0].set_ylabel('y')

    # Blue dataset
    axs[1].bar(base, normalized_hist, color='g')
    axs[1].set_title('F2')
    axs[1].set_xlabel('X')
    axs[1].set_ylabel('Y')

    # Adjust layout for better appearance
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

def compareplotGrayOnlyThree(base, gray_hist, normalized_hist, normalized_hist_og):
    

    fig, axs = plt.subplots(3, 1, figsize=(12, 10))
    fig.suptitle('Different Datasets Histograms', fontsize=16)

    axs[0].bar(base, gray_hist, color='g')
    axs[0].set_title('F1')
    axs[0].set_xlabel('X')
    axs[0].set_ylabel('y')

    # Blue dataset
    axs[1].bar(base, normalized_hist, color='g')
    axs[1].set_title('F2')
    axs[1].set_xlabel('X')
    axs[1].set_ylabel('Y')

    # Blue dataset
    axs[2].bar(base, normalized_hist_og, color='g')
    axs[2].set_title('F3')
    axs[2].set_xlabel('X')
    axs[2].set_ylabel('Y')

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


def generatehist():

    base = [0]*256
    frequency = [0] * 256

    summary = (1/128)/128

    choice = int(input("1- aumentar contraste / 2 - reduzir contraste: "))

    for i in range(256):
            
            base[i] = i


    if(choice == 1):

        value = 0

        for b in range(256):
            
            if(b<128):
                
                frequency[b] = value
                value = value + summary

            else:
                frequency[b] = value
                value = value - summary

    else:

        value = 1/128

        for b in range(256):
            
            if(b<128):
                
                frequency[b] = value
                value = value - summary

            else:
                frequency[b] = value
                value = value + summary


    plt.bar(base, frequency, color='grey')
    plt.show()

    accumulated_hist = [0]*256
    acc = 0

    
    for j in range(256):
        acc = frequency[j] + acc
        accumulated_hist[j] = acc

    plt.bar(base, accumulated_hist, color='grey')
    plt.show()
        
    return frequency, accumulated_hist
