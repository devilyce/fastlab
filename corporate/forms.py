from django import forms

from corporate.models import Corporate, lab_Corporate


class CorporateFrom(forms.ModelForm):
    class Meta:
        model = Corporate

        fields = '__all__'

        widgets = {
            'product': forms.Select(attrs={'class': 'form-select'}),
            'test_location': forms.Select(attrs={'class': 'form-select'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.Select(attrs={'class': 'form-control', 'type': 'time'}),

            'senior_pwd_id': forms.TextInput(attrs={'class': 'form-control'}),
            'senior_pwd_file': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}),

            'philhealth': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type':'email'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'civil_status': forms.Select(attrs={'class': 'form-select'}),
            'date_of_birth': forms.DateInput(format=('%m-%d-%Y'), attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control', 'name': 'occupation'}),
            'lot': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'brgy': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control'}),
            'cp_no': forms.TextInput(attrs={'class': 'form-control'}),
            'work_lot': forms.TextInput(attrs={'class': 'form-control'}),
            'work_street': forms.TextInput(attrs={'class': 'form-control'}),
            'work_brgy': forms.TextInput(attrs={'class': 'form-control'}),
            'work_city': forms.TextInput(attrs={'class': 'form-control'}),
            'work_province': forms.TextInput(attrs={'class': 'form-control'}),
            'workplace': forms.TextInput(attrs={'class': 'form-control'}),
            'work_contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'work_email': forms.TextInput(attrs={'class': 'form-control'}),
            'covid_consultation': forms.Select(attrs={'class': 'form-select'}),
            'covid_consultation_date': forms.DateInput(format=('%m-%d-%Y'),
                                                       attrs={'class': 'form-control', 'type': 'date'}),
            'consult_facility': forms.TextInput(attrs={'class': 'form-control'}),
            'health_facility': forms.Select(attrs={'class': 'form-select'}),
            'health_facility_date': forms.DateInput(format=('%m-%d-%Y'),
                                                    attrs={'class': 'form-control', 'type': 'date'}),
            'facility_name': forms.TextInput(attrs={'class': 'form-control'}),
            'region_facility': forms.TextInput(attrs={'class': 'form-control'}),
            'admitted_hospital': forms.TextInput(attrs={'class': 'form-control'}),
            'admitted_hospital_date': forms.DateTimeInput(format=('%m-%d-%Y'),
                                                          attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'admitted_facility': forms.TextInput(attrs={'class': 'form-control'}),
            'admitted_facility_date': forms.DateInput(format=('%m-%d-%Y'),
                                                      attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'home_quarantine': forms.TextInput(attrs={'class': 'form-control'}),
            'home_quarantine_date': forms.DateInput(format=('%m-%d-%Y'),
                                                    attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'other_admitted': forms.TextInput(attrs={'class': 'form-control'}),
            'discard_home': forms.Select(attrs={'class': 'form-select'}),
            'discarge_date': forms.DateInput(format=('%m-%d-%Y'), attrs={'class': 'form-control', 'type': 'date'}),
            'health_status_consult': forms.Select(attrs={'class': 'form-select'}),
            'case_classification': forms.Select(attrs={'class': 'form-select'}),
            'health_care_worker': forms.Select(attrs={'class': 'form-select'}),
            'health_care_worker_name': forms.TextInput(attrs={'class': 'form-control'}),
            'return_ofw': forms.Select(attrs={'class': 'form-select'}),
            'return_ofw_country': forms.TextInput(attrs={'class': 'form-control'}),
            'foreign_traveler': forms.Select(attrs={'class': 'form-select'}),
            'foreign_traveler_country': forms.TextInput(attrs={'class': 'form-control'}),
            'local_stranded': forms.Select(attrs={'class': 'form-select'}),
            'local_stranded_city': forms.TextInput(attrs={'class': 'form-control'}),
            'live_closed': forms.Select(attrs={'class': 'form-select'}),
            'live_closed_name': forms.TextInput(attrs={'class': 'form-control'}),
            'current_lot': forms.TextInput(attrs={'class': 'form-control'}),
            'current_street': forms.TextInput(attrs={'class': 'form-control'}),
            'current_brgy': forms.TextInput(attrs={'class': 'form-control'}),
            'current_city': forms.TextInput(attrs={'class': 'form-control'}),
            'current_province': forms.TextInput(attrs={'class': 'form-control'}),
            'current_phone_no': forms.TextInput(attrs={'class': 'form-control'}),
            'current_cp_no': forms.TextInput(attrs={'class': 'form-control'}),
            'current_email': forms.EmailInput(attrs={'class': 'form-control', 'type':'email'}),
            'ofw_lot': forms.TextInput(attrs={'class': 'form-control'}),
            'ofw_street': forms.TextInput(attrs={'class': 'form-control'}),
            'ofw_city': forms.TextInput(attrs={'class': 'form-control'}),
            'ofw_province': forms.TextInput(attrs={'class': 'form-control'}),
            'ofw_country': forms.TextInput(attrs={'class': 'form-control'}),
            'ofw_workplace': forms.TextInput(attrs={'class': 'form-control'}),
            'ofw_employer': forms.TextInput(attrs={'class': 'form-control'}),
            'ofw_contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'date_onset': forms.DateInput(format=('%m-%d-%Y'), attrs={'class': 'form-control', 'type': 'date'}),
            'asympto': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fever': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fever_temp': forms.TextInput(attrs={'class': 'form-control'}),
            'cough': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'general_weak': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fatigue': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'headache': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'myalgia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sore_throat': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'coryza': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'dyspnea': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'anorexia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nausea': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'vomiting': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'diarrhea': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'altered_mental': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'anosmia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'aguesia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'other_symptoms': forms.TextInput(attrs={'class': 'form-control'}),
            'como_none': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'gastro': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'hyper': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'genito': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'diabetes': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'neuro': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'heart_d': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cancer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'lung_d': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'como_others': forms.TextInput(attrs={'class': 'form-control'}),
            'pregnant': forms.Select(attrs={'class': 'form-select'}),
            'pregnant_lmp': forms.TextInput(attrs={'class': 'form-control'}),
            'risk_pregnant': forms.Select(attrs={'class': 'form-select'}),
            'diag_sari': forms.Select(attrs={'class': 'form-select'}),
            'chest_radio': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'chest_radio_finding': forms.TextInput(attrs={'class': 'form-control'}),
            'chest_ct': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'chest_ct_finding': forms.TextInput(attrs={'class': 'form-control'}),
            'lung_ultra': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'lung_ultra_finding': forms.TextInput(attrs={'class': 'form-control'}),
            'chest_imaging_none': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'rt_pcr_ops': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'rt_pcr_ops_date': forms.DateInput(format=('%m-%d-%Y'), attrs={'class': 'form-control', 'type': 'date'}),
            'rt_pcr_ops_lab': forms.TextInput(attrs={'class': 'form-control'}),
            'rt_pcr_ops_result': forms.Select(attrs={'class': 'form-select'}),
            'rt_pcr_ops_date_release': forms.DateInput(format=('%m-%d-%Y'),
                                                       attrs={'class': 'form-control', 'type': 'date'}),

            'rt_pcr_nps': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'rt_pcr_nps_date': forms.DateInput(format=('%m-%d-%Y'), attrs={'class': 'form-control', 'type': 'date'}),
            'rt_pcr_nps_lab': forms.TextInput(attrs={'class': 'form-control'}),
            'rt_pcr_nps_result': forms.Select(attrs={'class': 'form-select'}),
            'rt_pcr_nps_date_release': forms.DateInput(format=('%m-%d-%Y'),
                                                       attrs={'class': 'form-control', 'type': 'date'}),

            'rt_pcr_ops_nps': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'rt_pcr_ops_nps_date': forms.DateInput(format=('%m-%d-%Y'),
                                                   attrs={'class': 'form-control', 'type': 'date'}),
            'rt_pcr_ops_nps_lab': forms.TextInput(attrs={'class': 'form-control'}),
            'rt_pcr_ops_nps_result': forms.Select(attrs={'class': 'form-select'}),
            'rt_pcr_ops_nps_date_release': forms.DateInput(format=('%m-%d-%Y'),
                                                           attrs={'class': 'form-control', 'type': 'date'}),

            'rt_pcr': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'rt_pcr_specimen': forms.TextInput(attrs={'class': 'form-control'}),
            'rt_pcr_specimen_date': forms.DateInput(format=('%m-%d-%Y'),
                                                    attrs={'class': 'form-control', 'type': 'date'}),
            'rt_pcr_specimen_lab': forms.TextInput(attrs={'class': 'form-control'}),
            'rt_pcr_specimen_result': forms.Select(attrs={'class': 'form-select'}),
            'rt_pcr_specimen_date_release': forms.DateInput(format=('%m-%d-%Y'),
                                                            attrs={'class': 'form-control', 'type': 'date'}),

            'antigen': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'antigen_date': forms.DateInput(format=('%m-%d-%Y'), attrs={'class': 'form-control', 'type': 'date'}),
            'antigen_lab': forms.TextInput(attrs={'class': 'form-control'}),
            'antigen_result': forms.Select(attrs={'class': 'form-select'}),
            'antigen_date_release': forms.DateInput(format=('%m-%d-%Y'),
                                                    attrs={'class': 'form-control', 'type': 'date'}),

            'antibody': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'antibody_date': forms.DateInput(format=('%m-%d-%Y'), attrs={'class': 'form-control', 'type': 'date'}),
            'antibody_lab': forms.TextInput(attrs={'class': 'form-control'}),
            'antibody_result': forms.Select(attrs={'class': 'form-select'}),
            'antibody_date_release': forms.DateInput(format=('%m-%d-%Y'),
                                                     attrs={'class': 'form-control', 'type': 'date'}),

            'test_others': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'test_others_date': forms.DateInput(format=('%m-%d-%Y'), attrs={'class': 'form-control', 'type': 'date'}),
            'test_others_lab': forms.TextInput(attrs={'class': 'form-control'}),
            'test_others_result': forms.TextInput(attrs={'class': 'form-control'}),
            'test_others_date_release': forms.DateInput(format=('%m-%d-%Y'),
                                                        attrs={'class': 'form-control', 'type': 'date'}),

            'test_positive': forms.Select(attrs={'class': 'form-select'}),
            'test_positive_date': forms.DateInput(format=('%m-%d-%Y'), attrs={'class': 'form-control', 'type': 'date'}),
            'test_positive_lab': forms.TextInput(attrs={'class': 'form-control'}),
            'test_positive_number': forms.TextInput(attrs={'class': 'form-control'}),

            'current_admitted': forms.Select(attrs={'class': 'form-select'}),
            'recovered_date': forms.DateInput(format=('%m-%d-%Y'), attrs={'class': 'form-control', 'type': 'date'}),
            'death_date': forms.DateInput(format=('%m-%d-%Y'), attrs={'class': 'form-control', 'type': 'date'}),
            'immediate_cause': forms.TextInput(attrs={'class': 'form-control'}),
            'antecendent_cause': forms.TextInput(attrs={'class': 'form-control'}),
            'underlying_cause': forms.TextInput(attrs={'class': 'form-control'}),

            'history_exposure': forms.Select(attrs={'class': 'form-select'}),
            'history_date': forms.DateInput(format=('%m-%d-%Y'), attrs={'class': 'form-control', 'type': 'date'}),
            'history_place': forms.Select(attrs={'class': 'form-select'}),

            'health_facility_visit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'health_facility_visit_details': forms.TextInput(attrs={'class': 'form-control'}),
            'health_facility_visit_date': forms.DateInput(format=('%m-%d-%Y'),
                                                          attrs={'class': 'form-control', 'type': 'date'}),

            'closed_setting_visit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'closed_setting_visit_details': forms.TextInput(attrs={'class': 'form-control'}),
            'closed_setting_visit_date': forms.DateInput(format=('%m-%d-%Y'),
                                                         attrs={'class': 'form-control', 'type': 'date'}),

            'market_visit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'market_visit_details': forms.TextInput(attrs={'class': 'form-control'}),
            'market_visit_date': forms.DateInput(format=('%m-%d-%Y'), attrs={'class': 'form-control', 'type': 'date'}),

            'home_visit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'home_visit_details': forms.TextInput(attrs={'class': 'form-control'}),
            'home_visit_date': forms.DateInput(format=('%m-%d-%Y'), attrs={'class': 'form-control', 'type': 'date'}),

            'int_travel_visit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'int_travel_visit_details': forms.TextInput(attrs={'class': 'form-control'}),
            'int_travel_visit_date': forms.DateInput(format=('%m-%d-%Y'),
                                                     attrs={'class': 'form-control', 'type': 'date'}),

            'school_visit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'school_visit_details': forms.TextInput(attrs={'class': 'form-control'}),
            'school_visit_date': forms.DateInput(format=('%m-%d-%Y'), attrs={'class': 'form-control', 'type': 'date'}),

            'transpo_visit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'transpo_visit_details': forms.TextInput(attrs={'class': 'form-control'}),
            'transpo_visit_date': forms.DateInput(format=('%m-%d-%Y'), attrs={'class': 'form-control', 'type': 'date'}),

            'workplace_visit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'workplace_visit_details': forms.TextInput(attrs={'class': 'form-control'}),
            'workplace_visit_date': forms.DateInput(format=('%m-%d-%Y'),
                                                    attrs={'class': 'form-control', 'type': 'date'}),

            'local_travel_visit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'local_travel_visit_details': forms.TextInput(attrs={'class': 'form-control'}),
            'local_travel_visit_date': forms.DateInput(format=('%m-%d-%Y'),
                                                       attrs={'class': 'form-control', 'type': 'date'}),

            'gathering_visit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'gathering_visit_details': forms.TextInput(attrs={'class': 'form-control'}),
            'gathering_visit_date': forms.DateInput(format=('%m-%d-%Y'),
                                                    attrs={'class': 'form-control', 'type': 'date'}),

            'other_visit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'other_visit_details': forms.TextInput(attrs={'class': 'form-control'}),
            'other_visit_date': forms.DateInput(format=('%m-%d-%Y'), attrs={'class': 'form-control', 'type': 'date'}),

            'travel_history': forms.Select(attrs={'class': 'form-select'}),
            'travel_history_country': forms.TextInput(attrs={'class': 'form-control'}),
            'travel_history_airline': forms.TextInput(attrs={'class': 'form-control'}),
            'travel_history_airline_number': forms.TextInput(attrs={'class': 'form-control'}),
            'travel_history_airline_depart': forms.DateInput(format=('%m-%d-%Y'),
                                                             attrs={'class': 'form-control', 'type': 'date'}),
            'travel_history_airline_arival': forms.DateInput(format=('%m-%d-%Y'),
                                                             attrs={'class': 'form-control', 'type': 'date'}),

            'travel_history_local': forms.Select(attrs={'class': 'form-select'}),
            'travel_history_local_place': forms.TextInput(attrs={'class': 'form-control'}),
            'travel_history_local_airline': forms.TextInput(attrs={'class': 'form-control'}),
            'travel_history_local_airline_number': forms.TextInput(attrs={'class': 'form-control'}),
            'travel_history_local_airline_depart': forms.DateInput(format=('%m-%d-%Y'),
                                                                   attrs={'class': 'form-control', 'type': 'date'}),
            'travel_history_local_airline_arival': forms.DateInput(format=('%m-%d-%Y'),
                                                                   attrs={'class': 'form-control', 'type': 'date'}),

            'household_contacts_name1': forms.TextInput(attrs={'class': 'form-control'}),
            'household_contacts_number1': forms.TextInput(attrs={'class': 'form-control'}),
            'household_contacts_setting1': forms.TextInput(attrs={'class': 'form-control'}),

            'household_contacts_name2': forms.TextInput(attrs={'class': 'form-control'}),
            'household_contacts_number2': forms.TextInput(attrs={'class': 'form-control'}),
            'household_contacts_setting2': forms.TextInput(attrs={'class': 'form-control'}),

            'household_contacts_name3': forms.TextInput(attrs={'class': 'form-control'}),
            'household_contacts_number3': forms.TextInput(attrs={'class': 'form-control'}),
            'household_contacts_setting3': forms.TextInput(attrs={'class': 'form-control'}),

            'household_contacts_name4': forms.TextInput(attrs={'class': 'form-control'}),
            'household_contacts_number4': forms.TextInput(attrs={'class': 'form-control'}),
            'household_contacts_setting4': forms.TextInput(attrs={'class': 'form-control'}),

            'household_contacts_name5': forms.TextInput(attrs={'class': 'form-control'}),
            'household_contacts_number5': forms.TextInput(attrs={'class': 'form-control'}),
            'household_contacts_setting5': forms.TextInput(attrs={'class': 'form-control'}),

            'household_contacts_name6': forms.TextInput(attrs={'class': 'form-control'}),
            'household_contacts_number6': forms.TextInput(attrs={'class': 'form-control'}),
            'household_contacts_setting6': forms.TextInput(attrs={'class': 'form-control'}),

            'household_contacts_name7': forms.TextInput(attrs={'class': 'form-control'}),
            'household_contacts_number7': forms.TextInput(attrs={'class': 'form-control'}),
            'household_contacts_setting7': forms.TextInput(attrs={'class': 'form-control'}),

            'household_contacts_name8': forms.TextInput(attrs={'class': 'form-control'}),
            'household_contacts_number8': forms.TextInput(attrs={'class': 'form-control'}),
            'household_contacts_setting8': forms.TextInput(attrs={'class': 'form-control'}),

            'household_contacts_name9': forms.TextInput(attrs={'class': 'form-control'}),
            'household_contacts_number9': forms.TextInput(attrs={'class': 'form-control'}),
            'household_contacts_setting9': forms.TextInput(attrs={'class': 'form-control'}),

            'waiver': forms.CheckboxInput(attrs={'class': 'form-check-input'})

        }


class booking_CorporateForms(forms.ModelForm):
    class Meta:
        model = Corporate
        fields = {
            'product', 'test_location', 'booking_date', 'time', 'senior_pwd_id', 'payment_status', 'payment_method',
            'payment_reference',
        }
        widgets = {
            'product': forms.Select(attrs={'class': 'form-select', 'name': 'product'}),
            'test_location': forms.Select(attrs={'class': 'form-select', 'name': 'test_location'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.Select(attrs={'class': 'form-control', 'type': 'time'}),
            'senior_pwd_id': forms.TextInput(attrs={'class': 'form-control', 'name': 'senior_pwd_id'}),
            'payment_status': forms.Select(attrs={'class': 'form-select', 'name': 'payment_status'}),
            'payment_method': forms.Select(attrs={'class': 'form-select', 'name': 'payment_method'}),
            'payment_reference': forms.TextInput(attrs={'class': 'form-control', 'name': 'payment_reference'}),
        }


class clinic_CorporateForms(forms.ModelForm):
    class Meta:
        model = Corporate
        fields = {
            'pending_test'
        }
        widgets = {
            'pending_test': forms.Select(attrs={'class': 'form-select', 'name': 'pending_test'}),
        }


class lab_CorporateForms(forms.ModelForm):
    class Meta:
        model = lab_Corporate
        fields = {
            'result_file',
        }
        widgets = {
            'result_file': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'name': 'result_file'})
        }
