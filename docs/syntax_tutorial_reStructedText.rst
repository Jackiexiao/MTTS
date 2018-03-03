reST的语法教程

* 推荐阅读 https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html#rst-primer
* 不同轻量标记语言的异同整理 http://www.worldhello.net/gotgithub/appendix/markups.html


title 1
=====================


title 2 
----------------------

title 3 
~~~~~~~~~~~~~~~~~~~~~~

title 4 
^^^^^^^^^^^^^^^^^^^^^^^^

title 5 
++++++++++++++++++++++++++++++

**粗体**
*斜体*

| 星号旁边没有空格就无法显示**粗体**和*斜体*是这样的
| 星号旁边有空格就显示 **粗体** 和 *斜体* 是这样的

下面是一条分隔线

------------------

上面是一条分隔线

**上下标的表示**

斜杠后面必须有空格，传入的上标或者下标文字必须用反引号标起来，:sup: 后面接文字时不能有空格
 * H\:sub:2 \O
 * H\ :sub:`2`\O
 * E = mc\ :sup: `2`
 * E = mc\ :sup:`2`

**换行**
    听说可以用 | ，但是我发现跟缩进没什么不同

**无序列表**
    可以用 * 但是*右侧必须有空格

* 第一项
    + 无序列表
    + 啦啦啦
* 第二项
* 第三项

**有序列表**
    1. one
        A. A
        B. B
            a. 1
            b. 2
                i) haha
                ii) lala
    #. two
    #. three

**代码块** 注意::这个符号和代码之间也要有空行

::

    $python3 text.py

**高亮代码块** `.. code-block::空格python` 才能正确显示，中间空格少了不显示

.. code-block:: python
    :linenos:

    def foo():
        pass

**普通表格**

+-------+-------+-------+
| head1 | head2 | head3 |
+=======+=======+=======+
| one   | two   | three |
+-------+-------+-------+
| one   | two   | three |
+-------+-------+-------+

表格必须严格对齐，否则无法显示，比如下面的这个，注意文字和表格之间必须要有空行

**简单表格**

必须是=号，rst的表格都非常的娇贵，如果表格内文本没有对齐就无法正确显示

==== ==== ====
input     output
--------- ----
h1   h2   h3 
==== ==== ==== 
one  two  three
one  two  three
one  two  three
==== ==== ==== 

**链接到其他章节的方法**

在其他章节的头部加入 `.. _chapter1index:` 然后在此代码为 `:ref:`第一章 <chapter1index>` `

:ref:`第一章 <chapter1index>`

**超链接**

- 访问 `Google <http://google.com/>`_ 。
- 上面已定义，直接引用 google_ 链接。
- 链接地址在后面定义，如： GitHub_ 。
- 反引号括起多个单词的链接。如 `my blog`_ 。

.. _GitHub: http://github.com
.. _my blog: http://www.worldhello.net

**清空标记空白**

标记符号前后空白\
用\ **反斜线**\ 消除


**引言**

`Got GitHub` by Jackie Xiao.

**等宽字体&代码**

这是代码 ``code``

**下划线**

.. role:: ul
   :class: underline

:ul:`下划线` 效果

不留白的\ :ul:`下划线`\ 效果

**删除线**

.. role:: strike
   :class: strike

:strike:`删除线` 效果

不留白的\ :strike:`删除线`\ 效果


**加入图片的方法** 

.. figure:: /img/github.png
   :width: 32

   图：GitHub Octocat

- GitHub Logo: |octocat|
- 带链接的图片：
  |imglink|_
- 下图向右浮动。
   .. image:: /img/github.png
      :align: right

.. |octocat| image:: /img/github.png
.. |imglink| image:: /img/github.png
.. _imglink: https://github.com/

**图片跳转**

.. _fig1:

.. figure:: /img/github.png

   内部跳转图例

上面定义的位置，可以：

- 通过 fig1_ 跳转。
- 或者 `点击这里 <#fig1>`__ 跳转。 \` `之后不能有空格
- 或者参见 :ref:`fig1`\ 。
- 或者参见 :ref:`fig1`


**注释**
    ..加上文字就是注释，例如

.. 这是一个注释

**转义符**
    \即为转义符

**脚注**

reST脚注的多种表示法：

- 脚注即可以手动分配数字 [1]_ ，
  也可以使用井号自动分配 [#]_ 。

- 自动分配脚注 [#label]_ 也可以用
  添加标签形式 [#label]_ 多次引用。

- 还支持用星号嵌入符号式脚注，
  如这个 [*]_ 和 这个 [*]_ 。

- 使用单词做标识亦可 [CIT2012]_ 。


.. [1] 数字编号脚注。
.. [#] 井号自动编号。
.. [#label] 井号添加标签以便多次引用。
.. [*] 星号自动用符号做脚注标记。
.. [*] 星号自动用符号做脚注标记。
.. [CIT2012] 单词或其他规定格式。

[todo]不是很理解上面的..是什么意思



