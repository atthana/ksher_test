from django.urls import path
from .views import Home, Wechat, Alipay, Promptpay

urlpatterns = [
    path('', Home, name = 'home-page'),
    path('wechat/', Wechat, name = 'wechat-page'),
    path('alipay/', Alipay, name = 'alipay-page'),
    path('promptpay/', Promptpay, name = 'promptpay-page'),
]
