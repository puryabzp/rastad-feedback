from unicodedata import name
from django.urls import path
from .views import login_page,go_to_final_page,result,logout_view
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', login_page,name='login'),
    path('question-page/', login_required(go_to_final_page),name='go_to_final_page'),
    # path('feedback/', question_page,name='feedback'),
    path('result/', login_required(result),name='result'),
    path('logout/', login_required(logout_view),name='logout'),

]