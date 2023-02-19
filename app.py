import openai
import urllib.request
from PIL import Image
import streamlit as st

openai.api_key = "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"

# Set page title and favicon
st.set_page_config(page_title="AI Image Generator", page_icon="icon.jpeg")


def generate_image(image_description):
    img_response = openai.Image.create(
        prompt=image_description,
        n=1,
        size="512x512")

    img_url = img_response['data'][0]['url']

    urllib.request.urlretrieve(img_url, 'img.png')

    img = Image.open("img.png")

    return img


# page title
st.title('"AI Image Generator"')

# text input box for image recognition
img_description = st.text_input('Image Description')

if st.button('Generate Image'):
    generated_img = generate_image(img_description)
    st.image(generated_img)
