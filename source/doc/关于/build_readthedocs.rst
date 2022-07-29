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
5. 支持导出PDF，排版易阅读。


基本实践步骤
----------------
.. note::
   做一个基本的操作步骤说明，希望对大家有帮助。

1. 新建目录，这里为：my_books并进入目录
   > $ mkdir my_books
   > $ cd my_books 
2. 安装工具 Sphinx
   > pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sphinx
3. 使用Sphinx初始化文档目录

  > sphinx-quickstart

       .. image:: images/sphinx-start.jpg

  > ls  初始化后的内容
      - Makefile 
      - build   
      - make.bat source



--------------

-  更多了解\ `Mason`_
-  E-mail: hanghangli@aliyun.com

.. _Mason: https://lihanghang.top/