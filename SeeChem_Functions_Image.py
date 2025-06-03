from PIL import Image, ImageTk

# image
def Load_png(file_path, width = None):
    original = Image.open(file_path)
    width = width
    ratio = width / original.width
    height = int(original.height * ratio)
    resized = original.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(resized)