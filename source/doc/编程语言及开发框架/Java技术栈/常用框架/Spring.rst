================
Spring
================
.. note::
    了解一些Spring框架的设计思想和原理，本文记录下学习的笔记。至于应用层面可以：一个项目、一台电脑、一双手去实践吧，框架就是工具
    贵在和具体业务结合应用，工具的目的很简单就是来提高效率（开发、协作、运维等）的。

参考资料
===========
1. 查看 `Spring <https://developer.ibm.com/zh/languages/java/articles/j-lo-spring-principle/>` 框架的设计理念与设计模式分析。

Spring的设计思想
======================
1. 框架基石：Core（道具）、Context（舞台）、Bean（演员）（面向BOP编程,Bean Oriented Programming） 
    - BOP在Spring框架中的地位相当于OOP在编程中的地位。
    - Bean封装的是对象，而对象本身的数据、行为的由Context承载，Context会对Bean之间的关系进行建立和维护，Context是Bean关系的一个集合。
    - IOC容器就是Context中Bean的关系集合。
    - Core为维护Bean之间关系提供一系列的工具。
2. 关键是对象之间依赖关系的管理，Spring提供了配置文件形式来管理，即依赖注入机制。
    - 注入关系是在IOC（IOC，Inversion of Controll）容器中进行管理


