import os
from manimlib import *
class demo(Scene):
    def construct(self):

        # 创建一个点
        dot = Dot(color=BLUE, radius=0.1)
        self.play(ShowCreation(dot))
if __name__ == '__main__':
    os.system('manimgl {} demo'.format(__file__))
