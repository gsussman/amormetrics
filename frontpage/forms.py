from django import forms
from frontpage.models import Image

FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)

class ImageForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False,)
    profile = forms.CharField(widget=forms.Textarea, required=False)

        
class ProfileForm(forms.Form):
    file = forms.FileField()

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    
class ImageForm1(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']