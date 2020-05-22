# python
> 开发口头禅：“Don’t Repeat Yourself”
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
> 攀登高峰的脚步👣不能停下来，向前进……。

## 第四部分 高阶知识
> 会当凌绝顶，一览众山小。
### 元编程
> 还记得咱们的开发口头禅吗？对就是“don’t repeat yourself”，Python自身也为我们开发人员提供了一种实现方式，即元编程，目的就是减少重复性代码，主要技术是使用装饰器、类装饰器和元类。
1. 

### 多线程
1. 先要知道GIL（Global Interpreter Lock），Python的一把全局解释锁

### 协程
> 协程（Coroutine），又称微线程
1. 
## 第五部分 性能优化
1. [性能优化参考之一](https://www.ibm.com/developerworks/cn/linux/l-cn-python-optim/)

## 第六部分 思考和总结
> 不忘初心，方得始终，回望过去，是为了更好走向远方。