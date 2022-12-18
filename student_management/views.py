from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, ExamChoiceFrm, AnsChoice
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from admin_dash.models import Questions, Course, Paper, Answer
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login as dj_login,
    logout
)
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            course = Course.objects.filter(course=form.cleaned_data.get('course'))[0]
            request.session['course']=course.id
            email = form.cleaned_data.get('email')
            regd_id = form.cleaned_data.get('regd_id')
            password = form.cleaned_data.get('password')
            
            print(email)

            user = form.save(commit=False)

            user.set_password(password)
            user.save()
            newuser = authenticate(regd_id = regd_id, email = email, password = password)


            print(newuser)
            
            dj_login(request, newuser, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(student_home)

    form = RegistrationForm()
    context = {
        'form' : form
    }
    return render(request, 'std_register.html', context)

def login(request):
    if request.method == 'POST':
        
        form=LoginForm(request.POST or None)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            regd_id=form.cleaned_data.get('regd_id')
            password = form.cleaned_data.get('password')
            user = authenticate(request, regd_id = regd_id, email = email, password = password)

            if user is not None:
                dj_login(request,user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect(student_home)
            else:
                form = LoginForm()
                context = {
                'form' : form
                }
                messages.info(request, 'INVALID CREDENTIALS!')
                return render(request, 'login.html', context)

    else:
        form = LoginForm()
        context = {
        'form' : form
        }
    return render(request, 'login.html', context)

@login_required
def student_home(request):
    if request.method=='POST':
        form=ExamChoiceFrm(request.POST or None)
        if form.is_valid():     
            course=request.user.course
            request.session['course']=request.user.course.id
            paper=Paper.objects.filter(paper=form.cleaned_data.get('paper'))[0]
            request.session['paper']=paper.id
            ex=Answer.objects.filter(student=request.user,question__course=course,question__paper=paper)
            if ex:
                exam=ex[0].question
                if course==exam.course and paper==exam.paper:
                    form=ExamChoiceFrm()
                    context={
                        'form':form,
                        'msg':'Exam Already Completed!',
                    }
                    return render(request, 'student_home.html', context)
            else:
                qs=Questions.objects.filter(course=course,paper=paper)
                if qs:
                    qs=qs[0].qs_no
                    return redirect('exam_home',qs)
                else:
                    form=ExamChoiceFrm()
                    context={
                        'form':form,
                        'msg':'No Question Paper Found!',
                    }
                    return render(request,'student_home.html',context)

    form=ExamChoiceFrm()
    msg=""
    context={
        'form':form,
        'msg':msg,
    }
    return render(request,'student_home.html',context)


def logout_view(request):
	logout(request)
	return redirect('/')

def exam_home(request, qno):
    paper=request.session['paper']
    course=request.session['course']
    qts=Questions.objects.filter(course=course,paper=paper)
    try:
        qs=qts.filter(qs_no=qno)[0]
    except:
        qs=qts.filter(qs_no=1)[0]
    getqs=Answer.objects.filter(question=qs,student=request.user)
    if getqs:
        msg="Already answered, Your answer will not save"
        request.session['msg']=msg
    else:   
        request.session['msg']=""
        if request.method=='POST':
            form=AnsChoice(request.POST or None)
            if form.is_valid():
                ans=form.cleaned_data.get('ans')
                ansqs=Answer(
                    student=request.user,
                    question=qs,
                    answer=ans
                )
                ansqs.save()
                nqno=int(qno) + 1
                request.session['msg']="Answer Saved Sucessfully!"
                return redirect('exam_home' ,nqno)
    ansfrm=AnsChoice()
    context = {
        'ansfrm':ansfrm,
        'questions':qts,
        'qs':qs,
    }
    return render(request, 'question.html', context)

