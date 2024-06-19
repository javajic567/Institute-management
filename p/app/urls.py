from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import *
urlpatterns=[
    path('', h, name='Home'),
    path('user_regis',user_regis_view,name='user_regis'),

    path('registration/',regis_view,name='Registration'),
   path('regist/',regis_view),
    path('login/',LoginView.as_view(template_name='log.html'),name='LI'),
    path('logout/', LogoutView.as_view(template_name='logo.html'), name='LO'),

    path('enquiry/',enq_view,name='Enquiry'),
    path('pendingfee/',pf_view,name='Pendingfees'),
    path('display/',Display_enq,name='display'),
    path('pay/<int:pk>',pay_view,name='pay'),
    path('sta/',static_view,name='sta')
]