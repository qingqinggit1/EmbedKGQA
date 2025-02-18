#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2022/4/13 3:43 下午
# @File  : test_lstm_qa1.py
# @Author: jinxia
# @Contact : github: jinxia
# @Desc  : LSTM+ComplEx 问答模型的客户端，进行测试


import unittest
import requests
import time, os
import json
import base64
import random
import string
import pickle
import sys
import pandas as pd

class qaTestCase(unittest.TestCase):
    # 确保Flask server已经启动

    # host_server = f'http://192.168.10.242:9966'
    host_server = f'http://127.0.0.1:9966'
    def test_lstm_qa4(self):
        """
        给定的问题是字符串格式：    text = '市财政局存在哪些审计问题'
        答案：
        :return:
        :rtype:
        """
        url = f"{self.host_server}/api/qa_predict"
        # text = '市财政局存在哪些问题'
        # text = '市审计局审计了谁'
        params = {
                    "sender": "0001_2",
                    "message": "市财政局存在哪些问题"
                    # "message": "xdsaf"
                 }
        # params = {'text': text}
        headers = {'content-type': 'application/json'}
        r = requests.post(url, headers=headers, data=json.dumps(params), timeout=360)
        result = r.json()
        print(result)
        assert r.status_code == 200
        assert result is not None, "返回结果为None"
        # 检查结果，里面肯定是字典格式
        print("对数据接口测试完成")
    def test_lstm_qa_noanswer(self):
        """
        给定的问题是字符串格式：    text = '市财政局存在哪些审计问题'
        答案：
        :return:
        :rtype:
        """
        url = f"{self.host_server}/api/qa_predict"
        # text = '市财政局存在哪些问题'
        # text = '市审计局审计了谁'
        params = {
                    "sender": "0001_2",
                    # "message": "市财政局存在哪些问题"
                    "message": "xdsaf"
                 }
        # params = {'text': text}
        headers = {'content-type': 'application/json'}
        r = requests.post(url, headers=headers, data=json.dumps(params), timeout=360)
        result = r.json()
        # assert result['custom']['content'] == ' 该问题暂时无法回答', f"无法回答的问题进行验证失败"
        print(result)
        assert r.status_code == 200
        assert result is not None, "返回结果为None"
        # 检查结果，里面肯定是字典格式
        print("无法回答的问题进行验证数据接口测试完成")


if __name__ == '__main__':
    ##确保Flask server已经启动
    unittest.main()

