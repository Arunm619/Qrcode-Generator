import pyqrcode
import png
import string
import random
from PIL import Image
import qrcode

''' Generating unique String
@:param id_generator 
@returns string
'''


def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


''' Creates a QR code IMG in PNG format
@:param id_generator 
@returns string
'''


def createimg():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=4,
    )
    qr.add_data(id_generator())
    qr.make(fit=True)
    img = qr.make_image()
    img.save("qr.jpg")


def embed_qr_in_id():
    image = Image.open('idcardpartrgb.jpg')
    logo = Image.open("qr.jpg")
    image_copy = image.copy()
    # co-ordines of the QR code Position
    position = (244, 790)
    image_copy.paste(logo, position)
    image_copy.save('final' + str(i) + '.jpg')


# for i in range(1500): a=id_generator()
# createimg()
# createimg()


# 373,1151


# add_logo("mqr.png","logo.png","FirstQR.png")


i = 0
# for i in range(1500):
createimg()
embed_qr_in_id()
