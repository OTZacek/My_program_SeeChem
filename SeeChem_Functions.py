from PIL import Image, ImageTk
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

# image
def Load_png(file_path, width = None):
    original = Image.open(file_path)
    width = width
    ratio = width / original.width
    height = int(original.height * ratio)
    resized = original.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(resized)

def Load_svg(file_path, width = None):
    drawing = svg2rlg(file_path)
    img_pil = renderPM.drawToPIL(drawing)
    if width:
        ratio = width / img_pil.width
        height = int(img_pil.height * ratio)
        img_pil = img_pil.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(img_pil)
