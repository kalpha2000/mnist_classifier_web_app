from keras.models import load_model
import numpy as np
import cv2
import matplotlib.pyplot as plt

model = load_model(r'D:\college\machine learning\code\project\web app ml\digit classifier\mnist.h5')

def pred_digit(img_path):
    img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
    if img is not None:
        img = cv2.resize(img, (28,28))
        plt.imshow(img)
        plt.show()
        img = (img/255.0).reshape(1,28,28)
        img = np.expand_dims(img,-1)
        pred = np.argmax(model.predict(img)[0])

        return str(pred)
    
    else:
        return None


if __name__ == "__main__":
    img_path = r'./project/web app ml/digit classifier/digit.jpg'
    print(pred_digit(img_path))