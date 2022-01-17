import os
from PIL import Image

width = 512
path = "../images/"
images = os.listdir(path)  # original images in images dir

for infile in images:
    outfile = infile[:-4] + ".jpeg"
    try:
        png = Image.open(path+infile)
        # png = png.convert('RGB', png.size, (0, 0, 0))
        im = Image.new("RGB", png.size, (0, 0, 0))
        im.paste(png, mask=png.split()[3])
        ratio = width/im.size[0]
        size = (im.size[0]*ratio//1, im.size[1]*ratio//1)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(outfile, "JPEG", quality=95, optimize=True)
        print("saved image", outfile)
    except IOError:
        print("cannot create thumbnail for '%s'" % infile)
