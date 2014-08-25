import os
from PIL import Image, ImageFile

def convert_jpg(img_dir, scale_img, img_quality):
    print "called"
    img_files = [f for f in os.listdir(img_dir) if f.endswith('jpg')]
    for i in range(len(img_files)):
        img_file = Image.open(img_dir+"/"+img_files[i])
        print img_dir+"/"+img_files[i]
        if scale_img == 100:
            width, height = img_file.size
        else:
            width, height = (int(scale_img * img_file.size[0] / 100.0), 
                            int(scale_img * img_file.size[1] / 100.0))

        img_file = img_file.resize((width, height), Image.ANTIALIAS)
        try:
            img_file.save(img_dir+"/"+img_files[i], 
                          optimize=True, 
                          quality=img_quality, 
                          progressive=True)
        except IOError:
            ImageFile.MAXBLOCK = width * height
            img_file.save(img_dir+"/"+img_files[i], 
                          optimize=True, 
                          quality=img_quality, 
                          progressive=True)
        print str(i)
path_to_images = "images"
scale_img = 10
img_quality = 100
convert_jpg(path_to_images, scale_img, img_quality)