from django import forms

from accounts.models import myUser
from .models import Blog, Comment

class BlogForm(forms.Form):
    #내가 입력받고자 하는 값들

    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
    # nickname = forms.CharField()
    # mbti = forms.CharField()
    # class Meta:
    #     model = myUser
    #     fields = ['nickname']

    
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields=['title','body']

class BlogUpdate(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']       

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment  #Comment라는 모델을 기반으로 입력값을 받을거다
#         fields=['comment'] #이 부분만 입력받겠다는 의미

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  #Comment라는 모델을 기반으로 입력값을 받을거다
        fields=['comment'] #이 부분만 입력받겠다는 의미
    # comment = forms.CharField()
