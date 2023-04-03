'''
V1.1
    新增功能：
    创建游戏窗口
    利用游戏引擎中的功能模块
    官方开发文档（www.pygame.org）
'''
import pygame
_display = pygame.display
COLOR_BLACK = pygame.Color(0,0,0)
class MainGame():
    # 游戏主窗口
    window = None
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 800
    def __init__(self):
        pass
    # 开始游戏方法
    def startgame(self):
        _display.init()
        # 加载游戏窗口
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])
        # 设置游戏标题
        _display.set_caption("坦克大战V1.1")
        # 让窗口持续刷新炒作
        while True:
            # 给窗口填充一个颜色
            MainGame.window.fill(COLOR_BLACK)
            #窗口的刷新
            _display.update()
    # 结束游戏方法
    def endgame(self):
        print("谢谢使用")
        #结束python解释器
        exit()
class Tank():
    def __init__(self):
        pass
    # 坦克移动方法
    def move(self):
        pass
    # 坦克射击方法
    def shot(self):
        pass
    # 展示坦克
    def displayTank(self):
        pass
class MyTank(Tank):
    def __init__(self):
         pass
class EnemyTank(Tank):
    def __init__(self):
        pass
class Bullet():
    def __init__(self):
        pass
    # 子弹移动方法
    def move(self):
        pass
    # 展示子弹
    def displayBullet(self):
        pass
class Explode():
    def __init__(self):
        pass
    # 展示爆炸效果
    def displayExplode(self):
        pass
class Wall():
    def __init__(self):
        pass
    #展示墙壁
    def displayWall(self):
        pass
class Music():
    def __init__(self):
        pass
    #开始播放音乐
    def play(self):
        pass

MainGame().startgame()