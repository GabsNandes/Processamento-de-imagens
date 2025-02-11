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

    
    for g in range(border_size, img_with_border.shape[0]-border_size):
        for h in range(border_size, img_with_border.shape[1]-border_size):
            img_with_border[g,h] = gray[g-border_size,h-border_size]

    return img_with_border    


import numpy as np

def convolucao(img_border, mask_size=3):
    border_size = mask_size // 2  # Proper padding size

    img_conv = np.zeros((img_border.shape[0] - 2 * border_size, 
                         img_border.shape[1] - 2 * border_size), dtype=np.uint8)


    conv_matrix = np.array([[-1,  0,  1],
                             [-2,  0,  2],
                             [-1,  0,  1]])

    for j in range(border_size, img_border.shape[0] - border_size):
        for k in range(border_size, img_border.shape[1] - border_size):
   
            part = img_border[j - border_size:j + border_size + 1, k - border_size:k + border_size + 1]

            sumol = np.sum(part * conv_matrix)

           
            sumol = np.clip(sumol, 0, 255)

     
            img_conv[j - border_size, k - border_size] = sumol  

    return img_conv

import numpy as np

def erosao(img_border, mask_size, reps, cross, inv):
    
   

    if inv:
        img_border = invert_img(img_border)


    conv_matrix = np.ones((mask_size, mask_size), dtype=np.uint8)
    if cross:
        conv_matrix[0, 0] = conv_matrix[0, -1] = 0
        conv_matrix[-1, 0] = conv_matrix[-1, -1] = 0
    
    # Create the output image
    border_size = mask_size // 2
    img_conv = img_border.copy()
    
    for _ in range(reps):
        padded_img = np.pad(img_conv, pad_width=border_size, mode='constant', constant_values=0)
        output = np.zeros_like(img_conv)
        
        # Perform erosion
        for i in range(border_size, padded_img.shape[0] - border_size):
            for j in range(border_size, padded_img.shape[1] - border_size):
                region = padded_img[i-border_size:i+border_size+1, j-border_size:j+border_size+1]
                if np.array_equal(region * conv_matrix, conv_matrix * 255):
                    output[i-border_size, j-border_size] = 255
                else:
                    output[i-border_size, j-border_size] = 0
        
        img_conv = output

    if inv:
        img_conv = invert_img(img_conv)

    return img_conv



def dilatacao(bwimg, mask_size, reps, cross, inv):
    
    img_conv_returned = bwimg.copy()
    
    
    conv_matrix = np.ones((mask_size, mask_size), dtype=np.uint8)
    
    
    if cross:
        conv_matrix[0, 0] = 0
        conv_matrix[mask_size-1, 0] = 0
        conv_matrix[0, mask_size-1] = 0
        conv_matrix[mask_size-1, mask_size-1] = 0

    
    if inv:
        bwimg = invert_img(bwimg)

   
    for _ in range(reps):
        img_conv = np.zeros_like(bwimg)

        
        for i in range(bwimg.shape[0]):
            for j in range(bwimg.shape[1]):
               
                top = max(0, i - mask_size // 2)
                bottom = min(bwimg.shape[0], i + mask_size // 2 + 1)
                left = max(0, j - mask_size // 2)
                right = min(bwimg.shape[1], j + mask_size // 2 + 1)

                part = bwimg[top:bottom, left:right]

                
                if part.shape[0] < mask_size or part.shape[1] < mask_size:
                    part = np.pad(part, [(0, mask_size - part.shape[0]), (0, mask_size - part.shape[1])], mode='constant', constant_values=0)

                multmatrix = part * conv_matrix


                if np.any(multmatrix == 255):
                    img_conv[i, j] = 255
                else:
                    img_conv[i, j] = 0

        
        img_conv_returned = img_conv

    
    if inv and reps>0:
        img_conv_returned = invert_img(img_conv_returned)

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

def subtracao(bw, og):

    img_sub = np.zeros( (bw.shape[0], bw.shape[1]), dtype = np.uint8)





    for i in range(img_sub.shape[0]):
        for j in range(img_sub.shape[1]):

             

            diff = np.abs(bw[i, j] - og[i, j])


            if(diff==0):
                img_sub[i,j] = 255
            else:
                img_sub[i,j] = 0
                
        
    return img_sub


def equals (img1, img2):


    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):

            if img1[i,j]!=img2[i,j]:
                return False
            
    
    return True

def inter (img1, img2):
    
    interimg = np.ones( (img1.shape[0], img1.shape[1]), dtype = np.uint8)
    interimg = interimg*255

    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):

            if img1[i,j]==img2[i,j]:
                interimg[i,j] = img1[i,j]
            
            
    
    return interimg


def differ (img1, img2, inverted):

    if(inverted):
    
        interimg = np.ones( (img1.shape[0], img1.shape[1]), dtype = np.uint8)
        interimg = interimg*255
        differvalue = 0
        background = 255

    else:

        interimg = np.zeros( (img1.shape[0], img1.shape[1]), dtype = np.uint8)
        differvalue = 255
        background = 0



    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):

            if img1[i,j]==img2[i,j]:
                interimg[i,j] = background
            else:
                interimg[i,j] = differvalue
                

            
            
    
    return interimg


def combine(img1, img2, inv):

    if(inv==False):
       img1 = invert_img(img1)
       img2 = invert_img(img2)


    img1 = img1/255
    img2 = img2/255

    imgcomb = img1 * img2

    imgcomb = imgcomb*255

    if(inv==False):
       imgcomb = invert_img(imgcomb)

    return imgcomb


def esqueleto(img1, img2, inverted):

    img2 = invert_img(img2)
    if(inverted):
        value = 255
    else:
        value = 0

    interimg = img1

    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):

            if img2[i,j]== value:
                img1[i,j] = value

    
    return img1 

def filtro(img_border, mask_size):

    
    part =  np.zeros( (mask_size, mask_size), dtype = int )
    bordr = mask_size -1

    border_size = int(bordr/2)


    img_conv = np.zeros( (img_border.shape[0]-border_size, img_border.shape[1]-border_size), dtype = np.uint8)


    conv_matrix =  np.ones( (mask_size, mask_size), dtype = np.uint8)

    pixel = 1

    cut1 = 0
    cut2 = 0
    last_part1 = mask_size
    last_part2 = mask_size

    for j in range(border_size, (img_border.shape[0]-border_size)):
        for k in range(border_size, (img_border.shape[1]-border_size)):

            
            part = (img_border[cut1:last_part1,cut2:last_part2])*conv_matrix

            sumol = part.sum()/(part.shape[0]*part.shape[1])
        

            img_conv[j-border_size,k-border_size] = sumol
            
            
            cut2 +=1
            last_part2+=1
            
        cut2=0
        last_part2=mask_size


        
        cut1 +=1
        last_part1+=1
            


    return img_conv

def ruido(img_border, mask_size):

    
    part =  np.zeros( (mask_size, mask_size), dtype = int )
    bordr = mask_size -1

    border_size = int(bordr/2)


    img_conv = np.zeros( (img_border.shape[0]-border_size, img_border.shape[1]-border_size), dtype = np.uint8)


    conv_matrix =  np.ones( (mask_size, mask_size), dtype = np.uint8)

    pixel = 1

    cut1 = 0
    cut2 = 0
    last_part1 = mask_size
    last_part2 = mask_size

    for j in range(border_size, (img_border.shape[0]-border_size)):
        for k in range(border_size, (img_border.shape[1]-border_size)):

            
            part = (img_border[cut1:last_part1,cut2:last_part2])*conv_matrix

            sumol = np.median(part)
        

            img_conv[j-border_size,k-border_size] = sumol
            
            
            cut2 +=1
            last_part2+=1
            
        cut2=0
        last_part2=mask_size


        
        cut1 +=1
        last_part1+=1
            


    return img_conv

import statistics as st

def moda(img_border, mask_size):

    
    part =  np.zeros( (mask_size, mask_size), dtype = int )
    bordr = mask_size -1

    border_size = int(bordr/2)


    img_conv = np.zeros( (img_border.shape[0]-border_size, img_border.shape[1]-border_size), dtype = np.uint8)


    conv_matrix =  np.ones( (mask_size, mask_size), dtype = np.uint8)

    pixel = 1

    cut1 = 0
    cut2 = 0
    last_part1 = mask_size
    last_part2 = mask_size

    for j in range(border_size, (img_border.shape[0]-border_size)):
        for k in range(border_size, (img_border.shape[1]-border_size)):

            
            part = (img_border[cut1:last_part1,cut2:last_part2])*conv_matrix

            values, counts = np.unique(part, return_counts=True)
            mode_value = values[np.argmax(counts)]
        

            img_conv[j-border_size,k-border_size] = mode_value
            
            
            cut2 +=1
            last_part2+=1
            
        cut2=0
        last_part2=mask_size


        
        cut1 +=1
        last_part1+=1
            


    return img_conv


import numpy as np

def order(img_border, mask_size):
    border_size = mask_size // 2 

    img_conv = np.zeros((img_border.shape[0] - 2 * border_size, 
                         img_border.shape[1] - 2 * border_size), dtype=np.uint8)

    conv_matrix = np.ones((mask_size, mask_size), dtype=np.uint8)

    for j in range(border_size, img_border.shape[0] - border_size):
        for k in range(border_size, img_border.shape[1] - border_size):
 
            part = img_border[j - border_size:j + border_size + 1, k - border_size:k + border_size + 1]


            part = np.sort(part, axis=0)

            img_conv[j - border_size, k - border_size] = part[0,0]

    return img_conv



def filter_test(img_border, operator):
    
    if(operator == "sobel"):
        
        conv_matrix = np.array([[-1,  -2,  1],
                             [0,  0,  0],
                             [1,  2,  1]])
        
        mask_size = 3
        loop = 2 
        border_size = mask_size // 2
        adder = 1
        
    if(operator == "prewitt"):

        conv_matrix = np.array([[-1,  -1,  -1],
                             [0,  0,  0],
                             [1,  1,  1]])
        
        mask_size = 3
        loop = 2 
        border_size = mask_size // 2
        adder = 1


    if(operator == "roberts"):

        conv_matrix = np.array([[1,  0],
                             [0,  -1]])
        
        mask_size = 2
        loop = 2 
        border_size = 1
        adder = 0


    print(conv_matrix)


      # Proper padding size

    img_conv = np.zeros((img_border.shape[0] - 2 * border_size, 
                         img_border.shape[1] - 2 * border_size), dtype=np.uint8)
    
    img_conv = img_border

    


    for l in range(loop):

        print(l+1)

        for j in range(border_size, img_border.shape[0] - border_size):
            for k in range(border_size, img_border.shape[1] - border_size):
    
                part = img_conv[j - border_size:j + border_size + adder, k - border_size:k + border_size + adder]
                
                sumol = np.sum(part * conv_matrix)
                
            
                sumol = np.clip(sumol, 0, 255)

        
                img_conv[j - border_size, k - border_size] = sumol  

        cv2.imshow("Combined Image", img_conv)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if(operator == "sobel"):
            
            conv_matrix = np.array([[-1,  0,  1],
                                [-2,  0,  2],
                                [-1,  0,  1]])
            
            mask_size = 3
            
        if(operator == "prewitt"):

            conv_matrix = np.array([[-1,  0,  1],
                                [-2,  0,  1],
                                [-1,  0,  1]])
            
            mask_size = 3


        if(operator == "roberts"):

            conv_matrix = np.array([[0,  1],
                                [-1,  0]])
            
            mask_size = 2

    return img_conv














            









            













