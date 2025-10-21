from django import forms

from .models import CustomUser

class UserCreationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password','required':True})
    )
    class Meta:
        model = CustomUser
        fields = (
            "username","email","first_name","last_name","avatar","birth_date","password"
        )
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username','required':True}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email', 'required':True}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your First Name.'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Last Name.'}),
            'avatar':forms.FileInput(attrs={'class':'form-control'}),
            'birth_date':forms.DateInput(attrs={'class':'form-control','required':True}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password','required':True})
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("This username already exists.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email already exists.")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']

        if len(password) < 8:
            raise forms.ValidationError("Your password must be more than 8 character.")
        
        if password != confirm_password:
            raise forms.ValidationError("Your password mismatch with confirm_password.")
        
        return cleaned_data

    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            "username","email","first_name","last_name","avatar","birth_date"
        )
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username','required':True}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email', 'required':True}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your First Name.'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Last Name.'}),
            'avatar':forms.FileInput(attrs={'class':'form-control'}),
            'birth_date':forms.DateInput(attrs={'class':'form-control','required':True}),
        }
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if CustomUser.objects.filter(username=username).exclude(id=self.instance.pk).exists():
            raise forms.ValidationError("This username already taken.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exclude(id=self.instance.pk).exists():
            raise forms.ValidationError("This email already taken.")
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            "username","email","first_name","last_name","avatar","birth_date"
        )