from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

with Image.open("154141af5c9bea6feac1a0a24653af6e.jpeg") as pic_original:
    print("rasmer kartinki:", pic_original.size)
    print("format:", pic_original.format)
    print("tip:", pic_original.mode)
    pic_original.show()

    pic_gray = pic_original.convert("L")
    pic_gray.save("gray.jpg")
    pic_gray.show()

    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save("blured.jpg")
    pic_blured.show()

    pic_up = pic_original.transpose(Image.ROTATE_180)
    pic_up.save("up.jpg")
    pic_up.show()

    pic_mirror = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    pic_mirror.save("mirror.jpg")
    pic_mirror.show()

    pic_contrast = ImageEnhance.Contrast(pic_original)
    pic_contrast = pic_contrast.enhance(1.5)
    pic_contrast.save("contrast.jpg")
    pic_contrast.show()

    pic_gray_smooth = pic_original.filter((ImageFilter.SMOOTH))
    pic_gray_smooth = pic_gray_smooth.filter(ImageFilter.FIND_EDGES)
    pic_gray_smooth.save("smooth.jpg")
    pic_gray_smooth.show()

    pic_rotated = pic_original.rotate(30, expand=True)
    pic_rotated.save("rotate.jpg")
    pic_rotated.show()