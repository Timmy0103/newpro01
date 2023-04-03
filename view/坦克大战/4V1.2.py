'''
V1.2
    新增功能：
    事件处理：
        点击关闭按钮，推出程序的事件
        方向控制，子弹控制
'''
import pygame
_display = pygame.display
COLOR_BLACK = pygame.Color(0,0,0)
version = 'V1.2'
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
        _display.set_caption("坦克大战"+version)
        # 让窗口持续刷新炒作
        while True:
            # 给窗口填充一个颜色
            MainGame.window.fill(COLOR_BLACK)
            # 在循环中持续完成时间的获取
            self.getEvent()
            #窗口的刷新
            _display.update()
    #获取程序期间的所有事件（鼠标事件，键盘事件）
    def getEvent(self):
        # 1、获取所有事件
        eventList = pygame.event.get()
        # 2、对事件进行判断处理（1.点击和关闭按钮；2.按下键盘上的某个按键）
        for event in eventList:
            # 判断event.type是否QUIT，如果是退出的话，直接调用程序结束方法
            if event.type == pygame.QUIT:
                self.endgame()
            # 判断事件类型是否为按下按键，如果是，继续判断按键是哪一个按键，来进行对应的处理
            if event.type == pygame.KEYDOWN:
                # 具体是那个案件的处理
                if event.key == pygame.K_LEFT:
                    print("坦克向左掉头，移动")
                elif event.key == pygame.K_RIGHT:
                    print("坦克向右掉头，移动")
                elif event.key == pygame.K_UP:
                    print("坦克向上掉头，移动")
                elif event.key == pygame.K_DOWN:
                    print("坦克向下掉头，移动")
                elif event.key == pygame.K_SPACE:
                    print("发射子弹")
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