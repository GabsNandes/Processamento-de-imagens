import cv2
from utils.generalutils import *
from utils.graphutils import generatehist, calcHists, compareplotGrayOnly, compareplotGrayOnlyThree
from utils.grayutils import new_gray_level, normalized_gray, generate_normalized_img

nomeimagem = select_imagem()    
    
imagem = cv2.imread(nomeimagem)


print("lenght: ")

print(imagem.shape[1])

print("height: ")
print(imagem.shape[0])


print("Channels: ")
print(imagem.shape[2])
        
gray, blue, green, red = split_colors(imagem)


frequency, accumulated_hist = generatehist()

base, data, _, _, _ = calcHists(gray, blue, green, red, imagem)

normalized_hist = normalized_gray(gray, data)

compareplotGrayOnly(base, data, normalized_hist)

normalized_img = new_gray_level(gray, accumulated_hist)

target_size = (400, 400)  # Adjust this size as needed

normalized_img_og, accumulated = generate_normalized_img(gray, normalized_hist)

# Resize each image to the target size
grayN_resized = cv2.resize(normalized_img, target_size)
gray_resized = cv2.resize(gray, target_size)
grayOG_resized = cv2.resize(normalized_img_og, target_size)

# Stack images horizontally in pairs and then vertically to form a single image
top_row = cv2.hconcat([gray_resized, grayOG_resized,grayN_resized])
combined_image = cv2.vconcat([top_row])


cv2.imshow("Combined Image", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

base, data_norm, _, _, _ = calcHists(normalized_img, blue, green, red, imagem)

base, data_norm_og, _, _, _ = calcHists(normalized_img_og, blue, green, red, imagem)

compareplotGrayOnlyThree(base, data ,data_norm, data_norm_og)





cv2.imwrite("out.jpg", imagem)