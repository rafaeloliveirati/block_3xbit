from django.urls import path

from website import transactionView, loginView, walletView
from website.views import LoginView

app_name = 'website'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('sendLogin/', loginView.login),
    path('register/', loginView.register),
    path('wallet/', walletView.createWallet),
    path('history/', transactionView.history),
    path('sendTransaction/', transactionView.sendTransaction),
    path('findHash/', transactionView.findHash),
    path('receivedTransaction/', transactionView.receivedTransaction),
]
