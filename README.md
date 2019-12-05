# open-sign-detector
Open-source project to detect traffic signs and classify them

# Built for the IARRC's challenge

Need to recognize signs? Train your own network! Because raw OpenCV is hard.

# The Dataset

The dataset consists of images broken from videos I took myself of the sign in different positions. I split up the images into folders so you can load them individually


# The Model

The model is exported as the md5 file in the repos but feel free to build your own using the Jupyter Notebook provided.


# Built during this stream

https://www.twitch.tv/videos/516355741

And was completed in about an hour.

# For loading into the Pi
import keras
import numpy as np
import cv2
from tensorflow.keras import models

model = models.load_model("sign_detect_model.h5")
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    input_frame = np.array(cv2.resize(frame,(64,64)),dtype=np.float32)
    y_prob = model.predict(input_frame) 
    y_class = y_prob.argmax(axis=-1)
    print(y_class)
    # Keys to close the stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release the capture
cap.release()
cv2.destroyAllWindows()

# Next steps:

1. Add more images
2. Add more augmentations to create a more general model, currently the model is already operating well in 2 epochs.
