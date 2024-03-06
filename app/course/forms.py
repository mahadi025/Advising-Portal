from django.forms import ModelForm
from core.models import Takes


class EditGrade(ModelForm):
    class Meta:
        model = Takes
        fields = ["grade"]
