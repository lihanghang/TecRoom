基于ReadtheDocs托管在线知识库的步骤
=============================================
.. note::
   更新日期：2022-08-01


Abuout Hang's Tec Room
----------------------------
本文主要为想使用ReadtheDocs构建在线知识库的小伙伴提供一个参考步骤，我在用这个工具之前尝试了比较多的网站来记录一些笔记，但是感觉还是不到位，
Hang's Tec Room 是基于目前的工具构建的，用起来虽然有些门槛，但只要多练习下就能很快掌握。具体有以下特点：

1. 工具：Sphinx
2. 托管地址：ReadtheDocs
3. 支持rst和md格式的文档，md还是很常用，编写起来也容易。
4. 基于github或gitlab进行代码管理，推送后ReadtheDocs自动进行构建和发布。
5. 支持导出PDF，自动排版，易阅读。


基本实践步骤(QuickStart)
--------------------------
.. note::
   做一个基本的操作步骤说明，希望对大家有帮助。

1. 新建目录，这里为：my_books并进入目录
  
  .. code-block:: bash

   $ mkdir my_books
   $ cd my_books 

2. 安装工具 Sphinx

   ``$ pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sphinx``

3. 使用Sphinx初始化文档目录

   $ sphinx-quickstart

       .. image:: images/sphinx-start.jpg

   初始化后的内容
      .. code-block:: bash

         >>> ls
         Makefile 
         build    # 存放编译后的文件
         make.bat # win下编译脚本
         source # 文件目录

4. 每次发生文档变动后进行编译，生成后的文件放在build/html目录下
    - macos:

      ``$ make html``
    - win: 

      ``$ ./make.bat html``
5. 选择发布的网站主题
   - `主题网站 <https://sphinx-themes.org/>`_ ，我这里选择比较常见的Read the Docs
   - `效果图 <https://sphinx-themes.org/sample-sites/sphinx-rtd-theme/>`_

   - install theme
      ``$ pip install sphinx-rtd-theme``
   - set configure `conf.py` file , 位置：my_books/source/conf.py # line 81
      $ html_theme = 'sphinx_rtd_theme'
6. 生成依赖文件，服务于在readthedoc托管文档时自动构建，在根目录下生成
      ``$ python -m pip freeze > requirements.txt``

7. 将代码仓库在github管理 

   .. code-block:: bash
      
      $ git init
      $ git add .
      $ git commit -m "init my books code"
      $ git push

8. readthedoc网站托管--建立GitHub代码仓库与readthedocs的关联
  
   - 大家可直接 `参考官方步骤 <https://docs.readthedocs.io/en/stable/tutorial/>`_

9. 至此，从sphinx的安装，主题选择，再到推送到github，建立与readthedocs的关联就完成了。

10. 后续就是具体的文档编写，大家可以多看看rst的语法内容，也可以使用markdown语法去编写文档。
   
.. tip::  
   在source目录下进行文档编写，编写完成后进行make html编译操作，再推送github，构建由readthedocs自动完成。


谈谈题外话
--------------

::
   可以将此网站作为自己的日常生活或工作总结的地方，梳理总结的有价值的地方作为经验沉淀下来。对于工作多说一些，建议大家建立自己完整的知识体系，然后不断完善这个体系，这样有助于在我们工作，学习中不容易迷失方向。
   最后，如果自己的输出能有一些帮助到别人的部分也是很有价值的！

--------------

-  更多了解\ `Mason`_
-  E-mail: hanghangli@aliyun.com

.. _Mason: https://lihanghang.top/