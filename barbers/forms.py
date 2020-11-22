from django import forms
from .models import Profile, Gallery

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First name', widget = forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=30, label='Last name', widget = forms.TextInput(attrs={'placeholder':'Last Name'}))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class AddImageForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['image']
        labels = {'image': ''}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
         'bio',
         'profile_picture',
         'phone_no',
         'city',
         'state',
         'address',
         'whatsapp_no',
         'facebook_link',
         'intagram_link',
         'twitter_link',
         'home_service',
        ]

        labels = {
            'bio': 'Bio',
            'profile_picture': 'Profile picture',
             'phone_no': 'mobile number',
             'city' : 'city',
             'state':'State',
             'address': 'Shop address',
             'whatsapp_no': 'whatsApp number',
             'facebook_link':'Facebook Address',
             'intagram_link':'Instagram Address',
             'twitter_link':'Twitter Address',
             'home_service': 'Are you available for home service?'
  }
