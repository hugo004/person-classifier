from django.conf import settings

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img

import os
import numpy as np

MODEL = os.path.join(settings.BASE_DIR, 'ml-model/sakura_ayane_model.h5')
model = load_model(MODEL)

BASE_DIR = str(settings.BASE_DIR)

seiyu_dict = {
  0: 'sakyra ayane',
  1: 'unkown'
}

class SeiyuService:
  
  @staticmethod
  def preprocess_img(img):
    img = img.resize((128,128))
    img = np.array(img)
    img = img / 255.0
    img = img.reshape(1,128,128,3)
    
    return img

  @staticmethod
  def predict_seiyu(img_url):
    full_path = BASE_DIR + img_url
    img = load_img(full_path)
    img = SeiyuService.preprocess_img(img=img)
    
    predict = model.predict(img)
    return seiyu_dict[np.argmax(predict)]