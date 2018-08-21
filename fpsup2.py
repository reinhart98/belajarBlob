# import the necessary packages
from __future__ import print_function
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2
import numpy as np

vs = WebcamVideoStream(src=0).start()
fps = FPS.start()

while(True):
    # Capture frame-by-frame
    frame = vs.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
     

# When everything done, release the capture
vs.release()
cv2.destroyAllWindows()