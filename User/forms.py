from django import forms
from .models import Users


# 定义表单匹配
class UserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=50)
    password2 = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=11)


# 登录表单
class loginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=50)


# 修改表单
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['avatar']


# 代码检查和入队列
class Check_code(object):
    def __init__(self, username, taken, code, time):  # 用户名 taken值，代码，提交时间
        self.username = username
        self.taken = taken  # 用户是否登录的唯一识别码
        self.code = code
        self.time = time

    # 检查代码是否是恶意的代码
    def check_code(self):
        return True
