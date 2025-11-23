# show eudic（自动欧路查词）

自动将某个field中的字段放入eudic进行查询。 
安装使用详见：https://ankiweb.net/shared/info/1660656659?cb=1763809325611

改自https://[ankiweb.net/shared/info/1525025114](http://ankiweb.net/shared/info/1525025114) 

## 配置： 

1. 在配置内修改需要翻译的field；
工具->show eudic->插件设置

"answerField": "Word",   Word修改为需要查询的field， 如果这里添加会在显示答案时查词

"questionField": ""  如果这里添加会在正面提示时就查词
"questionField": "Front", The name of the field to copy to the clipboard when the question side of the card is shown. Case sensitive. If you don't want to copy, set to a blank string.

"answerField": "" The name of the field to copy to the clipboard when the answer side of the card is shown. Case sensitive. If you don't want to copy, set to a blank string.

2. 将欧路词典的安装路径加入到环境变量中。

