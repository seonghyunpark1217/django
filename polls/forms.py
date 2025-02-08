from django import forms
from django.forms import inlineformset_factory
from .models import Question, Choice

class QuestionForm(forms.ModelForm):
  class Meta:
    model = Question
    fields = ['question_text']

ChoiceFormSet = inlineformset_factory(Question, Choice, fields = ['choice_text'], extra = 0, min_num = 3, can_delete = False)    