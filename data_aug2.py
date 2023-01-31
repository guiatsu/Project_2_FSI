import cv2
import glob
import imgaug.augmenters as iia
import os
images = []
images_path = glob.glob('imgs/*.jpg')
for image_path in images_path:
    image = cv2.imread(image_path)
    if image is not None:
        images.append(image)
    else:
        print('Error loading image: ', image_path)
#fliped images
flip_aug = iia.Sequential([
    iia.Fliplr(1.0),
])
#rotated by 30 degrees images
rotate_aug = iia.Sequential([
    iia.Affine(rotate=(-30, 30)),
])
#blurred images
blur_aug = iia.Sequential([
    iia.GaussianBlur(sigma=(0.0, 3.0)),
])
#brightness images
brightness_aug = iia.Sequential([
    iia.Multiply((0.8, 1.2)),
])
#contrast images
contrast_aug = iia.Sequential([
    iia.LinearContrast((0.6, 1.4)),
])

# apply augmenters to images
flip_images = flip_aug.augment_images(images)
rotate_images = rotate_aug.augment_images(images)
blur_images = blur_aug.augment_images(images)
brightness_images = brightness_aug.augment_images(images)
contrast_images = contrast_aug.augment_images(images)

# combine all augmented images
augmented_images = [flip_images , rotate_images , blur_images , brightness_images , contrast_images]
augmented_images_folder_name = ['flipped', 'rotated', 'blurred', 'brightness', 'contrast']
for i in range(len(augmented_images)):
    if not os.path.exists(augmented_images_folder_name[i]):
        os.makedirs(augmented_images_folder_name[i])
    cont = 0
    for image in augmented_images[i]:
        cv2.imwrite(augmented_images_folder_name[i]+'/image_'+str(cont)+'.jpg', image)
        cont+=1
