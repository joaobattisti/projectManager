from django.forms import ModelForm
from .models import Activity

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['project_id', 'activity_name', 'activity_datestart', 'activity_datefinish', 'activity_concluded']
