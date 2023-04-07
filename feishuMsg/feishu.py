# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 添加所需的运行库
import requests,json,hmac,urllib,time,base64,hashlib,sys

# 加签
def Signature_Url(webhook_url,secret):
    # 生成当前时间戳，单位是毫秒，与请求调用时间误差不能超过1小时
    timestamp = str(round(time.time() * 1000))
    # 修改编码格式为utf-8
    secret_enc = secret.encode('utf-8')
    # 将timestamp和secret合并
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    # 修改编码格式为utf-8
    string_to_sign_enc = string_to_sign.encode('utf-8')
    # 将字段进行加密，加密类型采用sha256
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    # 生成请求的URL，WebHook地址
    Post_Url = ("%s&timestamp=%s&sign=%s" % (webhook_url, timestamp, sign))
    return Post_Url

# 发送消息
def DingMessage(Post_Url,Content):
    # 构建请求头部
    header = {
        "Content-Type": "application/json",
    }
    # 构建请求数据
    message ={
        "msg_type": "text",
        "content": {
            "text": Content['test']
        },
        "subject": {
            'text': Content['test']
        }
    }
    # 对请求的数据进行json封装、定义头部文件并发送请求
    info = requests.post(url=Post_Url,data=json.dumps(message),headers=header)
    # 判断是否发送成功
    if json.loads(info.text)['code'] == 0:
        print("发送成功!")
    else:
        print(json.loads(info.text))


senders = {}

def register(key: str, value: str):
    senders[key] = value
    print(senders)

register('feishu', 'webhook')


if __name__=="__main__":
    # 群机器人webhook链接
    webhook_url = "https://open.feishu.cn/open-apis/bot/v2/hook/b9b9eaf0-1c98-4faf-931d-acc27e4f8b06"
    access_token = "****************************************************************"
    # 密钥，机器人安全设置页面，加签一栏下面显示的SEC开头的字符串
    secret = '123'   # authcode
    # 需要发送的消息
    Content = {}
    Content['test'] = "feishu test"
    Content['time'] = "0322"
    
    # 是否@所有人,是输入True否则False
    People = 'cao'
    # 调用DingMessage填入需要传递的参数发送消息
    # 格式：python DingTalk_Alarm.py 发送的消息 True
    DingMessage(webhook_url,Content)
    
