from django import forms
class CommentsForm(forms.Form):
    name = forms.CharField(label='昵称', max_length=16, error_messages={'required': '请填写昵称', 'max_lenth': '昵称太长'})
    email = forms.EmailField(label='邮箱', error_messages={'required': '请填写你的邮箱', 'invalid': '邮箱格式不正确'})
    content = forms.CharField(label='评论内容', error_messages={'required': '请填写内容', 'max_length': '内容太长'})