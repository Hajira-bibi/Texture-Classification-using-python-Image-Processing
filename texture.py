import os
import random
import numpy as np
from skimage import io
from skimage.feature import local_binary_pattern
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# Dataset 3 classes
classes = {
    'fabric': 'fabric',
    'glass': 'glass',
    'wood': 'wood'
}


#load images from the dataset
def load_random_image(class_name):
    img = os.listdir(classes[class_name])
    selected_img = random.choice(img)
    img_path = os.path.join(classes[class_name], selected_img)
    image = io.imread(img_path)
    return image, img_path

#lBP method
def lbp(image, P=8, R=1):
    img_gray = rgb2gray(image)
    image_gray = (img_gray * 255).astype(np.uint8)
    Lbp = local_binary_pattern(image_gray, P, R, method='uniform')
    histogram, _ = np.histogram(Lbp.ravel(), bins=np.arange(0, P + 3), range=(0, P + 2))
    histogram = (histogram.astype("float"))
    histogram /= histogram.sum()  # Normalize the histogram
    return (histogram, Lbp)

# standard deviation of the two histogram
def std_deviation(hist1, hist2):
    std_dev = np.std(hist1 - hist2)
    return std_dev

#extract LBP features for the first image
first_class = random.choice(list(classes.keys()))  # Randomly select the first class
first_img, first_image_path = load_random_image(first_class)

#extract LBP features for the second image
second_class = random.choice(list(classes.keys()))  # Randomly select the second class
second_img, second_image_path = load_random_image(second_class)


#call LBP function
first_img_hist, first_lbp_img = lbp(first_img)
second_img_hist, second_lbp_img = lbp(second_img)

# Calculate the standard deviation between the two histograms
std_dev = std_deviation(first_img_hist, second_img_hist)

#Classification


#threshold=0.01
#threshold=0.05
#threshold=0.2
threshold = 0.03    # Adjust the threshold based on experimentation
classification = "similar" if std_dev < threshold else "different"

# Output
print(f"First image from class '{first_class}': {first_image_path}")
print(f"Second image from class '{second_class}': {second_image_path}")
print(f"Standard Deviation between the two images: {std_dev:.4f}")
print(f"Classification: {classification}")

# Ploting
plt.figure(figsize=(15, 9))

plt.subplot(2, 2, 1)
plt.imshow(first_img)
plt.title('First Image from ' + first_class)
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(first_lbp_img, cmap='gray')
plt.title('LBP Image for First Image')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(second_img)
plt.title('Second Image from ' + second_class)
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(second_lbp_img, cmap='gray')
plt.title('LBP Image for Second Image')
plt.axis('off')

plt.suptitle(
    f'Results: The images are classified as {classification}. \n '
    f'Standard Deviation: {round(std_dev, 4)} \n  Threshold: {threshold}'
)
plt.tight_layout()
plt.show()
