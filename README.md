# Driver Drowsiness Detection Using CNN

## 1. Project Overview
This project uses a Convolutional Neural Network (CNN) to classify eye images into two categories:

- **Closed (0):** the eye is closed.
- **Open (1):** the eye is open.

After training, the notebook demonstrates a simple drowsiness rule: if the model predicts **Closed** for several consecutive frames, it prints a **DROWSINESS ALERT** message.

> **Project scope:** The current notebook does not process a real driving video or run continuous webcam detection. It demonstrates eye-image classification and simulates a sequence using test images.

## 2. Objectives
- Load labelled open-eye and closed-eye images.
- Resize and normalize images before training.
- Build and train a simple CNN model.
- Evaluate the model using a separate test set.
- Demonstrate a basic consecutive-closed-frame alert rule.

## 3. Technologies Used
- Python
- TensorFlow / Keras
- NumPy
- Matplotlib
- scikit-learn
- KaggleHub
- Google Colab

## 4. Dataset
The notebook downloads the MRL Eye Dataset through KaggleHub:

`imadeddinedjerarda/mrl-eye-dataset`

The notebook searches the downloaded folders for image files. It labels an image using its parent folder name:
- Folder name containing `close` → Closed (0)
- Folder name containing `open` → Open (1)

Supported image formats: `.png`, `.jpg`, `.jpeg`, `.bmp`.

The notebook uses up to **8,000 images per class** to keep training manageable. Confirm that the dataset folders are named in a way that contains `open` or `close`; otherwise the notebook will not identify the labels.

Dataset source page: https://www.kaggle.com/datasets/imadeddinedjerarda/mrl-eye-dataset

Please follow the dataset provider's terms and conditions.

## 5. CNN Architecture
The model uses:
1. Input: 64 × 64 grayscale eye image
2. Conv2D (16 filters) + MaxPooling
3. Conv2D (32 filters) + MaxPooling
4. Conv2D (64 filters) + MaxPooling
5. Flatten
6. Dense (64 neurons)
7. Dropout (0.3)
8. Dense (1 neuron, sigmoid activation)

**Compilation settings**
- Optimizer: Adam
- Loss: Binary Crossentropy
- Metric: Accuracy
- Epochs: 5
- Batch size: 64

## 6. Project Workflow
1. Import required libraries and set random seeds.
2. Download the dataset using KaggleHub.
3. Collect image paths and assign labels.
4. Split the data into training (70%), validation (15%), and testing (15%).
5. Load images as grayscale, resize to 64 × 64, and normalize pixel values to 0–1.
6. Build and train the CNN.
7. Plot training and validation accuracy/loss.
8. Evaluate the model and display a classification report and confusion matrix.
9. View sample predictions.
10. Demonstrate a consecutive-closed-frame alert using a simulated sequence.
11. Save the model as `drowsiness_cnn.keras`.

## 7. How to Run in Google Colab
1. Open https://colab.research.google.com/.
2. Select **File → Upload notebook**.
3. Upload `Driver_Drowsiness_Detection_CNN.ipynb`.
4. Select **Runtime → Run all**, or run each cell from top to bottom.
5. Allow the notebook to install KaggleHub and download the dataset.
6. Wait for training, evaluation, and prediction cells to finish.
7. The final model is saved as `drowsiness_cnn.keras` in the Colab session.

A Google account and internet access are required for KaggleHub dataset download. If KaggleHub or the dataset download fails, check the internet connection and dataset availability, then retry.

## 8. Files in This Project
- `Driver_Drowsiness_Detection_CNN.ipynb` — complete Google Colab notebook.
- `README.md` — project overview and execution instructions.
- `requirements.txt` — Python package dependencies for a local Python environment.
- `.gitignore` — files and folders that should not be committed to Git.

## 9. Requirements
For Google Colab, the notebook installs KaggleHub in a notebook cell and uses the Colab environment. For local execution, install the packages listed in `requirements.txt`. TensorFlow installation can depend on your Python version and operating system; use a TensorFlow-supported Python version.

## 10. Limitations
- The model classifies individual eye images; it does not locate eyes in a full face image.
- The alert sequence is simulated from test images, not extracted from a real driving video.
- A fixed frame threshold is only a demonstration and does not represent a medically or scientifically validated drowsiness threshold.
- Dataset quality, lighting, glasses, camera angle, and differences between training images and real camera images can affect predictions.
- The project is an educational prototype, not a certified driver-safety system. Do not use it as a substitute for safe driving practices.

## 11. Future Enhancements
- Read frames from a driving video or webcam.
- Detect face and eye regions using OpenCV or MediaPipe.
- Send detected eye crops to the trained CNN.
- Add a sound alarm when prolonged eye closure is detected.
- Test on independent videos and report precision, recall, and false-alarm rate.

## 12. Expected Output
The notebook displays:
- Number of open and closed images found.
- Training and validation accuracy/loss plots.
- Test accuracy.
- Classification report and confusion matrix.
- Sample eye-image predictions.
- A text-based drowsiness alert for the simulated frame sequence.

