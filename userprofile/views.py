from multiprocessing import context
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from bootcamp.models import Exam,UserCourse
from .models import Certificate
def login_page(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.error(request,  'با موفقیت وارد شدید ')
            return redirect('/question-page/')
            
        else:
            context['LoginError'] = 'رمز عبور یا ایمیل شما اشتباه است'

    return render(request, 'userprofile/login.html',context=context)
# def question_page(request):
#     return render(request,'userprofile/academy-question.html',)    
def go_to_final_page(request):
    context = {}
    if request.method == 'POST':
        print(request.POST)
        try:
            question_1= request.POST['radio']
        except MultiValueDictKeyError:
            question_1= 0
        try:
            question_2= request.POST['radio2']
        except MultiValueDictKeyError:
            question_2= 0
        try:
            question_3= request.POST['radio3']
        except MultiValueDictKeyError:
            question_3= 0
        try:
            question_4= request.POST['radio4']
        except MultiValueDictKeyError:
            question_4= 0
        try:
            question_5= request.POST['radio5']
        except MultiValueDictKeyError:
            question_5= 0
        try:
            question_6= request.POST['radio6']
        except MultiValueDictKeyError:
            question_6= 0
        try:
            question_7= request.POST['radio7']
        except MultiValueDictKeyError:
            question_7= 0
        try:
            question_8= request.POST['radio8']
        except MultiValueDictKeyError:
            question_8= 0
        try:
            question_9= request.POST['textarea']
        except MultiValueDictKeyError:
            question_9= ' '                               
        exam = Exam.objects.create(exam_user=request.user,question_1=question_1, question_2=question_2, question_3=question_3, question_4=question_4, question_5=question_5, question_6=question_6, question_7=question_7, question_8=question_8, question_9=question_9)   
        exam.save()                 
        return redirect('/result/')
    return render(request,'userprofile/academy-question.html',context)   
def result(request):
    context = {}
    try:
        courses = UserCourse.objects.get(user=request.user)
        context['courses']=courses.course.all()
    except UserCourse.DoesNotExist:
        messages.error(request,'ویدیو های دوره برای شما در دسترس نیست') 
        context['courses_error'] = 'ویدیو های دوره برای شما در دسترس نیست' 
    try:      
        cert = Certificate.objects.filter(user = request.user)
        context['certs'] = cert
    except:
            messages.error(request,'مدرک شما صادر نگردیده است') 
            context['cert_error'] = 'مدرک شما صادر نگردیده است'
    print(Certificate.objects.filter(user = request.user))
    return render(request,'userprofile/result.html',context=context)

def error_404(request, exception):
        data = {}
        return render(request,'userprofile/error404.html', data)
def logout_view(request):
        logout(request)
        return redirect('/')       
            
