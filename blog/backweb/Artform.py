
from django import forms

class AddArtForm(forms.Form):
    title = forms.CharField(min_length=5, required=True,error_messages={
        'min_length':'文章标题不能小于5个字',
        'required':'文章标题不能为空',
    })
    describe = forms.CharField(min_length=10, required=True,error_messages={
        'min_length':'文章描述不能小于10个字',
        'required':'文章描述不能为空',
    })
    content = forms.CharField(required=True,error_messages={
        'required':'文章内容不能为空'
    })
    category = forms.CharField(required=False)
    visibility = forms.CharField(required=False)
    keywords = forms.CharField(required=False)
    titlepic = forms.ImageField(required=False)
    tags = forms.CharField(required=False)


class EditArtForm(forms.Form):
    title = forms.CharField(min_length=5, required=True,error_messages={
        'min_length':'文章标题不能小于5个字',
        'required':'文章标题不能为空',
    })
    describe = forms.CharField(min_length=10, required=True,error_messages={
        'min_length':'文章描述不能小于10个字',
        'required':'文章描述不能为空',
    })
    content = forms.CharField(required=True,error_messages={
        'required':'文章内容不能为空'
    })
    category = forms.CharField(required=False)
    visibility = forms.CharField(required=False)
    keywords = forms.CharField(required=False)
    titlepic = forms.ImageField(required=False)
    tags = forms.CharField(required=False)


class AddCateForm(forms.Form):
    name = forms.CharField(min_length=2,required=True)
    alias = forms.CharField(min_length=2,required=True)
    keywords = forms.CharField(min_length=2,required=True)
    describe = forms.CharField(min_length=2,required=True)


class UpdateCateForm(forms.Form):
    name = forms.CharField(min_length=2, required=True)
    alias = forms.CharField(min_length=2, required=True)
    keywords = forms.CharField(min_length=2, required=True)
    describe = forms.CharField(min_length=2, required=True)