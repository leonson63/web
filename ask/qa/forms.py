# forms
from django import forms
from models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        q = Question(**self.cleaned_data)
#        q.author_id=0
        q.save()
        return q



class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()

    def clean_question(self):
        try:
            return int(self.clenned_data['question'])
        except ValueError:
            raise forms.ValidationError

    def save(self):
        a = Answer(**self.cleaned_data)
#        a.author_id=0
        a.save()
        return a

class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
