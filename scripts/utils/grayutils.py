import cv2 
import os
import numpy as np
import matplotlib.pyplot as plt
from utils.generalutils import adjustpart


def blackandwhite(blackandwhiteimg):

    cutOffPoint = 127

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


def new_gray_level(gray, accumulated):
    normalized_img = np.zeros( (gray.shape[0], gray.shape[1]), dtype = np.uint8 )

    gray_level = [0]*256

    for k in range(256):

        gray_level[k] = round(accumulated[k]*255)
        print(gray_level[k])

    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):

            normalized_img[i,j] = gray_level[gray[i,j]]

            
            
    return normalized_img


def add_black_border(gray, mask_size):

    mask_size-=1

    border_size = int(mask_size/2)

    print("-----",border_size)

    img_with_border = np.zeros( (gray.shape[0]+mask_size, gray.shape[1]+mask_size), dtype = np.uint8 )
    
    for j in range(border_size):
        for i in range(img_with_border.shape[0]):
        
            img_with_border[i,j] = 0

    for k in range(border_size):
        for l in range(img_with_border.shape[1]):
        
            img_with_border[k,l] = 0

    
    for g in range(border_size, img_with_border.shape[0]-border_size):
        for h in range(border_size, img_with_border.shape[1]-border_size):
            img_with_border[g,h] = gray[g-border_size,h-border_size]

    return img_with_border    


def convolucao(img_border, mask_size):

    
    part =  np.zeros( (mask_size, mask_size), dtype = int )
    bordr = mask_size -1

    border_size = int(bordr/2)


    img_conv = np.zeros( (img_border.shape[0]-border_size, img_border.shape[1]-border_size), dtype = np.uint8)


    conv_matrix = np.array([[0,  1, 0],
                            [1, -4, 1],
                            [0,  1, 0]])

    pixel = 1

    cut1 = 0
    cut2 = 0
    last_part1 = mask_size
    last_part2 = mask_size

    for j in range(border_size, (img_border.shape[0]-border_size)):
        for k in range(border_size, (img_border.shape[1]-border_size)):

            
            part = (img_border[cut1:last_part1,cut2:last_part2])*conv_matrix

            sumol = part.sum()
            

            if(sumol>255):
                sumol = 255
            if (sumol<0):
                sumol = 0

            img_conv[j-border_size,k-border_size] = sumol
            
            
            cut2 +=1
            last_part2+=1
            
        cut2=0
        last_part2=mask_size


        
        cut1 +=1
        last_part1+=1
            


    return img_conv


def erosao(img_border, mask_size, reps, cross):

    
    part =  np.zeros( (mask_size, mask_size), dtype = int )
    bordr = mask_size -1

    border_size = int(bordr/2)


    img_conv = np.zeros( (img_border.shape[0]-border_size, img_border.shape[1]-border_size), dtype = np.uint8)


    conv_matrix = np.ones((mask_size, mask_size), dtype = np.uint8)

    if(cross == True):
        

        conv_matrix[0,0] = 0
        conv_matrix[mask_size-1,0] = 0
        conv_matrix[0,mask_size-1] = 0
        conv_matrix[mask_size-1,mask_size-1] = 0

        print(conv_matrix)

        values, counts = np.unique(conv_matrix, return_counts=True)

        print(counts)

        count255 = counts[1]

    equal_matrix = conv_matrix*255

    
    print(conv_matrix)
    print(equal_matrix)

    pixel = 1

    cut1 = 0
    cut2 = 0
    last_part1 = mask_size
    last_part2 = mask_size

    img_conv_returned = img_border

    for i in range(reps):

        cut1 = 0
        cut2 = 0
        last_part1 = mask_size
        last_part2 = mask_size

        print("LOOP", i+1)

        for j in range(border_size, (img_conv_returned.shape[0]-border_size)):
            for k in range(border_size, (img_conv_returned.shape[1]-border_size)):

                

                part = (img_conv_returned[cut1:last_part1,cut2:last_part2])

                multmatrix = (part*conv_matrix)

        
                if((multmatrix == equal_matrix).all()):
                    img_conv[j-border_size,k-border_size] = 255
                else:
                    img_conv[j-border_size,k-border_size] = 0
                
                
                
                
                cut2 +=1
                last_part2+=1
                
            cut2=0
            last_part2=mask_size


            
            cut1 +=1
            last_part1+=1

        img_conv_returned = img_conv
            
    return img_conv_returned


def dilatacao(bwimg, mask_size, reps, cross):

    part =  np.zeros( (mask_size, mask_size), dtype = int )
    bordr = mask_size -1


    img_conv = np.zeros( (bwimg.shape[0], bwimg.shape[1]), dtype = np.uint8)


    conv_matrix = np.ones((mask_size, mask_size), dtype = np.uint8)

    multmatrix = np.zeros( (mask_size, mask_size), dtype = int )

    if(cross == True):
        

        conv_matrix[0,0] = 0
        conv_matrix[mask_size-1,0] = 0
        conv_matrix[0,mask_size-1] = 0
        conv_matrix[mask_size-1,mask_size-1] = 0

        print(conv_matrix)

        values, counts = np.unique(conv_matrix, return_counts=True)

        print(counts)

        count255 = counts[1]

    equal_matrix = conv_matrix*255

    help = np.zeros((1,3), dtype = np.uint8)
    print(help)

    
    print(conv_matrix)
    print(equal_matrix)

    pixel = 1

    cut1 = 0
    cut2 = 0
    last_part1 = mask_size
    last_part2 = mask_size

    img_conv_returned = bwimg

    for i in range(reps):

        cut1 = 0
        cut2 = 0
        last_part1 = mask_size
        last_part2 = mask_size

        print("LOOP", i+1)

        for j in range(0, (img_conv_returned.shape[0])):
            for k in range(0, (img_conv_returned.shape[1])):

                

                part = (bwimg[cut1:last_part1,cut2:last_part2])


                if part.shape[0]<mask_size or part.shape[1]<mask_size:

                    part = adjustpart(part,mask_size)
                

                multmatrix = part * conv_matrix

        
                
                if np.any(multmatrix == 255 ):
                    img_conv[j, k] = 255
                else:
                    img_conv[j, k] = 0
                
                
                
                
                cut2 +=1
                last_part2+=1

            
                
            cut2=0
            last_part2=mask_size


            
            cut1 +=1
            last_part1+=1

        img_conv_returned = img_conv
            
    return img_conv_returned


def erosaohit(img_border, mask_size, reps, inverted):

    
    part =  np.zeros( (mask_size, mask_size), dtype = int )
    bordr = mask_size -1

    border_size = int(bordr/2)


    img_conv = np.zeros( (img_border.shape[0]-bordr, img_border.shape[1]-bordr), dtype = np.uint8)


    if(inverted != True):
        
        conv_matrix = np.ones((mask_size, mask_size), dtype = np.uint8)
        
        conv_matrix[1:bordr, 1:bordr] = 0

        print(conv_matrix)


    else:

        conv_matrix = np.zeros((mask_size, mask_size), dtype = np.uint8)
        
        conv_matrix[1:bordr, 1:bordr] = 1

        print(conv_matrix)


    equal_matrix = conv_matrix*255

    
    print(conv_matrix)
    print(equal_matrix)

    pixel = 1

    cut1 = 0
    cut2 = 0
    last_part1 = mask_size
    last_part2 = mask_size

    img_conv_returned = img_border

    for i in range(reps):

        cut1 = 0
        cut2 = 0
        last_part1 = mask_size
        last_part2 = mask_size

        print("LOOP", i+1)

        for j in range(border_size, (img_conv_returned.shape[0]-border_size)):
            for k in range(border_size, (img_conv_returned.shape[1]-border_size)):

                

                part = (img_conv_returned[cut1:last_part1,cut2:last_part2])

                multmatrix = (part*conv_matrix)

        
                if((multmatrix == equal_matrix).all()):
                    img_conv[j-border_size,k-border_size] = 255
                else:
                    img_conv[j-border_size,k-border_size] = 0
                
                
                
                
                cut2 +=1
                last_part2+=1
                
            cut2=0
            last_part2=mask_size


            
            cut1 +=1
            last_part1+=1

        img_conv_returned = img_conv
            
    return img_conv_returned


def invert_img(bwimg):

    img_inv = np.zeros( (bwimg.shape[0], bwimg.shape[1]), dtype = np.uint8)



    for j in range(0, (bwimg.shape[0])):
            for k in range(0, (bwimg.shape[1])):

                if(bwimg[j,k]==255):
                    img_inv[j,k] = 0
                else:
                    img_inv[j,k] = 255

    
    return img_inv



def hitormiss(bwimg, mask_size):

    border_img = add_black_border(bwimg, 7)

    mask_size -=1

    plt.imshow(border_img, cmap = "gray")
    plt.show()

    hitormissimg = np.zeros( (border_img.shape[0]-mask_size, border_img.shape[1]-mask_size), dtype = np.uint8)



    eros1 = erosaohit(border_img, 7, 1, False)
    eros2 = erosaohit(invert_img(border_img), 7, 1, True)

    eros1 = eros1/255
    eros2 = eros2/255

    hitormissimg = (eros1*eros2)*255


    fig, axs = plt.subplots(2, 3, figsize=(12, 10))
    fig.suptitle('Different Datasets Histograms', fontsize=16)

    axs[0, 0].imshow(bwimg, cmap = "gray")
    axs[0, 0].set_title('Grey Dataset')
    

    # Blue dataset
    axs[1, 0].imshow(invert_img(bwimg), cmap = "gray")
    axs[1, 0].set_title('Blue Dataset')
    

    # Green dataset
    axs[0, 1].imshow(eros1, cmap = "gray")
    axs[0, 1].set_title('Green Dataset')
    

    # Red dataset
    axs[1, 1].imshow(eros2, cmap = "gray")
    axs[1, 1].set_title('Red Dataset')

    axs[1, 2].imshow(hitormissimg, cmap = "gray")
    axs[1, 2].set_title('Red Dataset')
    

    # Adjust layout for better appearance
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

    
    return hitormissimg







            









            













