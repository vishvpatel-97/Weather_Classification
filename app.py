import streamlit as st
import numpy as np
from skimage.io import imread
from skimage.transform import resize
import pickle
from PIL import Image
st.title('Weather Image Classification')
st.text('Upload the Image')

model=pickle.load(open('classifier.pkl','rb'))
uploaded_file =st.file_uploader("Choose an image...", type='jpg')
if uploaded_file is not None:
  img=Image.open(uploaded_file)
  st.image(img,caption='Uploaded Image')

  if st.button('PREDICT'):
    CATEGORIES=['cloudy','rainy','shiny','sunrise']
    st.write('Result...')
    flat_data=[]
    img=np.array(img)
    img_resized=resize(img,(150,150,3))
    flat_data.append(img_resized.flatten())
    flat_data=np.array(flat_data)
    y_out=model.predict(flat_data)
    y_out=CATEGORIES[y_out[0]]
    st.title(f'PREDICTED OUTPUT:{y_out}')
    q=model.predict_proba(flat_data)
    for index, item in enumerate(CATEGORIES):
      st.write(f'{item}:{q[0][index]*100}')

