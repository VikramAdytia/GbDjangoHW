from django import forms

class ClientForm(forms.Form): 
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    tel = forms.CharField(max_length=10)
    address = forms.CharField(widget=forms.Textarea)
    
    def clean_email(self):
        email: str = self.cleaned_data['email']
        if not (email.endswith('vk.team') or email.endswith('corp.mail.ru')):
            raise forms.ValidationError('Используйтекорпоративную почту')
        return email

# class ManyFieldsFormWidget(forms.Form):
#     name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введитеимяпользователя'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
#     age = forms.IntegerField(min_value=18, widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
#     birthdate = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control'}))
#     gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
#     message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    foto = forms.ImageField()
    quantity = forms.IntegerField(min_value=0)
