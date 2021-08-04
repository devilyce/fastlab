from django import forms

from orderitem.models import OrderItem

# TEST_CHOICE = Product.objects.all().values_list('name', 'name')
# TEST_CHOICE_LIST = []
# for item in TEST_CHOICE:
#     TEST_CHOICE_LIST.append(item)
#
# TEST_LOC = TestLocation.objects.all().values_list('location_name', 'location_name')
# TEST_LOC_LIST = []
# for item in TEST_LOC:
#     TEST_LOC_LIST.append(item)

NUMBER_OF_PERSON = (
    ('1', 'One'),
    ('2', 'Two'),
    ('3', 'Three'),
    ('4', 'Four'),
)
YES_NO = (
    ('YES', 'Yes'),
    ('NO', 'No'),
)
GENDER = (
    ('', '-Select Gender-'),
    ('Male', 'Male'),
    ('Female', 'Female'),
)
CIVIL_STATUS = (
    ('', '-Select Civil Status-'),
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('Widowed', 'Widowed'),
    ('Annulled', 'Annulled'),
    ('Legally Separated', 'Legally Separated'),
)


class OrderItemForms(forms.ModelForm):
    waiver = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    sick1 = forms.BooleanField(required=True, widget=forms.RadioSelect(choices=YES_NO, ))
    sick2 = forms.BooleanField(required=True, widget=forms.RadioSelect(choices=YES_NO, ))
    sick3 = forms.BooleanField(required=True, widget=forms.RadioSelect(choices=YES_NO, ))

    class Meta:
        model = OrderItem
        fields = {
            'number_of_person', 'product', 'test_location', 'first_name',
            'first_name', 'last_name', 'middle_name', 'email', 'contact_number', 'nationality',
            'civil_status', 'date_of_birth', 'gender', 'address', 'senior_pwd_id', 'year', 'month', 'day', 'time',
            'senior_pwd_file'
        }

        widgets = {
            'product': forms.Select(attrs={'class': 'form-select', 'name': 'product'}),
            'test_location': forms.Select(attrs={'class': 'form-select', 'name': 'test_location'}),
            'year': forms.TextInput(
                attrs={'required': '', 'class': 'form-control', 'name': 'year', }),
            'month': forms.TextInput(attrs={'required': '', 'class': 'form-control', 'name': 'month', }),
            'day': forms.TextInput(attrs={'required': '', 'class': 'form-control', 'name': 'day', }),
            'time': forms.TextInput(attrs={'required': '', 'class': 'form-control', 'name': 'time', }),
            'number_of_person': forms.Select(choices=NUMBER_OF_PERSON,
                                             attrs={'class': 'form-select', 'name': 'number_of_person'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'last_name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'middle_name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'}),
            'contact_number': forms.TextInput(
                attrs={'class': 'form-control', 'type': 'number', 'name': 'contact_number'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'name': 'nationality'}),
            'civil_status': forms.Select(choices=CIVIL_STATUS,
                                         attrs={'class': 'form-select', 'name': 'civil_status'}),
            'date_of_birth': forms.DateInput(format=('%d-%m-%Y'),
                                             attrs={'class': 'form-control', 'name': 'date_of_birth',
                                                    'type': 'date'}),
            'gender': forms.Select(choices=GENDER, attrs={'class': 'form-select', 'name': 'gender'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'name': 'address', }),
            'senior_pwd_id': forms.TextInput(attrs={'class': 'form-control', 'name': 'senior_pwd_id'}),
            'senior_pwd_file': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'})
        }
