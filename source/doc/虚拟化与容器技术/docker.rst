==========
Docker
==========

书籍推荐
========
访问 `docker_practice <https://www.gitbook.com/download/pdf/book/yeasy/docker_practice>`_ 下载。

初识Docker
============
.. note::

   总的来说，Docker属于运维部署领域。如果是应用者就是熟练的在合适的场景下操作相应的命令；如果是进一步研究其底层原理，那需要的基础就要多些了，比如虚拟化技术。

1. Docker就是开源的容器引擎，诞生于2013年。最形象的比喻就是集装箱，各自自成体系，互不影响，可任意放在不同的平台。
#. Docker是容器的一种，容器是一种轻量级的虚拟技术，相对应的，虚拟机（VMware、VirtualBox等）就是重量级的虚拟技术。
#. 最切实的价值是什么？
    + 项目开发有三大基础环境： 开发环境（程序员）、测试环境（测试人员）、生产环境（运维人员）。
    + 要保持三者环境的统一Docker的优势不明觉厉。举个例子，小王，程序员一枚，在自己电脑上优雅的完成了业务开发。怀着如释重负的心情将代码推送至测试环境，然后休息，进行吃鸡游戏……。突然，测试人员小李发来消息，小王呀，你昨天推的代码不work呀，小王说：不可能！我本地非常work的，你再仔细看看吧……；小李说：我这真没问题。
    + 你看看是不是吃鸡的心情不好了！问题究竟在哪里呢？原来呀小王本地开发环境使用的Python3.7，但是小李所用的测试环境是Python3.6，造成了有些功能不work。如果我们有了Docker，就可以代码+环境保持一致，不再造成上面的尴尬！
#. 可移植。MAC、Win、Linux等平台。
#. 相互隔离。
#. 开销低。

*Docker是一种容器技术，解决软件跨环境迁移的问题！*


Docker架构（组件）
===================
.. important::

    Docker采用C/S架构。Docker客户端（Client）可以通过命令行形式或API来与提供Docker服务（Server）的守护进程进行通信。

基本架构图
----------

.. image:: images/docker/2020-03-06-docker架构.png
  :width: 600px


核心组件
--------
.. important::

    Docker共包含三大核心组件：**镜像（image）、容器（container）、仓库（Repository）**。镜像和容器可以类比面向对象编程中类和实例的关系，image->class、container->instance。仓库可类别代码控制中心，负责存储和共享用户的镜像。

1. Image
    + 一个只读的静态模板。存储容器所需要的环境和应用的执行代码。相当于是一个root文件系统，比如官方镜像Python:3.9就包含了完整的一套Python3.9最小系统的root文件系统。
    + 采用分层机制。
#. Container
    + 一个运行时的环境。镜像是静态的定义，容器是镜像运行时的实体。
    + 容器就相当于集装箱，不关心里面装什么，所有应用都有统一的生命周期：创建、启动、删除、暂停、重启等。
    + 容器也不在乎自己所处的平台。本机、虚拟机、服务器等都可相互移植，对于前面提到的部署都是非常适合的。
#. Repository
    + Docker采用注册服务器来存储和共享用户的镜像。
    + 注册服务器分为公共和私有两种。公共就是官方的Docker Hub，私有就是自己注册一个Docker Hub账号建立自己的私有仓库，便于小范围内的共享。

通过Docker开发和部署的流程图
-----------------------------
.. note::

    利用下图能更好的理解Docker在日常开发、部署中的应用流程和三大组件。

.. image:: images/docker/docker-开发部署流程图.png
    :width: 700

:流程概述: 

- 开发主机上
    1. 创建容器A，创建方法可以手动也可通过Dockerfile文件自动构建。

    .. tip::

        Dockerfile文件后续会讲，这也是最常用的一种构建容器方式。

    2. 容器A必须基于镜像来创建。镜像A就是容器的静态形式，容器是镜像的动态形式。
    3. 将容器A保存为镜像A，然后推送到Docker库进行共享
- 集群环境上
    1. 在Docker库中搜索所需镜像A，并将其拉取到本地。
    2. 拉取后在本地就可以运行容器A了。
    3. 在集群环境中可以运行很多容器，彼此相互独立、互不影响。

安装Docker（MAC)并注册国内镜像加速器
=======================================
.. tip::

    MAC系统可以直接安装桌面版Docker，社区版就够用了。关于镜像加速器推荐使用国内阿里云镜像加速器，配置也比较容易，配置后再使用docker镜像就比较快了。

安装
------
1. 点击 `下载 <https://hub.docker.com/editions/community/docker-ce-desktop-mac/>`_ docker桌面版。
2. 查看docker版本，验证是否安装成功

  .. code-block:: bash

      $ docker -v
      Docker version 19.03.5, build 633a0ea

配置阿里云镜像加速器
---------------------
 :step-1: 使用阿里云或支付宝等账号登录 `阿里云镜像加速器 <https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors>`_ 网站。
 :step-2: 登录后就能看到针对不同操作系统的操作步骤了。如下图所示：

 .. image:: images/docker/2020-03-06阿里云镜像加速器.jpg
    :width: 700px

Docker常用命令
===============
.. note::

    本章是docker知识的重点，基本都是命令。跟着命令敲起你的小键盘吧。

Docker服务（Daemon）相关命令
----------------------------
.. note::

    mac系统下直接点击客户端就启动了docker服务，非常简单。使用Mac系统，就可以跳过这部分内容了。
    为了使本笔记不失一般性，这里使用CentOS进行相关命令演示。

休息一下：你们公司更倾向于选择什么操作系统作为服务器呢？centos、RH、Linux？ why? `知乎 <https://www.zhihu.com/question/19599986>`_ 上有一篇帖子讨论了这个问题。

1. 启动docker服务
      .. code-block:: bash

        $ systemctl start docker
#. 停止docker服务
    .. code-block:: bash

        $ systemctl stop docker
#. 重启docker服务
    .. code-block:: bash

        $ systemctl restart docker
#. 查看docker服务状态
    .. code-block:: bash

        $ systemctl status docker
        ● docker.service - Docker Application Container Engine
        Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; vendor preset: disabled)
        Active: active (running) since 四 2019-12-12 10:06:56 CST; 2 months 24 days ago
        Docs: https://docs.docker.com
#. 开机启动docker服务
    .. code-block:: bash

        $ systemctl enable docker

Docker镜像（Image）相关命令
----------------------------
1. 查看
    .. tip::

        - docker images -q 查看所有镜像ID
        - docker iamges 查看所有镜像信息

    .. code-block:: bash

        $ docker images
        REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
        python              3.8                 f88b2f81f83a        9 days ago          933MB
        nginx               latest              2073e0bcb60e        4 weeks ago         127MB
        ubuntu              14.04               6e4f1fe62ff1        2 months ago        197MB
    .. note::

        可以看到，执行命令后列出了已创建（可能你还没有镜像，列表就为空）的镜像。下面针对表头做一个说明。

        - REPOSITORY： 仓库名称                           
        - TAG：版本号，默认为latest                          
        - IMAGE ID：镜像唯一标识                        
        - CREATED ：创建时间                            
        - SIZE ：镜像所占的虚拟大小                  


#. 搜索 
    .. tip::

        - docker search [name]

    .. code-block:: bash

        $ docker search mysql
        NAME                              DESCRIPTION                                     STARS               OFFICIAL （是否官方）           AUTOMATED
        mysql                             MySQL is a widely used, open-source relation…   9196                [OK]                
        mariadb                           MariaDB is a community-developed fork of MyS…   3274                [OK]                
        mysql/mysql-server                Optimized MySQL Server Docker images. Create…   679                 [OK]
        centos/mysql-57-centos7           MySQL 5.7 SQL database server                   70                          

    | 搜索是联网进行的，列出可用的镜像。官方镜像搜索网站，可以查看下有没有自己想要的版本。

#. 拉取（下载）
    .. tip::
        - docker pull [name]:[tag]
        - 不写tag，则默认为latest
        - 访问 `Docker Hub 镜像网站`_，可以了解更多关于的版本信息。

        .. _Docker Hub 镜像网站: https://hub.docker.com/search?q=&type=image

    .. code-block:: bash

        $ docker pull mysql:5.6
        5.6: Pulling from library/mysql
        6d28e14ab8c8: Pull complete 
        dda15103a86a: Pull complete 
        55971d75ab8c: Pull complete 
        f1d4ea32020b: Pull complete 
        61420072af91: Pull complete 
        30862a48418b: Pull complete 
        c6c2ee3a9a57: Pull complete 
        0f4efadb31df: Pull complete 
        dd931017b211: Pull complete 
        488a86083079: Pull complete 
        921d4bdabca2: Pull complete 
        Digest: sha256:a72a05bcf3914c902070765a506b1c8c17c06400258e7b574965763099dee9e1
        Status: Downloaded newer image for mysql:5.6
        docker.io/library/mysql:5.6

    | 上面的拉取镜像过程就体现了分层。

#. 删除
    .. tip::

        - 单个删除 docker rmi image-id/[name]:[tag]
        - 删除本次所有镜像docker rmi `docker images -q`

    .. code-block:: bash

        $ docker rmi c8078e
        Untagged: mysql:5.6
        Untagged: mysql@sha256:a72a05bcf3914c902070765a506b1c8c17c06400258e7b574965763099dee9e1
        Deleted: sha256:c8078e8ab06d8dabd6c30cffb03951fa035d85f75c19a83ace29b01cb3ecd272