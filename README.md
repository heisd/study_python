# Python 基础学习与 C/C++ 对照

记录 Python 入门阶段的语法练习。源码注释以 Python 3.10 为学习环境，并穿插与 C/C++ 的对比，适合已有 C 语言经验、希望理解 Python 写法的人按主题阅读。

## 文件导航

| 文件 | 内容 |
| --- | --- |
| [hello.py](./hello.py) | 入门脚本 |
| [easy_python.py](./easy_python.py) | 标识符、关键字、缩进、输入、字符串及与 C/C++ 的语法对照 |
| [numer_type.py](./numer_type.py) | 数值类型练习，文件名保留原拼写 |
| [python_operator.py](./python_operator.py) | 运算符相关练习 |
| [type_change.py](./type_change.py) | 类型转换 |
| [circular_function.py](./circular_function.py) | 循环与函数相关练习 |
| [math_function.py](./math_function.py) | 数学函数 |
| [random_num.py](./random_num.py) | 随机数 |
| [python_Interpreter.py](./python_Interpreter.py) | 解释器相关记录 |

这些是独立学习文件，不是一个按模块打包安装的 Python 应用，也没有统一启动器。

## 环境准备

准备 Python 3，建议先使用与学习注释一致的 3.10 环境核对行为：

```bash
git clone --branch main https://github.com/heisd/study_python.git
cd study_python
python --version
python hello.py
```

在部分 macOS/Linux 环境中，将 `python` 替换为 `python3`。仓库未提供锁定依赖版本的配置；遇到额外导入时，应根据对应脚本单独检查，不必为了阅读全部笔记一次性配置复杂环境。

## 推荐学习顺序

1. 从 `hello.py` 熟悉运行脚本与终端输出。
2. 阅读 `easy_python.py`，理解缩进、关键字、变量和字符串操作。
3. 对照数值类型、运算符和类型转换脚本。
4. 继续学习循环、函数、数学函数和随机数。
5. 修改小段代码并记录输入与输出，再与注释中的 C/C++ 示例比较。

`easy_python.py` 内容较长，既有代码也有对照说明。建议分段阅读，不必把整份文件一次运行的输出当作一套自动化测试结果。

## 交互与运行行为

例如：

```bash
python easy_python.py
python type_change.py
python random_num.py
```

部分脚本调用 `input()`，会等待终端输入；`help()` 可能进入分页帮助界面，通常可按 `q` 退出后继续运行。推荐使用能交互输入的终端，而不是只显示输出的编辑器面板。

## 学习时需要区分的概念

- Python 的缩进属于语法，不能按 C/C++ 的大括号习惯随意移动。
- 动态类型、字符串处理与复数写法可以用来做语言比较，但两种语言的库函数和运行模型并非逐项等价。
- 文件中保留了学习过程中的解释，跨语言结论应结合语言文档与实际例子验证。

## 常见问题

| 问题 | 检查方式 |
| --- | --- |
| `python` 命令不存在 | 确认已安装 Python，或尝试 `python3` |
| 程序停在某处没有输出 | 查看是否在等待 `input()` 或帮助分页输入 |
| 中文乱码 | 使用 UTF-8 源文件与支持中文的终端 |
| 修改后报缩进错误 | 检查空格和 Tab 是否混用 |
| 不同运行结果 | 随机数脚本可能每次生成不同值 |

本仓库保留个人学习过程，重点是读懂并修改示例；并未声明所有文件已在全部 Python 版本和操作系统下通过测试。
