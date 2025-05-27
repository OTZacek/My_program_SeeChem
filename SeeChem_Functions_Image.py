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

def Load_svg(file_path, width=None):
    drawing = svg2rlg(file_path)  
    if width and drawing.width != 0:
        scale_factor = width / drawing.width
        img_pil = renderPM.drawToPIL(drawing, scale=scale_factor)
    else:
        img_pil = renderPM.drawToPIL(drawing)
    
    return ImageTk.PhotoImage(img_pil)