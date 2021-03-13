# Python基础知识
> 开发口头禅：“Don’t Repeat Yourself”

> coding env: python3.6+
## 书籍推荐
1. 《流畅的Python》
    - 能够解决大部分疑难杂症
2. 《[python3 cookbook](https://python3-cookbook.readthedocs.io/zh_CN/latest/index.html)》 
3. 《[python 进阶](https://docs.pythontab.com/interpy/#python)》  深入python语法等  
4. 《[编写高质量代码改善 Python 程序的 91 个建议](https://l1nwatch.gitbook.io/writing_solid_python_code_gitbook/di-1-zhang-yin-lun)》 
5. 《python Cookbook》 
## 第一部分 编码规范
> 良好的习惯我们就从最开始刻意练习，让我们的代码也要同翻译的三字标准一样：**信、雅、达**。这里记录我认为比较好的习惯吧，供大家参考使用。
1. 缩进规范
    - 使用**纯空格**缩进，不要Tab、不要空格与Tab混用。
2. **导包规范**
    + 尽量避免 import *，如果要导入一个命名空间下的多个方法，可使用import test_class，再使用test_class.func的方式
    + 顺序问题。标准库 》第三方库 》本地库
3. 命名规范
    + 命名要尽量达意！长一点倒不怕，就怕他人看到名字不能很快了解其含义。比如表示订单数量：num、order_num 你说哪个好！

4. 对于嵌套处理尽量不要超过4层。比如for与if的嵌套，按照我的经验这类代码肯定是有优化空间，可以从Python自身的一些好用特性和业务逻辑本身两个角度与优化。
## 第二部分 基础知识 
> 基础不牢，地动山摇。

## 第三部分 进阶知识 
> 攀登高峰的脚步👣不能停下来，向前进……。主要包含python的高阶函数使用及技巧。
1. 产生随机字典、集合（一般在测试代码时使用）
    + 主要使用random包中的randint模块
    ```python
    #!/usr/bin/env python3
    from random import randint

    # generate dict
    d = {"name%d" % n :randint(10, 30) for n in range(10)}
    # generate set
    s = {randint(10, 30) for _ in range(10)}
    ```
2. 集合的求交集操作
    + key points: keys() of dict、func map, reduce
    + 把函数作为结果返回的函数是高阶函数：map、filter、reduce（py3已不再内置）、sorted、all etc.
    + map 函数：把函数应用到各个元素上，生成一个新序列。
    + reduce 函数：把一系列值归约成单个值。第一个参数是接受两个参数的函数，第二个参数是一个可迭代的对象。看下一个例子：

    ```python
    from functools import reduce

    # example： reduce 
    reduce(func, iterable)：reduce(lambda a, b: a * b, range(1, 5))
    >>> 24
    ```

    ```python
    from random import randint, sample
    from functools import reduce

    # random generate three dict
    s = 'china'
    d1 = {k: randint(2, 5) for k in sample(s, randint(4, 7))}
    d2 = {k: randint(2, 5) for k in sample(s, randint(4, 7))}
    d3 = {k: randint(2, 5) for k in sample(s, randint(4, 7))}
    # 求以上三个字典的公共键：使用map、all
    d1 = [d1, d2, d3]
    [k for k in d1[0] if all(map(lambda d: k in d, d1[1:]))]
    >>> ['o']

    # 使用集合运算求交集：reduce。使用场景：存在多个自典时。
    reduce(lambda dict1, dict2: dict1 & dict2, map(dict.keys, d1))
    >>> {'o'}
    ```

3. 枚举、命名元组模块

4. 

## 第四部分 高阶知识
> 会当凌绝顶，一览众山小。
### 一切皆对象（包括类和函数）
    ```python
        def func_1(name='zhang'):
            print(name) 

        def func_2():
            return func_1
        # return func
        new_inst = func_2() # 返回一个函数
        new_inst('li')
    ```
### 类型、对象和类

### 元编程
> 还记得咱们的开发口头禅吗？对就是“don’t repeat yourself”，Python自身也为我们开发人员提供了一种实现方式，即元编程，目的就是减少重复性代码，主要技术是使用装饰器、类装饰器和元类。
1. 装饰器
    + 场景1: 在系统中大多数的模块都有日志打印、时间统计等功能。
### 多线程
1. 先要知道GIL（Global Interpreter Lock），Python的一把全局解释锁
### 协程
> 协程（Coroutine），又称微线程
## 第五部分 性能优化
1. [性能优化参考之一](https://www.ibm.com/developerworks/cn/linux/l-cn-python-optim/)
## 第六部分 思考和总结
> 不忘初心，方得始终，回望过去，是为了更好走向远方。

## python小应用
> 总结工作中可能用到的业务功能。
