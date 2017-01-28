from PIL import Image, ImageFilter
import os

size_300 =(300,300)
size_100 =(100,100)

# for f in os.listdir('.'):
#     if(f.endswith('.jpg')):
#         i = Image.open(f)
#         fn, fext = os.path.splitext(f)
#         print fn
#         i.thumbnail(size_300)
#         i.save('100/{}_100{}'.format(fn, fext))
# image1 = Image.open('min.jpg')
# image1.filter(ImageFilter.GaussianBlur()).save('min_mod.jpg')

image1 = Image.open('boo.jpg')
# fn, fext = os.path.splitext(image1)
image1.thumbnail(size_100)
image1.save('100/{}_100{}'.format('boo', '.png'))