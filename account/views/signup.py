from django.shortcuts import render
from django.forms import Form,CharField,EmailField,ValidationError,TextInput
from ..models import User,UserInfo
from django.http import JsonResponse
from django.contrib.auth import login

def signup(request):
    if request.method=='post':
        form=RegisterForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                return JsonResponse({'code':-200})
            if User.objects.filter(email=email).exists():
                return JsonResponse({'code':-201})
            user=User.objects.create_user(username,email,form.cleaned_data['password1'])
            user.save()
            info = UserInfo(user=user)
            info.save()
            login(request,user)
            return JsonResponse({'code':0})
        return JsonResponse({'code':-100})
    else:
        return render(request,'account/signup.html',{'form':RegisterForm})

class RegisterForm(Form):
    username=CharField(max_length=100,required=True)
    password1=CharField(max_length=100,required=True)
    password2=CharField(max_length=100,required=True)
    email = EmailField(max_length=100,required=True)

    def clean_email(self):
        email=self.cleaned_data['email'].lower()
        if email:
            try:
                User.objects.get(email=email)
                raise ValidationError('邮箱已注册')
            except User.DoesNotExist:
                return email
        else:
            return ValidationError("邮箱不能为空")

    def clean_password(self):
        if self.cleaned_data['password1']!=self.cleaned_data['password2']:
            raise ValidationError('密码不一致')




