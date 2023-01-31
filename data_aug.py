import glob
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from numpy import expand_dims
from matplotlib import pyplot
import os
# Get all JPG images in the directory 'imgs/*.jpg'
image_list = glob.glob('imgs/*.jpg')

# Create an instance of the ImageDataGenerator class
datagen = ImageDataGenerator(horizontal_flip=True, fill_mode='constant')

# Iterate through the list of images
cont = 0
for image_path in image_list:
    # Load the image
    image = load_img(image_path)

    image = img_to_array(image)
    image_new = expand_dims(image, 0)
    datagen.fit(image_new)
    # rotated_images = datagen.flow(image_new, batch_size=1)
    # rotated_image = next(rotated_images)
    rotated_image = datagen.flow(image_new, batch_size=1).next()[0].astype('uint8')
    new_file_name = 'rotated\\image_'+str(cont)+'.jpg'
    pyplot.imsave(new_file_name, rotated_image.astype('uint8'))
    cont += 1
    # for i, rotated_image in enumerate(rotated_images):
    #     print(i)
    #     new_file_name = 'rotated\\image_'+str(i)+'.jpg'
    #     pyplot.imsave(new_file_name, rotated_image[0].astype('uint8'))

        
