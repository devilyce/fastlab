from django import forms

from customers.models import Customers

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


class CustomerForms(forms.ModelForm):
    waiver = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    sick1 = forms.BooleanField(required=True, widget=forms.RadioSelect(choices=YES_NO, ))
    sick2 = forms.BooleanField(required=True, widget=forms.RadioSelect(choices=YES_NO, ))
    sick3 = forms.BooleanField(required=True, widget=forms.RadioSelect(choices=YES_NO, ))
    senior_pwd_id_file = forms.FileField(required=False,
                                         widget=forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}))

    class Meta:
        model = Customers
        fields = {
            'number_of_person', 'product', 'test_location', 'first_name',
            'first_name', 'last_name', 'middle_name', 'email', 'contact_number', 'nationality',
            'civil_status', 'date_of_birth', 'gender', 'address', 'senior_pwd_id', 'booking_date', 'time',
        }

        widgets = {
            'product': forms.Select(attrs={'class': 'form-select', 'name': 'product'}),
            'test_location': forms.Select(attrs={'class': 'form-select', 'name': 'test_location'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'name': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'name': 'time'}),
            'number_of_person': forms.Select(choices=NUMBER_OF_PERSON,
                                             attrs={'class': 'form-select', 'name': 'number_of_person'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'last_name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'middle_name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'}),
            'contact_number': forms.NumberInput(
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
        }


class admin_edit_CustomerForms(forms.ModelForm):
    class Meta:
        model = Customers
        fields = {
            'product', 'number_of_person', 'test_location',
            'booking_date', 'time', 'senior_pwd_id', 'payment_status', 'refund_discount',
            'payment_method', 'payment_reference'
        }
        widgets = {
            'product': forms.Select(attrs={'class': 'form-select', 'name': 'product'}),
            'test_location': forms.Select(attrs={'class': 'form-select', 'name': 'test_location'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'senior_pwd_id': forms.TextInput(attrs={'class': 'form-control', 'name': 'senior_pwd_id'}),
            'number_of_person': forms.Select(choices=NUMBER_OF_PERSON,
                                             attrs={'class': 'form-select', 'name': 'number_of_person'}),
            'refund_discount': forms.NumberInput(
                attrs={'class': 'form-control', 'type': 'number', 'name': 'refund_discount'}),
            'payment_status': forms.Select(attrs={'class': 'form-select', 'name': 'payment_status'}),
            'payment_method': forms.Select(attrs={'class': 'form-select', 'name': 'payment_method'}),
            'payment_reference': forms.TextInput(attrs={'class': 'form-control', 'name': 'payment_reference'}),
        }
