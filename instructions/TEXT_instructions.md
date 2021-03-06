# TEXT

TensorBoard 的[TEXT](instructions/TEXT_instructions.md)栏目显示文本。

class SummaryWriter 中用于打点文本数据的成员函数为`add_text`。

函数 `add_text` 的定义与实现均在
文件[../tb_paddle/summary_writer.py](../tb_paddle/summary_writer.py) 中。

## Class SummaryWriter 的成员函数 add_text

Demo-1 add\_text-demo.py

```python
# coding=utf-8
from tb_paddle import SummaryWriter

writer = SummaryWriter('./log')

for step in range(10):
    text = 'The text support the markdown format.  \nThis is line ' + str(step)  
    writer.add_text('LSTM', text, step)
    writer.add_text('rnn', text, step)

writer.close()

```

执行以下指令，启动服务器：

```
python add_text-demo.py
tensorboard --logdir ./log/ --host 0.0.0.0 --port 6066
```

打开浏览器地址 [http://0.0.0.0:6066/](http://0.0.0.0:6066/)，即可在tensorboard的**TEXT**栏目中查看文本：

<p align="center">
<img src="../screenshots/add_text.png" width=600><br/>
图1. add_text - 显示文本 <br/>
</p>

**注:** Tensorboard 的 text 使用 markdown 的解析方式。如果需要换行，则需要在 `\n` 前添加两个空格，例如

```
line_1  \nline2  \nline3
```
