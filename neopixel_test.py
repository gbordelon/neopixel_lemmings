from PIL import Image
import numpy as np
import time

class DisplayMatrixTest(object):
    def __init__(self):
        self.max_x = 32
        self.max_y = 32
        self.data = np.zeros((self.max_y, self.max_x, 3), dtype=np.uint8)

    def __setitem__(self, xy, val):
        x, y = xy
        self.data[y,x] = val

    def __getitem__(self, xy):
        x, y = xy
        return self.data[x,y]

    def show(self):
        img = Image.fromarray(self.data, 'RGB')
        img.save('/tmp/displaymatrixtest.png')
        img.close()

if __name__ == '__main__':
    from lemmings import LemmingsAnimation, LemmingAliveState, LemmingDyingState

    display = DisplayMatrixTest()
    lemmings_anim = LemmingsAnimation()

    while True:
        for x,y,rgb in lemmings_anim.animation_pixel_generator(LemmingAliveState.WALK):
            if rgb is None:
                display.show()
                time.sleep(0.5)
            else:
                display[x,y] = rgb
