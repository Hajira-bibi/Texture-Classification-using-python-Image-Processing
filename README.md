
# Image Processing Class Assignment

This project demonstrates texture classification using **Local Binary Pattern (LBP)**. It classifies images from three categories: fabric, glass, and wood, and compares their textures based on LBP features.

## Project Structure
ImageProcessingClass/ ├── fabric/ # Folder containing fabric images ├── glass/ # Folder containing glass images ├── wood/ # Folder containing wood images ├── texture.py # Python script for texture classification └── README.md # This README file



## How to Run
1. **Install the required libraries**:
   ```bash
   pip install numpy scikit-image matplotlib
Place images in the fabric/, glass/, and wood/ folders.
Run the code using:
bash
Copy code
python texture.py
Output
Displays the original and LBP-transformed images.
Classifies the images as "similar" or "different" based on the standard deviation of LBP histograms
