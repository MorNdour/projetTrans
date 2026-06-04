# Tomato Disease Classification – Raspberry Pi

Classify tomato leaf diseases using a CNN deployed on a Raspberry Pi with IoT sensors.

## Project Summary

This project tackles the classification of tomato leaf diseases using image data. We:

- Prepared and preprocessed a labeled dataset of tomato leaf images.
- Trained a Convolutional Neural Network (CNN) to recognize and classify disease categories from images.
- Evaluated the CNN's performance using a confusion matrix and classification report (see notebook for details).
- Post-training quantization. [See report](https://www.researchgate.net/publication/404732965_Post-Training_Quantization_and_Core_ML_Deployment_of_a_Tomato_Disease_Classifier_for_On-Device_Inference)

---

## Results

The CNN model was evaluated **with and without data augmentation**. The following metrics summarize the improvement:

### Comparison Table

| Model                  | Test Accuracy | Macro F1 | Weighted F1 |
|------------------------|---------------|----------|-------------|
| CNN (no augmentation)  | 0.87          | 0.87     | 0.87        |
| CNN (with augmentation)| 0.92          | 0.92     | 0.92        |

---

### Confusion Matrices

**Left:** CNN without augmentation &nbsp;&nbsp;|&nbsp;&nbsp; **Right:** CNN with augmentation

<p>
  <img src="image-1.png" style="width:49%; display:inline-block;" />
  <img src="image-2.png" style="width:49%; display:inline-block;" /> 
</p>


---

### Training Curves

**Left:** CNN without augmentation &nbsp;&nbsp;|&nbsp;&nbsp; **Right:** CNN with augmentation

<p>
  <img src="image-4.png" style="width:49%; display:inline-block;" />
  <img src="image-3.png" style="width:49%; display:inline-block;" /> 
</p>


---

## Takeaways

- Data augmentation greatly improved the model’s generalization (reducing potential shift issues) and accuracy.  
- CNN reached **92% test accuracy** with augmentation, compared to 87% without.  

---

## Tools

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-444876?style=for-the-badge&logo=seaborn&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-563D7C?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
