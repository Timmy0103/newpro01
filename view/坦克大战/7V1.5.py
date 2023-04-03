'''
V1.3
    新增功能：
            1、坦克类新增speed速度属性，用来控制坦克移动快慢
            2、时间处理：
                1.改变坦克方向
                2.修改坦克的位置（left,top）取决于坦克的速度
    优化功能：
            1、bug：坦克可以移出窗口边界
'''
import pygame
_display = pygame.display
COLOR_BLACK = pygame.Color(0,0,0)
COLOR_RED = pygame.Color(255,0,0)
version = 'V1.5'
class MainGame():
    # 游戏主窗口
    window = None
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 800
    # 创建我方坦克
    TANK_P1 = None
    def __init__(self):
        pass
    # 开始游戏方法
    def startgame(self):
        _display.init()
        # 加载游戏窗口
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])
        # 创建我方坦克
        MainGame.TANK_P1 = Tank(375,450)
        # 设置游戏标题
        _display.set_caption("坦克大战"+version)
        # 让窗口持续刷新操作
        while True:
            # 给窗口填充一个颜色
            MainGame.window.fill(COLOR_BLACK)
            # 在循环中持续完成时间的获取
            self.getEvent()
            # 将绘制文字得到的小画布，粘贴到窗口中
            MainGame.window.blit(self.getTextSurface("剩余敌方坦克{0}辆".format('5')),(5,5))
            # 将我方坦克加入到窗口中
            MainGame.TANK_P1.displayTank()
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
                    # 修改坦克方向
                    MainGame.TANK_P1.direction = 'L'
                    # 完成移动操作(调用坦克的移动方法)
                    MainGame.TANK_P1.move()
                elif event.key == pygame.K_RIGHT:
                    print("坦克向右掉头，移动")
                    # 修改坦克方向
                    MainGame.TANK_P1.direction = 'R'
                    # 完成移动操作(调用坦克的移动方法)
                    MainGame.TANK_P1.move()
                elif event.key == pygame.K_UP:
                    print("坦克向上掉头，移动")
                    # 修改坦克方向
                    MainGame.TANK_P1.direction = 'U'
                    # 完成移动操作(调用坦克的移动方法)
                    MainGame.TANK_P1.move()
                elif event.key == pygame.K_DOWN:
                    print("坦克向下掉头，移动")
                    # 修改坦克方向
                    MainGame.TANK_P1.direction = 'D'
                    # 完成移动操作(调用坦克的移动方法)
                    MainGame.TANK_P1.move()
                elif event.key == pygame.K_SPACE:
                    print("发射子弹")
    # 左上角文字绘制的功能
    def getTextSurface(self,text):
        # 初始化字体模块
        pygame.font.init()
        # 查看系统支持的所有字体
        # fontList = pygame.font.get_fonts()
        # print(fontList)
        # 选中一个合适的字体
        font = pygame.font.SysFont('kaiti',18)
        # 使用对应的字符完成相关内容的绘制
        textSurface = font.render(text,True,COLOR_RED)
        return textSurface

    # 结束游戏方法
    def endgame(self):
        print("谢谢使用")
        #结束python解释器
        exit()
class Tank():
    def __init__(self,left,top):
        self.images = {
            'U':pygame.image.load('E:/1tank/p1tankU.png'),
            'D':pygame.image.load('E:/1tank/p1tankD.png'),
            'L':pygame.image.load('E:/1tank/p1tankL.png'),
            'R':pygame.image.load('E:/1tank/p1tankR.png')
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        # 坦克所在的区域 Rect-->
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置 分别距X，Y轴的位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = 5
    # 坦克的移动方法
    def move(self):
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < MainGame.SCREEN_WIDTH:
                self.rect.left += self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.wheight < MainGame.SCREEN_HEIGHT:
                self.rect.top += self.speed
    # 坦克射击方法
    def shot(self):
        pass
    # 展示坦克（将坦克这个surface绘制到窗口中）
    def displayTank(self):
        # 1.重新设置坦克的图片
        self.image = self.images[self.direction]
        # 2.将坦克加入到窗口中
        MainGame.window.blit(self.image,self.rect)
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