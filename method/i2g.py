from images2gif import writeGif
from PIL import Image
import os
import pdb

    # file_names = ['0.jpg', '1.jpg', '2.jpg', '3.jpg']

    # images = [Image.open(fn) for fn in file_names]

    # size = (1024,768)
    # for im in images:
    #     im.thumbnail(size, Image.ANTIALIAS)

    # filename = "doge.gif"
    # # pdb.set_trace()
    # writeGif(filename, images, duration=1, dither=0, subRectangles=False)
class WriteGif(object):
    """docstring for WriteGif"""
    def __init__(self, ):
        super(WriteGif, self).__init__()
        # self.arg = arg

    def write(self, filename="doge.gif", duration=2, dither=0, subRectangles=False):
        file_names = os.listdir('.')
        # pdb.set_trace()
        for file_ in file_names:
            if file_[-4:] != '.jpg':
                file_names.remove(file_)
        file_names.sort()
        print 'flie_names', file_names
        images = [Image.open(fn) for fn in file_names]
        # pdb.set_trace()
        size = (609,651)
        for im in images:
            im.thumbnail(size, Image.ANTIALIAS)
        # pdb.set_trace()
        writeGif(filename, images, duration, dither, subRectangles=False)


if __name__ == '__main__':
    wg = WriteGif()
    wg.write()



