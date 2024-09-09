from PIL import Image

image = Image.open('Arijeet Ghosh_Iem_bca 2025.jpg')
dpi = image.info['dpi']
print(f"DPI: {dpi}")
