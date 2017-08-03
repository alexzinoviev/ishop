from django import forms
from profanity import profanity
from django.core.exceptions import ValidationError

# логика работы с формой

class CommentForm(forms.Form):
    #author = forms.CharField()
    body = forms.CharField(widget=forms.Textarea())

    def clean_body(self):
        if profanity.contains_profanity(self.cleaned_data['body']):
            raise ValidationError("Body shouldn't contain profanity")
        return self.cleaned_data['body']

    # def clean(self):
        # if self.cleaned_data['author'] == self.cleaned_data.get('body', ''):
        #     raise ValidationError("Name can't be the same with body text")
        # return self.cleaned_data


