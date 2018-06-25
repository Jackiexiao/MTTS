# 语音合成测试语料库
目标是设计1000句左右的测试语料，包含多方面考察点，以便用于合成语音的评价和分析。

## 基本要求

* 尽可能覆盖所有发音
* 覆盖发音字，轻声，儿话音，上声单音节
* 包含一些生僻字
* 标注韵律
* 覆盖所有语气类型，陈述句，疑问句，感叹句，祈使句等等
* 覆盖常见的不同说话场景：新闻，日常对话，演讲等
* 覆盖分词测试，例如人名，地名
* 包括汉语中参见的英文缩写发音，度量单位，数字串
* 包含英语和汉语两种语言的测试语料
* 变调规则，例如两个三声连着读第一个字读二声 todo



## 汉语部分

```
101 向#1香港#2特别#1行政区#1同胞，#4澳门#2和#1台湾#1同胞#2海外#1侨胞
102 向#1香港#2特别#1行政区#4同胞，#4澳门#1和#1台湾#1同胞#4，海外#3侨胞
103 向香港特别行政区同胞，澳门和台湾同胞，海外侨胞，致以诚挚的问候和良好的祝愿
104 这#1两批#1货物#2都打折出售#4，严重#2折本#3，他#1再也#2经不起#1这样折腾。
105 他#1每次#2出差#3，差不多#1都要#1出点#1差错。
106 广州市#1明天#2多云转晴。
107 江南、#3华南#1东部#3以及#1四川、#3重庆、#1湖北#3有#1小到#1中雨
108 呵呵#3，我不知道诶#4，我现在#1什么#1都不想说。		
109 一二三四五六七八九十十一十二一百两千三万四亿五兆六六六
110 六百#1九十一万#2三千零一元
111 啊！欸？恩。好。额。哼！喵喵。
112 姑姑舅舅#3，这个#1哑巴#3在打量#1我，真不是个东西！
113 爹爹#1明白#1之后#3，鸡皮疙瘩#2都起来了。
114 后面#1住的#3都是#1什么#1人？
115 难道#3咱们#1就#1一点#1盼望#3也没#1有了吗？
116 猩猩#1中弹#2之后#1动弹不得。
117 立定！不许胡说！找个地方坐下！
118 老风刀勾亏丑工光女扑虫书乒乓鸟
119 房客#2有时#2想要#1早餐#4，有时#1想要#1大床房#3，如果#2比较#1好一#1点的，就#1先预留#1给他们。让他们#1可以#2先到一旁#1坐着#1等候#4。我们#1一会#2就可以#1安排好。
120 美国会通过对台售武法案。
121 体重128斤的小明手机是1289025621，他现在在乘坐G128列车。
122 KFC，ATM，CNN。
123 八百标兵奔北坡，北坡炮兵并排跑，炮兵怕把标兵碰，标兵怕碰炮兵炮。
124 吃葡萄不吐葡萄皮儿，不吃葡萄倒吐葡萄皮儿。
125 我和林小兰打算过去广州番禺天和服装厂
126 吴小姐和曾先生曾经去过那里
```

### 说明
```
101 韵律
102 不同韵律
103 无韵律
104 多音字测试：打折（zhé），折（shé）本，折（zhē）腾。
105 多音字测试：出差（chāi）差（chà）不多差（chā）错
106 天气
107 天气
108 日常对话&带情感
109 数字串
110 数字串
111 语气词
112 轻声：姑姑 舅舅 哑巴 打量 东西
113 轻声：爹爹 明白 疙瘩 
114 疑问句
115 疑问句
116 多音字：中弹（dan4）动弹（tan3）
117 祈使句：立定！不许胡说！找个地方坐下！
118 儿话音
119 长句&日常对话
120 中文分词歧义：既可以切分成“美国/会/通过对台售武法案”，又可以切分成“美/国会/通过对台售武法案”
121 数字规范化：小明体重是128斤”中的"128"应该规范为"一百二十八"，而"G128次列车”中的"128"应该规范为“一二八”，而电话中却读作幺二八
122 英文缩写：KFC，ATM，CNN。
123 绕口令
124 绕口令
125 分词中的人名和地名
126 分词与多音字
```
## English 
reference: [google tacotron2 example]
(https://github.com/google/tacotron/tree/master/publications/tacotron2)
```
201 Generative adversarial network or variational auto-encoder.
202 Basilar membrane and otolaryngology are not auto-correlations.
203 He has read the whole thing.
204 He reads books
205 Don't desert me here in the desert!
206 He thought it was time to present the present.
207 Thisss isrealy awhsome
208 This is your personal assistant, Google Home.
209 This is your personal assistant Google Home.
210 The buses aren't the problem, they actually provide a solution.
211 The buses aren't the PROBLEM, they actually provide a SOLUTION.
212 The quick brown fox jumps over the lazy dog.
213 Does the quick brown fox jump over the lazy dog?
214 She sells sea-shells on the sea-shore. The shells she sells are sea-shells I'm sure.
215 Peter Piper picked a peck of pickled peppers. How many pickled peppers did Peter Piper pick?
```

### explanation
```
201 out-of-domain and complex words
202 out-of-domain and complex words
203 polyphone
204 polyphone
205 polyphone
206 polyphone
207 spelling errors
208 punctuation
209 punctuation
210 stress and intonation
211 stress and intonation
212 declarative sentences
213 interrogative sentences
214 tongue twisters
215 tongue twisters
```

