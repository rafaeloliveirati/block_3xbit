from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from core.views import transactionView
from core.views import userView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', userView.login),
    url('register/', userView.register),
    url('wallet/', userView.wallet),
    url('history/', transactionView.history),
    url('sendTransaction/', transactionView.sendTransaction),
    url('findHash/', transactionView.findHash),
    url('receivedTransaction/', transactionView.receivedTransaction),
]
