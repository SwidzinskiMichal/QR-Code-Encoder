import qrcode
from PIL import Image


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
def logo_resize():
    # Image source
    logo_source = '/home/michal/Workspace/qr-code-encoder/Token.png'
    logo = Image.open(logo_source)

    # Logo size adjustment 
    new_logo = logo.resize((50, 50))
    return new_logo

def set_colors():
    # Set colors for image
    QRcolor = "Black"
    BGcolor = "White"
    return QRcolor, BGcolor

def create_qr(QRcontent, QRcolor, BGcolor, new_logo):
    # Data that will be encoded 
    data = QRcontent

    # Add data to create QR Code
    qr.add_data(data)
    QR_Image = qr.make_image(fill_color=QRcolor, back_color=BGcolor)

    # Position the logo
    pos = ((QR_Image.size[0] - new_logo.size[0]) // 2,
        (QR_Image.size[1] - new_logo.size[1]) // 2)
    QR_Image.paste(new_logo, pos)
    # Save the Image
    QR_Image.save("/home/michal/Workspace/qr-code-encoder/Generated-QR-Code.png")
    return QR_Image

def generate_qrcode(QRcontent):
    new_logo = logo_resize()
    QRcolor, BGcolor = set_colors()
    print('QR code generated!')
    return create_qr(QRcontent, QRcolor, BGcolor, new_logo)

generate_qrcode("https://www.youtube.com/watch?v=nmb_831Io7w")