from django import forms

from expense_tracker.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'profile_image': forms.FileInput(
                attrs={
                    'class': 'form-file',
                },
            ),
        }


class EditProfileForm(CreateProfileForm):
    pass
