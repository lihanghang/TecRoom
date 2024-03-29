===============
设计模式
===============

update: 2022-08-13

.. note::
    - 设计模式比较抽象，都是思想层面的，仅仅是归纳总结的软件设计思路，不是万灵药，切不可生搬硬套。设计模式的目的就是为了是软件系统各功能更灵活、架构清晰、协同性好、可维护性、可扩展性等只要能达到这些目的你的设计模式（抽象类）就是值得点赞的！
    - 还是要有一定的实际的工程的经验再看设计模式，这样容易产生共鸣，不然它可能不是心目的样子，看着它没感觉。

资源推荐
============
1. 《大话设计模式》
2. 《设计模式-可复用**面向对象**软件的基础》（经典）
3. 设计模式 `视频课程 <https://www.bilibili.com/video/BV1kW411P7KS>`_

** Gong of Four 23(GOF 23) 四个人总结了23种设计原则模式 **

.. note::
    推荐两本书，可以看看。第二本书比较全面讲了23种模式，可作为日常完善所需，总体划分了三大类型：创建型、结构型、行为型。

知识框架图
==============

.. image:: images/design_pattern.png

初识设计模式
====================
什么是设计模式？
-------------------
1. 定义
    + 对用来在特定场景下解决一般设计的问题的类和相互通信的对象的描述。
2. 模式四要素
    1. 模式名称(P)。
    2. 问题(I)。
    3. 解决方案（S)。
    4. 效果（C)。 

OOP（面向对象）七大原则 
------------------------
.. note::
    作为架构设计的七大原则

1. 开闭原则：对扩展开放，对修改关闭。
2. 里氏替换原则：继承必须确保超类所拥有的性质在子类中仍然成立。
3. 依赖倒置原则：要面向接口编程，不要面向实现编程。
4. 单一职责原则：控制类的粒度大小，将对象解耦，提高其内聚性。
5. 接口隔离原则：要为各个类建立它们需要的专用接口。
6. 迪米特法则：只与你的直接朋友交谈，不跟“陌生人”说话。
7. 合成复用原则：尽量先使用组合或者聚合等关联关系来实现，其次才考虑使用继承关系来实现。

创建型（5）
==============  
工厂方法
-------------------
抽象工厂
-------------------
1. 超级工厂

生成器
-------------------
原型
-----------
单件
-----------


结构型（7）
=============

适配器
--------
桥接
-----
组合
-----
装饰
-----
外观
-----
享元
-----
代理
-----

行为型（11）
==================

职责链
---------
命令
-----
解释器
--------
迭代器
--------
中介者
--------
备忘录
--------
观察者
--------
状态
--------
策略
--------
模板方法
--------
访问者
--------