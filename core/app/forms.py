from django import forms

class InputForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control' # bootstrapを使用するため
            field.widget.attrs['placeholder'] = field.label

    username       = forms.CharField(label='ユーザー名')
    password       = forms.CharField(label='パスワード', widget=forms.PasswordInput(), min_length=8)
    hashtag        = forms.CharField(label='ハッシュタグ(#なし)')
    max_like_count = forms.IntegerField(label='いいねする数')
