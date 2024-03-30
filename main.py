import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from pngMakeGradient import create_gradient_image_with_transparent_background

# Функция для загрузки изображения из Dropbox
def load_image_from_dropbox(dropbox_url):
    response = requests.get(dropbox_url)
    image = Image.open(BytesIO(response.content))
    return image

# Функция для обработки изображения
def process_image(image):
    # Ваш код обработки изображения здесь
    processed_image = create_gradient_image_with_transparent_background(image)  # Просто заглушка, замените эту строку на ваш реальный код обработки
    return processed_image

# Функция для скачивания изображения
def download_image(image, filename='processed_image.png'):
    image.save(filename)
    with open(filename, "rb") as f:
        data = f.read()
    return data, filename

# Заголовок и описание приложения
st.title('Приложение для обработки изображений')
st.write('Это приложение позволяет обрабатывать изображения, в стиле Strana.')

# Загрузка изображения
uploaded_image = st.file_uploader('Выберите изображение', type=['png'])
if uploaded_image is not None:
    try:
        image = Image.open(uploaded_image)
        st.image(image, caption='Загруженное изображение', use_column_width=True)

        # Обработка изображения
        processed_image = process_image(image)
        st.image(processed_image, caption='Обработанное изображение', use_column_width=True)

        processed_image_data, processed_image_filename = download_image(processed_image)
        st.download_button(label='Нажмите, чтобы скачать', data=processed_image_data, file_name=processed_image_filename, mime='image/png')
    except Exception as e:
        st.error(f'Ошибка: {e}')
