from django.contrib import admin
from django.urls import path

from core.views import transactionView, loginView
from core.views import userView

app_name = 'block3'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginView.login),
    path('register/', loginView.register),
    path('wallet/', userView.wallet),
    path('history/', transactionView.history),
    path('sendTransaction/', transactionView.sendTransaction),
    path('findHash/', transactionView.findHash),
    path('receivedTransaction/', transactionView.receivedTransaction),
]
