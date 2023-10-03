import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

model = tf.keras.models.load_model('handwritten_digit_recognition.model')


img_number=1
while os.path.isfile(f'pics/digit{img_number}.png'):
    try:
        img=cv2.imread(f'pics/digit{img_number}.png')[:,:,0]
        img=np.invert(np.array([img]))
        prediction = model.predict(img)
        print(f'the number is probably a {np.argmax(prediction)}')
        plt.imshow(img[0],cmap=plt.cm.binary)
        plt.show()

    except:
        print("error")    

    finally:
        img_number+=1   