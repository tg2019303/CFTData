# 动态蹭饭图精准POI定位

本项目是<https://github.com/tg2019303/tg2019303.github.io/>的辅助代码库。

挣扎了很久还是打算把它开源出来。
这是一个简陋的工具，没有命令行参数，与数据在同一个目录

|姓名|大学|专业|电话|css类|个性HTML|
|:--:|:--:|:--:|:--:|:--:|:--:|
|赵六|华东师范大学|外国语言文学|88888888883||&lt;li&gt;赵六&lt;img style=\"position:absolute\" width=\"50px\" src=\"data/TG2019303/crown.gif\"/&gt;&lt;ul&gt;&lt;li&gt;专业：一流专业&lt;/li&gt;&lt;li&gt;电话：12345678901&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;|

## 各文件功能简单介绍
### csvpatch.py
- 当前目录没有`data.json`时，根据`data.csv`创建并填上同学对应的HTML
- 已经存在时，重填同学对应的HTML，不影响大学定位结果
### get_poi.py
根据POI定位高校。
### release_json.py
生成单行数据文件`release.json`
### encrypt.html
使用AES加密`release.json`
### example_json.py
生成访客数据文件`dataExample.js`
### config.py
装装样子的配置文件
```python
AK = '您的AK'
```