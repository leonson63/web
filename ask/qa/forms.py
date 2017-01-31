# forms
from django import forms
from models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, **kwargs):
        self.title=kwargs['title']
        self.text=kwargs['text']

    def save(self):
        q = Question(**self.cleaned_data)
        q.save()
        return q



class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.CharField()

    def clean_question(self):
        try:
            return int(self.clenned_data['question'])
        except ValueError:
            raise forms.ValidationError

    def save(self):
        a = Answer(**self.cleaned_data)
        a.save()
        return a