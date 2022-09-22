from django import forms


class UploadVideoForm(forms.Form):
    title = forms.CharField(label='Title', max_length=32)
    video = forms.FileField(label='Video')
    preview = forms.ImageField(label='Preview')

    # def __str__(self):
    #     return f'title {self.title}'


class AddCommentForm(forms.Form):
    value = forms.CharField(max_length=300)
    video_id = forms.IntegerField()
    author_id = forms.IntegerField()
