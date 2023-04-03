'''
面向对象编程的思想主要是针对大型软件设计而来的。面向对象编程使程序的扩展性更强、可读性更好，
使得编程可以像搭积木一样简单
面向对象编程将数据和操作数据相关的方法封装到对象中，组织代码和数据的方式更加接近人的思维，
从而大大提高了编程的效率
Python完全采用了面向对象的思想，是真正面向对象的编程语言，完全支持面向对象的基本功能，
例如：继承、多态、封装等
Python中，一切皆对象，我们在前面学习的数据类型、函数等，都是对象
Python支持面向过程、面向对象、函数式编程等多种编程范式
'''

'''
面向过程思维
面向过程编程更加关注的是“程序的逻辑流程”，是一种“执行者”思维，适合编写小规模的程序
面向过程思维思考问题时，我们首先思考“怎么按步骤实现？”，并将步骤对应成方法，一步一步，最终实现
这个适合单任务，不需要过多协作的情况。比如，如何开车？我们很容易就列出实现步骤：
1.发动车 2.挂挡 3.踩油门 4.走你
面向过程适合简单，不需要协作的事务。但是当我们思考比较复杂的问题。比如“如何造车？”，就会发现列出1234这样的步骤，
是不可能的。那是因为，造车太复杂，需要很多协作才能完成。此时面向对象思维就应运而生
'''

'''
面向对象思维
面向对象更加关注的是“软件中对象之间的关系”，是一种“设计者”思维，适合编写大规模程序
面向对象思想更契合人的思维模式，我们首先思考的是“怎么设计这个事物？”，比如思考造车，
我们就会先思考“车怎么设计？”，而不是“怎么按步骤造车而问题”。这就是思维方式的转变
面向对象方式思考造车，发现车友如下对象组成：
1.轮胎 2.发动机 3.车壳 4.座椅 5.挡风玻璃
为了便于协作，我们找到轮胎厂完成制造轮胎的步骤，发动机厂完成制造发动机的步骤；这样，
发现大家可以同时进行车的制造，最终进行组装，大大提高了效率，但是，具体到轮胎厂的一个流水线操作，
仍然是有步骤的，还是离不开面向过程思想
因此，面向对象可以帮助我们从宏观上把握，从整体上分析整个系统。但是，具体到实现的微观操作（就是一个个方法），
仍然需要面向过程的思路去处理
面向对象和面向过程是相辅相成的，面向对象离不开面向过程
面向对象的思考方式：遇到复杂问题，先从问题中找名词（面向过程更多的是找动词），然后确立这些名词哪些可以作为类，
再根据问题需求确定类的属性和方法，确定类之间的关系
'''

'''
面向对象和面向过程的总结
1、都是解决问题的思维方式，都是代码组织的方式
2、解决简单问题可以使用面向过程
3、解决复杂问题：宏观上使用面向对象把握，微观处理上仍然是面向过程
'''
