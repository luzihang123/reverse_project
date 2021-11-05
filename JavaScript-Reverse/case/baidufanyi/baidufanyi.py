# -*- coding:utf-8 -*-
# @Author: 聆风clark
# @Time: 2021/11/5 11:46 上午
# @File: baidufanyi.py
# @project demand:复现 https://blog.csdn.net/kdl_csdn/article/details/119419865
import re
import execjs
import requests
from loguru import logger

index_url = 'https://fanyi.baidu.com/'
lang_url = 'https://fanyi.baidu.com/langdetect'
translate_api = 'https://fanyi.baidu.com/v2transapi?from={lang}&to=en'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh,zh-CN;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=FAD5BA8758B927BD8315752FB2962071; PSTM=1549097115; BAIDUID=2AA34448D5DB2AF0CED81AA547CB260E:FG=1; __yjs_duid=1_9bbc922d476c82116cd7b069b9f189701619669323989; H_WISE_SIDS=107311_110085_127969_128698_131423_146872_154619_165136_165517_166148_168388_169066_170816_170873_170936_171573_172643_173017_173124_173615_173829_174035_174180_174448_174649_174661_174665_174682_174695_175212_175275_175284_175365_175450_175667_175678_175755_175797_175948_175974_176130_176157_176262_176339_176346_176380_176398_176418_176562; MCITY=-289%3A; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID_BFESS=4FAA7025CBD7222DB6A4BF810CE1B36D:FG=1; BAIDU_WISE_UID=wapp_1635935016306_472; BDRCVFR[shF0fZW8Lss]=mk3SLVN4HKm; delPer=0; H_PS_PSSID=31254_26350; PSINO=5; BDUSS=hVczZaSm1DQ245eDVVcjVTNjBhTWV6dGFaUHl3Y1dZOUUyRXVjblZnYkotNnBoSVFBQUFBJCQAAAAAAAAAAAEAAAB0PL6q19PW8fH2t-cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMlug2HJboNhSD; BDUSS_BFESS=hVczZaSm1DQ245eDVVcjVTNjBhTWV6dGFaUHl3Y1dZOUUyRXVjblZnYkotNnBoSVFBQUFBJCQAAAAAAAAAAAEAAAB0PL6q19PW8fH2t-cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMlug2HJboNhSD',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_token():
    response_text = requests.get(url=index_url, headers=headers).text
    token = re.findall(r"token: '([0-9a-z]+)", response_text)[0]
    return token


def get_sign(query):
    with open('baidu_encrypt.js', 'r', encoding='utf-8') as f:
        baidu_js = f.read()
    sign = execjs.compile(baidu_js).call('e', query)
    return sign


def get_result(lang, query, sign, token):
    data = {
        'from': lang,
        'to': 'en',
        'query': query,
        'domain': 'common',
        'simple_means_flag': '3',
        'sign': sign,
        'token': token,
    }
    response = requests.post(url=translate_api.format(lang=lang), headers=headers, data=data)
    print(response.json())
    result = response.json()['trans_result']['data'][0]['dst']
    return result


def main():
    query = input('请输入要翻译的文字:')
    response = requests.post(url=lang_url, headers=headers, data={'query': query})
    lang = response.json()['lan']
    logger.debug(lang)
    token = get_token()
    sign = get_sign(query)
    logger.debug(f"{token} {sign}")
    result = get_result(lang, query, sign, token)
    print(f"翻译成英文的结果为:{result}")


if __name__ == '__main__':
    main()
