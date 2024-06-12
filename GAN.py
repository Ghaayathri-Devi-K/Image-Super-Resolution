import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from skimage.metrics import peak_signal_noise_ratio, mean_squared_error, structural_similarity
import warnings
from tensorflow import keras
warnings.filterwarnings("ignore")

gen = keras.models.load_model('generator_100')

def inference_gan(gen):
    st.markdown(f"<center><h1 style='font-size: 40px;'>DISTILLED LEARNING GAN</h3></center>", unsafe_allow_html=True)
    x = st.slider("Adjust x", min_value=0, max_value=100, value=5)
    low_res_image_path = f"Data/LR/{x}.png"
    high_res_image_path = f"Data/HR/{x}.png"
    
    lr_img = Image.open(low_res_image_path)
    lr_img = np.array(lr_img.resize((96, 96))) / 255.0
    lr_img = np.expand_dims(lr_img, axis=0)
    hr_img = Image.open(high_res_image_path)
    hr_img = np.array(hr_img.resize((384, 384))) / 255.0
    gen_img = gen.predict(lr_img)
    gen_img = np.squeeze(gen_img, axis=0)
    gen_img = np.clip(gen_img, 0, 1)
    col1, col2 = st.columns(2)
    with col1:
        st.image(lr_img[0], caption="Low-Resolution (LR)", use_column_width=True)
    with col2:
        st.image(gen_img, caption="Generated High-Resolution (HR)", use_column_width=True)
    psnr = peak_signal_noise_ratio(hr_img, gen_img)
    mse = mean_squared_error(hr_img, gen_img)
    # ssim = structural_similarity(hr_img, gen_img, multichannel=True)
    st.markdown(f"<center><h4 style='font-size: 22px;'>PSNR: {psnr}</h3></center>", unsafe_allow_html=True)
    st.markdown(f"<center><h4 style='font-size: 22px;'>MSE: {mse}</h3></center>", unsafe_allow_html=True)
    # st.markdown(f"<center><h4 style='font-size: 22px;'>SSIM: {ssim}</h3></center>", unsafe_allow_html=True)


inference_gan(gen)

