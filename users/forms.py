from django.contrib.auth.forms import AuthenticationForm,UserCreationForm, UserChangeForm
from django import forms
from users.models import User, Order
from django.core.exceptions import ValidationError
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs = {'class':'form-control py-4', 'placeholder': 'Ваше имя'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class':'form-control py-4', 'placeholder': 'Ваш пароль'}))
    class Meta:
        models=User
        fields=('username','password')
        
        
        
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class UserProfileForm(UserChangeForm):
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
        
        
class OrderForm(forms.Form):

        
        
  
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Электронный адрес"})) 
    descriptionord = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Комментарии к заказу"}))
    adress = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Адрес почты"})) 
    contact = forms.CharField(max_length=13,widget=forms.TextInput(attrs={"placeholder": "Телефон"}))
   
    def clean_contact(self):
        
        email_data = self.cleaned_data['email']
        descriptionord_data = self.cleaned_data['descriptionord']
        adress_data = self.cleaned_data['adress']
        contact_data = self.cleaned_data['contact']
     
      
        if '+' not in contact_data:
            raise ValidationError('Добавьте "+" к началу номера телефона')
        if contact_data[1]!='3':
            raise ValidationError('Укажите номер в формате "+375(..)"')
        if contact_data[2]!='7':
            raise ValidationError('Укажите номер в формате "+375(..)"')
        if contact_data[3]!='5':
            raise ValidationError('Укажите номер в формате "+375(..)"')
        if len(descriptionord_data)== 1 and '-' not in descriptionord_data:
            raise ValidationError('Пожалуйста, заполните комментарии к заказу или поставьте прочерк')
        if len(contact_data)< 13:
            raise ValidationError('Необходимое колличество символов в номере: 13')
            
            
        return contact_data