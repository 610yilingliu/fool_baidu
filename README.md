# 百度网盘mp3数字签名修改工具(防和谐)

## 原理
将MP3的commet(说明)改成"sb baidu", 改变原有文件md5码达成暂时不被检测的效果.

不清楚能否100%奏效并维持一段时间,就目前百度网盘处理txt,zip等文件的方式来看应该是同md5的文件被举报后直接从服务器删除(同一个md5文件仅会在服务器存储一次,之后无论有多少人上传下载多少次也只有这一个文件)

Change mp3 commet to to "sb baidu" to change its md5 code.

## Environment:
Python 3.7.6

## Extra Requirements

[mp3_tagger] (https://github.com/artcom-net/mp3-tagger)


## Usage

Put mp3 files in the same folder of the script and run the script.