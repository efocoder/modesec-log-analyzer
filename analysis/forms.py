from django.forms import ModelForm, Form, CharField

from analysis.models import Analysis


class NewLogForm(ModelForm):
    class Meta:
        model = Analysis
        fields = ['title', 'log_file']


class FilterForm(Form):
    title = CharField(max_length=255, required=False)
    section = CharField(max_length=255, required=False)
    log_id = CharField(max_length=255, required=False)
