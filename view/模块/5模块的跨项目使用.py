'''
1、模块的发布
    为什么要发布？
    自定义模块，切换项目后，不可以使用
    系统模块，切换项目后，可以使用
    sys.path路径下没有要导入的模块，会无法导入模块，通过如下方法解决：
    1、将模块所在路径手动添加到sys.path中
    2、将自定义模块，发布到系统目录中
        发布自定义模块到系统目录的步骤：
        1、确定的发布模块的目录结构
        |--setup.py
        |--package1
            |--自定义模块 MyMath
        2、setup的编辑工作
        setup()
        3、构建模块
        python setup.py build
        4、发布模块
        python setuo,py sdist
2、模块的安装
    1、通过命令安装
        1、找到之前发布的压缩包，解压操作
        2、python setup.py install  # 默认路径安装，也可以指定安装路径，后天添加 prefix=安装路径
    2、暴力安装
        直接将要安装的包以及模块复制到系统目录中
'''
# import MyMath
# import random
import sys
list1 = sys.path  # 搜索路径列表
print(type(list1))
for path in list1:
    print(path)