import sys
from PIL import Image

def main():
    images = []

    # Cargamos las imágenes desde los argumentos
    for arg in sys.argv[1:]:
        img = Image.open(arg)
        images.append(img)

    if len(images) < 2:
        print("Necesitas al menos dos imágenes!")
        return

    size = images[0].size 

    frames = []
    for img in images:
        resized_img = img.resize(size) 
        frames.append(resized_img)

    frames[0].save(
        "costume.gif", 
        save_all=True, 
        append_images=frames[1:], 
        duration=200, 
        loop=0
    )
    print("¡GIF successfully created!")

if __name__ == "__main__":
    main()