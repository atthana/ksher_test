#encoding: utf-8
import urllib
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen
import json
import time
import datetime
from random import Random
import rsa
import binascii

native_pay_url = "http://api.mch.ksher.net/KsherPay/native_pay"

def random_str():
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(32):
        str+=chars[random.randint(0, length)]
    return str

def dh_sign(message):
    """
    签名
    @param message is a dict
    """
    alist=[]
    for key, value in message.items():
        alist.append(key+"="+str(value))
    alist.sort()
    predata = "".join(alist).encode('utf8')

    # print("Predate", predata)

    with open('mch_privkey.pem') as privatefile:
        keydata = privatefile.read()
    dh_privkey = rsa.PrivateKey.load_pkcs1(keydata,'PEM')
    signature = rsa.sign(predata, dh_privkey, 'MD5')
    signature = binascii.hexlify(signature)
    return signature


#########################################################################
nonce_str = random_str()
#mch0000001   USD
#mch0000002   THB
#mch0000003   KRW
#mch0000004   HKD
#mch0000005   NZD
#mch0000006   CNY

appid = "mch20163"
time_stamp = time.strftime('%Y%m%d%H%M%S')
mch_order_no = str(int(time.time()))
total_fee = 10
fee_type = 'THB'
channel = 'wechat'
redirect_url = 'https://www.baidu.com'
notify_url = 'https://ht.dspread.com/weixin/dev6/NativepayApp/pay_notify'
paypage_title = 'TestNativeAPI'
product = ''
attach = ''
operator_id = ''
device_id = ''
limit_pay = ''
img_type = 'png'


dict = {
    'version':'1.0.0',
    'time_stamp':time_stamp,
    # 'data': {
    'appid':appid,
    'nonce_str':nonce_str,
    'mch_order_no':mch_order_no,
    'total_fee':total_fee,
    'fee_type':fee_type,
    'notify_url': notify_url,
    'channel': channel,
    'img_type': img_type
    # }
}

#签名

def generate_qrcode(dict):
    signature = dh_sign(dict)
    dict.update({'sign': signature})
    # print("Print dict", dict)

    # print(json.dumps(dict,sort_keys=True,indent=4))

    parmas = urllib.parse.urlencode(dict).encode("utf-8")
    # f=urllib.urlopen(native_pay_url,parmas)
    f=urllib.request.urlopen(native_pay_url,parmas)
    response = f.read()
    response_json = json.loads(response)
    # print (json.dumps(response_json, sort_keys=True, indent=4))
    if response_json['code'] == 0:
        if response_json['data']['result'] == 'SUCCESS':
            if img_type == 'svg':
                print (response_json['data']['imgdat'])
            elif img_type == 'png' or img_type == '': 
                return format(response_json['data']['imgdat'])
                # f = open("qrcode.html", "w+")
                # f.write("<img src={}>".format(response_json['data']['imgdat']))
                # f.flush()
                # f.close()
            else:
                pass
        else:
            pass
    return ''


if __name__ == '__main__':
    # print(generate_qrcode(dict))
    pass

