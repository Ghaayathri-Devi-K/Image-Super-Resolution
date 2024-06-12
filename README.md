# Image-Super-Resolution
This repository implements a novel Knowledge Distillation based Generative Adversarial Network (KD-GAN) approach for achieving state-of-the-art image super-resolution. The proposed method surpasses existing techniques like SRCNN and SRGAN in terms of image quality, reaching a Structural Similarity Index Measure (SSIM) of 94%.

## Key Features:
<ul>
  <li><b>Superior Image Quality:</b> Achieves exceptional SSIM scores, outperforming existing methods. </li>
  <li><b>Hybrid Deep Learning Approach:</b> Combines knowledge distillation, a refined loss function, and regularization techniques. </li>
  <li><b>Faster Training: </b> Improved loss function facilitates faster training compared to traditional methods. </li>
</ul>

This repository includes:
<ol>
  <li>Implementation of the KD-GAN model for image super-resolution. </li>
  <li>Training scripts and configurations.</li>
</ol>

## Getting Started:

<ol>
  <li> <b>Clone the repository: </b> git clone https://github.com/Ghaayathri-Devi-K/Image-Super-Resolution </li>
    <li> Install dependencies (Refer to requirements.txt for details).</li>
    <li> Utilize the provided scripts for image super-resolution using the trained model.</li>
</ol>

## Experiment
 The model was trained using Python v3.9.13, and TensorFlow library v2.11.0 in a local machine configuration with 16GB RAM and NVIDIA GeForce RTX 3060 GPU.
 
## Dataset Used:
<ul>
  <li><b>Set5:</b> It contains five high-quality images, offering a range of different textures and structures. </li>
  <li><b>Set14:</b> Comprising 14 images, this dataset provides a more comprehensive challenge with a variety of scenes and objects. </li>
  <li><b>URBAN100:</b> Focused on urban scenes, URBAN100 contains 100 high-resolution images. It is useful for evaluating how well super-resolution models handle man-made structures.</li>
  <li><b>BSD100:</b> Part of the larger Berkeley Segmentation Dataset, BSD100 includes 100 diverse natural images.</li>
</ul>

## Model Architecture Used:
##### 1. Backpropogation steps used in the training process of the proposed KD-GAN
![image](https://github.com/Ghaayathri-Devi-K/Image-Super-Resolution/assets/99457944/42a91643-5c39-4fc4-a08a-68cbb77350b7)

The model architecture described in this section was trained for 100 epochs with a learning rate of 0.005. 

##### 2. The generator
![image](https://github.com/Ghaayathri-Devi-K/Image-Super-Resolution/assets/99457944/73b6bcaf-208b-44ac-8f51-c9370c4550d7)

Accepts an input of any size but requires a depth of 3 channels (RGB).

##### 3. The discriminator
![image](https://github.com/Ghaayathri-Devi-K/Image-Super-Resolution/assets/99457944/39106b7a-db48-44f2-a12a-6d1f4fc3bdba)

## Results

##### 1. Results obtained from mathematical models and Random forest regression and the original image displayed for comparison
![image](https://github.com/Ghaayathri-Devi-K/Image-Super-Resolution/assets/99457944/8f30fe89-73ae-4d8f-bb29-3ca2adcbcda0)

##### 2. Results from image super-resolution using SRCNN
![image](https://github.com/Ghaayathri-Devi-K/Image-Super-Resolution/assets/99457944/3192be32-179d-4804-8a4a-036981cf17d8)

##### 3. Results from image super-resolution using KD-GAN
![image](https://github.com/Ghaayathri-Devi-K/Image-Super-Resolution/assets/99457944/1827f6aa-db92-4001-a859-e80d8714dd04)

##### 4. Comparison of different models for the test-dataset
![image](https://github.com/Ghaayathri-Devi-K/Image-Super-Resolution/assets/99457944/be51e7fb-f70a-4080-b08e-afc5e084edc7)

##### 4. Comparison of different models for the existing benchmark image super-resolution datasets
![image](https://github.com/Ghaayathri-Devi-K/Image-Super-Resolution/assets/99457944/4bce1fef-f4b5-4a95-9308-2325af99b0a2)
