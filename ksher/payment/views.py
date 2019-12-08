from django.shortcuts import render
from django.http import HttpResponse
from .native_pay import generate_qrcode, random_str
import time


# Create your views here.

def Home(request):
	return render (request, 'payment/home.html')

def Wechat(request):
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

	qr_wechat = generate_qrcode(dict)
	return render (request, 'payment/wechat.html', {'qr_wechat': qr_wechat})

def Alipay(request):
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
	channel = 'alipay'
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

	qr_alipay = generate_qrcode(dict)
	return render (request, 'payment/alipay.html', {'qr_alipay': qr_alipay})

def Promptpay(request):
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
	channel = 'bbl_promptpay'
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

	qr_promptpay = generate_qrcode(dict)
	return render (request, 'payment/promptpay.html', {'qr_promptpay': qr_promptpay})