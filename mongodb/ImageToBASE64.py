import base64
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/loggings")


class ImageToBASE64:
    def __init__(self, image):
        self.image = image

        
with open('C:/Users/SAMSUNG\Desktop/hsh\git/Friends-versus/mongodb/test.png', 'rb') as img:
    base64_string = base64.b64encode(img.read())

print(base64_string)