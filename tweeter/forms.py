from django import forms

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(label='Nickname', max_length=100)
    content_input = forms.CharField(label='Content', widget=forms.Textarea)
    # You can add validation or custom methods here if needed

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Etiketleri (label) sadeleştir
        self.fields["username"].label = "Username"
        self.fields["password1"].label = "Password"
        self.fields["password2"].label = "Password (again)"

        # Karmaşık yardım metinlerini kaldır
        for name in ["username", "password1", "password2"]:
            self.fields[name].help_text = ""

        # Bootstrap class ekle
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})