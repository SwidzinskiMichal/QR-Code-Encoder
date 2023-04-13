from QRgenerator import set_colors

def test_colors():
    QRcolor, BGcolor = set_colors()
    if QRcolor == BGcolor:
        raise Exception ("QR color and background color must be different!")