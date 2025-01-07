# [PYTHON PROJECT] : Complex QR Code Generator with Image Functionality

import qrcode               # Importing Module [qrcode].
from PIL import Image       # Importing Module [PIL], & accessing its Image Module.
                            # "PIL" Stands for Pillow Module. This dependency is used for Image related functionalities.

qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 10, border = 4,)      # [QRCode] is function that belongs to the module [qrcode], and allows one to change the functionality [i.e. Borders, Version, Errors, etc.] of a generated QR Code.
qr.add_data("https://www.linkedin.com/in/ripan-das-375b33286")

qr.make(fit = True)         # "make()" function can be used only after importing the module [i.e. qrcode] and allows one to generate a QR Code.
                            # "make(fit = True)" signifies that the function will only be executed if the data recieved from the URL evaluates to be True.

# Further we create a variable "img" assigning the previous variable "qr" followed by accessing the function "make_image()" in order to customize and alter the generated image properties.
img = qr.make_image(fill_color = "Green", back_color = "White")

# "save()" function can be used only after importing the module [i.e. qrcode], and allows one to save the generated qr code as an image file
img.save("Generated_QR_01.png")