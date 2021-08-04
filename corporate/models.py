import uuid

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from cal.models import timeChoice
from locations.models import TestLocation
from products.models import Product


class Corporate(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    reference_number = models.CharField(max_length=50, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    test_location = models.ForeignKey(TestLocation, on_delete=models.SET_NULL, null=True, blank=True)
    booking_date = models.DateField(null=True, blank=True)
    time = models.ForeignKey(timeChoice, on_delete=models.SET_NULL, null=True, blank=True)

    senior_pwd_id = models.CharField(max_length=50, null=True, blank=True)
    senior_pwd_file = models.FileField(null=True, blank=True, upload_to="senior_pwd_file/")

    philhealth = models.CharField(max_length=120, null=True, blank=True)
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    middle_name = models.CharField(max_length=120, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True, )
    age = models.CharField(max_length=120, null=True, blank=True)
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=120, choices=GENDER, default='', null=True, blank=True)
    CIVIL_STATUS = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
        ('Annulled', 'Annulled'),
        ('Legally Separated', 'Legally Separated'),
    )
    civil_status = models.CharField(max_length=120, choices=CIVIL_STATUS, default='', null=True, blank=True)
    nationality = models.CharField(max_length=120, null=True, blank=True)
    occupation = models.CharField(max_length=120, null=True, blank=True)
    lot = models.CharField(max_length=120, null=True, blank=True)
    street = models.CharField(max_length=120, null=True, blank=True)
    brgy = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120, null=True, blank=True)
    province = models.CharField(max_length=120, null=True, blank=True)
    phone_no = models.CharField(max_length=120, null=True, blank=True)
    cp_no = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(max_length=120, null=True, blank=True)
    work_lot = models.CharField(max_length=120, null=True, blank=True)
    work_street = models.CharField(max_length=120, null=True, blank=True)
    work_brgy = models.CharField(max_length=120, null=True, blank=True)
    work_city = models.CharField(max_length=120, null=True, blank=True)
    work_province = models.CharField(max_length=120, null=True, blank=True)
    workplace = models.CharField(max_length=120, null=True, blank=True)
    work_contact_no = models.CharField(max_length=120, null=True, blank=True)
    work_email = models.CharField(max_length=120, null=True, blank=True)
    SELECT = [('YES', 'Yes'), ('NO', 'No')]
    covid_consultation = models.CharField(max_length=120, choices=SELECT, default='', null=True, blank=True)
    covid_consultation_date = models.DateField(null=True, blank=True)
    consult_facility = models.CharField(max_length=120, null=True, blank=True)
    health_facility = models.CharField(max_length=120, choices=SELECT, default='', null=True, blank=True)
    health_facility_date = models.DateField(null=True, blank=True)
    facility_name = models.CharField(max_length=120, null=True, blank=True)
    region_facility = models.CharField(max_length=120, null=True, blank=True)
    admitted_hospital = models.CharField(max_length=120, null=True, blank=True)
    admitted_hospital_date = models.DateTimeField(null=True, blank=True)
    admitted_facility = models.CharField(max_length=120, null=True, blank=True)
    admitted_facility_date = models.DateTimeField(null=True, blank=True)
    home_quarantine = models.CharField(max_length=120, null=True, blank=True)
    home_quarantine_date = models.DateTimeField(null=True, blank=True)
    discard_home = models.CharField(max_length=120, choices=SELECT, default='', null=True, blank=True)
    other_admitted = models.CharField(max_length=120, null=True, blank=True)
    discarge_date = models.DateField(null=True, blank=True)
    STATUS_CONSULT = [
        ('ASYMPTOMATIC', 'Asymptomatic'), ('MILD', 'Mild'), ('MODERATE', 'Moderate'),
        ('SEVERE', 'Severe'), ('CRITICAL', 'Critical')
    ]
    health_status_consult = models.CharField(max_length=120, choices=STATUS_CONSULT, default='', null=True, blank=True)
    CASE_CLASS = [('SUSPECT', 'Suspect'), ('PROBABLE', 'Probable'), ('CONFIRMED', 'Confirmed'),
                  ('NON-COVID-19-CASE', 'Non-Covid-19 Case')]
    case_classification = models.CharField(max_length=120, choices=CASE_CLASS, default='', null=True, blank=True)
    health_care_worker = models.CharField(max_length=120, choices=SELECT, default='', null=True, blank=True)
    health_care_worker_name = models.CharField(max_length=120, null=True, blank=True)
    return_ofw = models.CharField(max_length=120, choices=SELECT, default='', null=True, blank=True)
    return_ofw_country = models.CharField(max_length=120, null=True, blank=True)
    foreign_traveler = models.CharField(max_length=120, choices=SELECT, default='', null=True, blank=True)
    foreign_traveler_country = models.CharField(max_length=120, null=True, blank=True)
    local_stranded = models.CharField(max_length=120, choices=SELECT, default='', null=True, blank=True)
    local_stranded_city = models.CharField(max_length=120, null=True, blank=True)
    live_closed = models.CharField(max_length=120, choices=SELECT, default='', null=True, blank=True)
    live_closed_name = models.CharField(max_length=120, null=True, blank=True)
    current_lot = models.CharField(max_length=120, null=True, blank=True)
    current_street = models.CharField(max_length=120, null=True, blank=True)
    current_brgy = models.CharField(max_length=120, null=True, blank=True)
    current_city = models.CharField(max_length=120, null=True, blank=True)
    current_province = models.CharField(max_length=120, null=True, blank=True)
    current_phone_no = models.CharField(max_length=120, null=True, blank=True)
    current_cp_no = models.CharField(max_length=120, null=True, blank=True)
    current_email = models.EmailField(max_length=120, null=True, blank=True)
    ofw_lot = models.CharField(max_length=120, null=True, blank=True)
    ofw_street = models.CharField(max_length=120, null=True, blank=True)
    ofw_city = models.CharField(max_length=120, null=True, blank=True)
    ofw_province = models.CharField(max_length=120, null=True, blank=True)
    ofw_country = models.CharField(max_length=120, null=True, blank=True)
    ofw_workplace = models.CharField(max_length=120, null=True, blank=True)
    ofw_employer = models.CharField(max_length=120, null=True, blank=True)
    ofw_contact_no = models.CharField(max_length=120, null=True, blank=True)
    date_onset = models.DateField(null=True, blank=True)
    asympto = models.BooleanField(default=False, null=True, blank=True)
    fever = models.BooleanField(default=False, null=True, blank=True)
    fever_temp = models.CharField(max_length=120, null=True, blank=True)
    cough = models.BooleanField(default=False, null=True, blank=True)
    general_weak = models.BooleanField(default=False, null=True, blank=True)
    fatigue = models.BooleanField(default=False, null=True, blank=True)
    headache = models.BooleanField(default=False, null=True, blank=True)
    myalgia = models.BooleanField(default=False, null=True, blank=True)
    sore_throat = models.BooleanField(default=False, null=True, blank=True)
    coryza = models.BooleanField(default=False, null=True, blank=True)
    dyspnea = models.BooleanField(default=False, null=True, blank=True)
    anorexia = models.BooleanField(default=False, null=True, blank=True)
    nausea = models.BooleanField(default=False, null=True, blank=True)
    vomiting = models.BooleanField(default=False, null=True, blank=True)
    diarrhea = models.BooleanField(default=False, null=True, blank=True)
    altered_mental = models.BooleanField(default=False, null=True, blank=True)
    anosmia = models.BooleanField(default=False, null=True, blank=True)
    aguesia = models.BooleanField(default=False, null=True, blank=True)
    other_symptoms = models.CharField(max_length=120, null=True, blank=True)
    como_none = models.BooleanField(default=False, null=True, blank=True)
    gastro = models.BooleanField(default=False, null=True, blank=True)
    hyper = models.BooleanField(default=False, null=True, blank=True)
    genito = models.BooleanField(default=False, null=True, blank=True)
    diabetes = models.BooleanField(default=False, null=True, blank=True)
    neuro = models.BooleanField(default=False, null=True, blank=True)
    heart_d = models.BooleanField(default=False, null=True, blank=True)
    cancer = models.BooleanField(default=False, null=True, blank=True)
    lung_d = models.BooleanField(default=False, null=True, blank=True)
    como_others = models.CharField(max_length=120, null=True, blank=True)
    pregnant = models.CharField(max_length=120, choices=SELECT, default='', null=True, blank=True)
    pregnant_lmp = models.CharField(max_length=120, null=True, blank=True)
    risk_pregnant = models.CharField(max_length=120, choices=SELECT, default='', null=True, blank=True)
    diag_sari = models.CharField(max_length=120, choices=SELECT, default='', null=True, blank=True)
    chest_radio = models.BooleanField(default=False, null=True, blank=True)
    chest_radio_finding = models.CharField(max_length=120, null=True, blank=True)
    chest_ct = models.BooleanField(default=False, null=True, blank=True)
    chest_ct_finding = models.CharField(max_length=120, null=True, blank=True)
    lung_ultra = models.BooleanField(default=False, null=True, blank=True)
    lung_ultra_finding = models.CharField(max_length=120, null=True, blank=True)
    chest_imaging_none = models.BooleanField(default=False, null=True, blank=True)

    TEST_RESULT = [('PENDING', 'Pending'), ('NEGATIVE', 'Negative'), ('POSITIVE', 'Positive'),
                   ('EQUIVOCAL', 'Equivocal')]

    rt_pcr_ops = models.BooleanField(default=False, null=True, blank=True)
    rt_pcr_ops_date = models.DateField(null=True, blank=True)
    rt_pcr_ops_lab = models.CharField(max_length=120, null=True, blank=True)
    rt_pcr_ops_result = models.CharField(max_length=120, choices=TEST_RESULT, default='', null=True, blank=True)
    rt_pcr_ops_date_release = models.DateField(null=True, blank=True)

    rt_pcr_nps = models.BooleanField(default=False, null=True, blank=True)
    rt_pcr_nps_date = models.DateField(null=True, blank=True)
    rt_pcr_nps_lab = models.CharField(max_length=120, null=True, blank=True)
    rt_pcr_nps_result = models.CharField(max_length=120, choices=TEST_RESULT, default='', null=True, blank=True)
    rt_pcr_nps_date_release = models.DateField(null=True, blank=True)

    rt_pcr_ops_nps = models.BooleanField(default=False, null=True, blank=True)
    rt_pcr_ops_nps_date = models.DateField(null=True, blank=True)
    rt_pcr_ops_nps_lab = models.CharField(max_length=120, null=True, blank=True)
    rt_pcr_ops_nps_result = models.CharField(max_length=120, choices=TEST_RESULT, default='', null=True, blank=True)
    rt_pcr_ops_nps_date_release = models.DateField(null=True, blank=True)

    rt_pcr = models.BooleanField(default=False, null=True, blank=True)
    rt_pcr_specimen = models.CharField(max_length=120, null=True, blank=True)
    rt_pcr_specimen_date = models.DateField(null=True, blank=True)
    rt_pcr_specimen_lab = models.CharField(max_length=120, null=True, blank=True)
    rt_pcr_specimen_result = models.CharField(max_length=120, choices=TEST_RESULT, default='', null=True, blank=True)
    rt_pcr_specimen_date_release = models.DateField(null=True, blank=True)

    antigen = models.BooleanField(default=False, null=True, blank=True)
    antigen_date = models.DateField(null=True, blank=True)
    antigen_lab = models.CharField(max_length=120, null=True, blank=True)
    antigen_result = models.CharField(max_length=120, choices=TEST_RESULT, default='', null=True, blank=True)
    antigen_date_release = models.DateField(null=True, blank=True)

    ANTIBODY_RESULT = [('lgM(+)lgG(-)', 'lgM(+)lgG(-)'), ('lgM(+)lgG(+)', 'lgM(+)lgG(+)'),
                       ('lgM(-)lgG(+)', 'lgM(-)lgG(+)'), ('lgM(-)lgG(-)', 'lgM(-)lgG(-)')]

    antibody = models.BooleanField(default=False, null=True, blank=True)
    antibody_date = models.DateField(null=True, blank=True)
    antibody_lab = models.CharField(max_length=120, null=True, blank=True)
    antibody_result = models.CharField(max_length=120, choices=ANTIBODY_RESULT, default='', null=True, blank=True)
    antibody_date_release = models.DateField(null=True, blank=True)

    test_others = models.BooleanField(default=False, null=True, blank=True)
    test_others_date = models.DateField(null=True, blank=True)
    test_others_lab = models.CharField(max_length=120, null=True, blank=True)
    test_others_result = models.CharField(max_length=120, null=True, blank=True)
    test_others_date_release = models.DateField(null=True, blank=True)

    test_positive = models.CharField(max_length=120, choices=SELECT, default='', null=True, blank=True)
    test_positive_date = models.DateField(null=True, blank=True)
    test_positive_lab = models.CharField(max_length=120, null=True, blank=True)
    test_positive_number = models.CharField(max_length=120, null=True, blank=True)

    current_admitted = models.CharField(max_length=120, choices=SELECT, default='', null=True, blank=True)
    recovered_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    immediate_cause = models.CharField(max_length=120, null=True, blank=True)
    antecendent_cause = models.CharField(max_length=120, null=True, blank=True)
    underlying_cause = models.CharField(max_length=120, null=True, blank=True)

    SELECT2 = [('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')]
    history_exposure = models.CharField(max_length=120, choices=SELECT2, default='', null=True, blank=True)
    history_date = models.DateField(null=True, blank=True)
    history_place = models.CharField(max_length=120, choices=SELECT2, default='', null=True, blank=True)

    health_facility_visit = models.BooleanField(default=False, null=True, blank=True)
    health_facility_visit_details = models.CharField(max_length=120, null=True, blank=True)
    health_facility_visit_date = models.DateField(null=True, blank=True)

    closed_setting_visit = models.BooleanField(default=False, null=True, blank=True)
    closed_setting_visit_details = models.CharField(max_length=120, null=True, blank=True)
    closed_setting_visit_date = models.DateField(null=True, blank=True)

    market_visit = models.BooleanField(default=False, null=True, blank=True)
    market_visit_details = models.CharField(max_length=120, null=True, blank=True)
    market_visit_date = models.DateField(null=True, blank=True)

    home_visit = models.BooleanField(default=False, null=True, blank=True)
    home_visit_details = models.CharField(max_length=120, null=True, blank=True)
    home_visit_date = models.DateField(null=True, blank=True)

    int_travel_visit = models.BooleanField(default=False, null=True, blank=True)
    int_travel_visit_details = models.CharField(max_length=120, null=True, blank=True)
    int_travel_visit_date = models.DateField(null=True, blank=True)

    school_visit = models.BooleanField(default=False, null=True, blank=True)
    school_visit_details = models.CharField(max_length=120, null=True, blank=True)
    school_visit_date = models.DateField(null=True, blank=True)

    transpo_visit = models.BooleanField(default=False, null=True, blank=True)
    transpo_visit_details = models.CharField(max_length=120, null=True, blank=True)
    transpo_visit_date = models.DateField(null=True, blank=True)

    workplace_visit = models.BooleanField(default=False, null=True, blank=True)
    workplace_visit_details = models.CharField(max_length=120, null=True, blank=True)
    workplace_visit_date = models.DateField(null=True, blank=True)

    local_travel_visit = models.BooleanField(default=False, null=True, blank=True)
    local_travel_visit_details = models.CharField(max_length=120, null=True, blank=True)
    local_travel_visit_date = models.DateField(null=True, blank=True)

    gathering_visit = models.BooleanField(default=False, null=True, blank=True)
    gathering_visit_details = models.CharField(max_length=120, null=True, blank=True)
    gathering_visit_date = models.DateField(null=True, blank=True)

    other_visit = models.BooleanField(default=False, null=True, blank=True)
    other_visit_details = models.CharField(max_length=120, null=True, blank=True)
    other_visit_date = models.DateField(null=True, blank=True)

    travel_history = models.CharField(max_length=120, choices=SELECT, default='', null=True, blank=True)
    travel_history_country = models.CharField(max_length=120, null=True, blank=True)
    travel_history_airline = models.CharField(max_length=120, null=True, blank=True)
    travel_history_airline_number = models.CharField(max_length=120, null=True, blank=True)
    travel_history_airline_depart = models.DateField(null=True, blank=True)
    travel_history_airline_arival = models.DateField(null=True, blank=True)

    travel_history_local = models.CharField(max_length=120, choices=SELECT, default='', null=True, blank=True)
    travel_history_local_place = models.CharField(max_length=120, null=True, blank=True)
    travel_history_local_airline = models.CharField(max_length=120, null=True, blank=True)
    travel_history_local_airline_number = models.CharField(max_length=120, null=True, blank=True)
    travel_history_local_airline_depart = models.DateField(null=True, blank=True)
    travel_history_local_airline_arival = models.DateField(null=True, blank=True)

    household_contacts_name1 = models.CharField(max_length=120, null=True, blank=True)
    household_contacts_number1 = models.CharField(max_length=120, null=True, blank=True)
    household_contacts_setting1 = models.CharField(max_length=120, null=True, blank=True)

    household_contacts_name2 = models.CharField(max_length=120, null=True, blank=True)
    household_contacts_number2 = models.CharField(max_length=120, null=True, blank=True)
    household_contacts_setting2 = models.CharField(max_length=120, null=True, blank=True)

    household_contacts_name3 = models.CharField(max_length=120, null=True, blank=True)
    household_contacts_number3 = models.CharField(max_length=120, null=True, blank=True)
    household_contacts_setting3 = models.CharField(max_length=120, null=True, blank=True)

    household_contacts_name4 = models.CharField(max_length=120, null=True, blank=True)
    household_contacts_number4 = models.CharField(max_length=120, null=True, blank=True)
    household_contacts_setting4 = models.CharField(max_length=120, null=True, blank=True)

    household_contacts_name5 = models.CharField(max_length=120, null=True, blank=True)
    household_contacts_number5 = models.CharField(max_length=120, null=True, blank=True)
    household_contacts_setting5 = models.CharField(max_length=120, null=True, blank=True)

    household_contacts_name6 = models.CharField(max_length=120, null=True, blank=True)
    household_contacts_number6 = models.CharField(max_length=120, null=True, blank=True)
    household_contacts_setting6 = models.CharField(max_length=120, null=True, blank=True)

    household_contacts_name7 = models.CharField(max_length=120, null=True, blank=True)
    household_contacts_number7 = models.CharField(max_length=120, null=True, blank=True)
    household_contacts_setting7 = models.CharField(max_length=120, null=True, blank=True)

    household_contacts_name8 = models.CharField(max_length=120, null=True, blank=True)
    household_contacts_number8 = models.CharField(max_length=120, null=True, blank=True)
    household_contacts_setting8 = models.CharField(max_length=120, null=True, blank=True)

    household_contacts_name9 = models.CharField(max_length=120, null=True, blank=True)
    household_contacts_number9 = models.CharField(max_length=120, null=True, blank=True)
    household_contacts_setting9 = models.CharField(max_length=120, null=True, blank=True)

    waiver = models.CharField(max_length=120, null=True, blank=True)

    PAYMENT = [
        ('PENDING', 'Pending'),
        ('VERIFIED', 'Verified'),
    ]
    PAYMENT_METHOD = [
        ('', ''),
        ('CASH', 'Cash'),
        ('BANK', 'Bank'),
        ('PAYPAL', 'Paypal'),
    ]
    payment_status = models.CharField(max_length=20, choices=PAYMENT, default='PENDING', null=True, blank=True)
    refund_discount = models.IntegerField(null=True, blank=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='', null=True, blank=True)
    payment_reference = models.CharField(max_length=20, null=True, blank=True)
    STATUS = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
    ]
    test_result_status = models.CharField(max_length=20, choices=STATUS, default='PENDING', null=True, blank=True)
    pending_test = models.CharField(max_length=20, choices=STATUS, default='PENDING', null=True, blank=True)
    pending_result = models.CharField(max_length=20, choices=STATUS, default='PENDING', null=True, blank=True)
    result_sent = models.CharField(max_length=20, choices=STATUS, default='PENDING', null=True, blank=True)
    result_file = models.FileField(null=True, blank=True, upload_to="result_file/")


    def __str__(self):
        return self.first_name + '' + self.last_name

    class Meta:
        permissions = [('email_corporate', 'Can Email')]

    def save(self, *args, **kwargs):
        if self.reference_number is None:
            self.reference_number = str(uuid.uuid4())[:11].replace('-', '').lower()
        return super().save(*args, **kwargs)

    @property
    def get_total(self):
        total = self.product.price
        return total

    @property
    def get_discount(self):
        if self.refund_discount is not None and self.senior_pwd_id is not None:
            discount = self.refund_discount + (0.2 * float(self.get_total))
        elif self.senior_pwd_id is not None:
            discount = 0.2 * float(self.get_total)
        elif self.refund_discount is not None:
            discount = self.refund_discount
        else:
            discount = None
        return discount

    @property
    def get_total_price_after_discount(self):
        if self.refund_discount is not None:
            total_price = self.get_total - int(self.refund_discount)
        elif self.senior_pwd_id is not None:
            total_price = float(self.get_total) - self.get_discount
        else:
            total_price = self.get_total
        return total_price

    def get_absolute_url(self):
        return reverse('corporate_detail', kwargs={'pk': self.pk})


class lab_Corporate(models.Model):
    client = models.ForeignKey(Corporate, on_delete=models.SET_NULL, null=True, blank=True)
    result_file = models.FileField(null=True, blank=True, upload_to="result_file/")
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.client)