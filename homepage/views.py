import calendar
import datetime
from datetime import date

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from cal.models import setYear, setMonth, setDay, setTime
from clients.forms import ClientForms
from clients.models import Client
from customers.models import Customers
from fastlab import settings
from homepage.forms import ContactForm
from orderitem.forms import OrderItemForms
from orderitem.models import OrderItem
from products.models import Product


def home(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form_full_name = request.POST['name']
            form_subject = form.cleaned_data['subject']
            form_email = form.cleaned_data['from_email']
            form_message = form.cleaned_data['message']
            message = '%s: %s: %s: %s' % (
                form_full_name,
                form_email,
                form_subject,
                form_message,
            )
            subject = 'Site Contact Form'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [from_email, 'fastlabtest@gmail.com']
            try:
                email = send_mail(subject, message, from_email, recipient_list)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('mail_sent')
    return render(request, 'homepage/pages/home.html', {'form': form})


def mail_sent(request):
    return render(request, 'homepage/pages/mail_sent.html')


class book_now(ListView):
    model = Product
    template_name = 'homepage/pages/book_now.html'


class create_appointment(CreateView):
    model = OrderItem
    form_class = OrderItemForms
    template_name = 'homepage/pages/create_appointment.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_today = date.today()
        orderitem = OrderItem.objects.filter(first_name=first_name, last_name=last_name, date_added=date_today).count()
        if orderitem != 0:
            return redirect('error')
        return self.form_valid(form)

def confirm_appointment(request, pk):
    orderitem = OrderItem.objects.get(pk=pk)
    date_today = date.today()
    current_site = get_current_site(request)

    if request.method == 'POST':
        for instance in Customers.objects.all():
            if (instance.last_name == orderitem.last_name) and (instance.first_name == orderitem.first_name):
                if instance.date_added == date_today:
                    return redirect('error')
        Customers.objects.create(
            product=orderitem.product,
            number_of_person=orderitem.number_of_person,
            test_location=orderitem.test_location,
            booking_date=orderitem.day,
            time=orderitem.time,
            first_name=orderitem.first_name,
            last_name=orderitem.last_name,
            middle_name=orderitem.middle_name,
            email=orderitem.email,
            contact_number=orderitem.contact_number,
            nationality=orderitem.nationality,
            civil_status=orderitem.civil_status,
            date_of_birth=orderitem.date_of_birth,
            gender=orderitem.gender,
            address=orderitem.address,
            senior_pwd_id=orderitem.senior_pwd_id,
            senior_pwd_file=orderitem.senior_pwd_file,
        )

        return redirect('success')

    context = {'orderitem': orderitem}
    return render(request, 'homepage/pages/confirm_appointment.html', context)

def health_declaration(request, pk):
    form = ClientForms()
    if request.method == 'POST':
        form = ClientForms(request.POST)
        ref = Customers.objects.get(pk=pk)
        ref_num_p = ref.number_of_person
        ref_count = ref.count
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_today = date.today()
        client = Client.objects.filter(first_name=first_name, last_name=last_name, date_added=date_today).count()
        if ref_count < ref_num_p :
            if client == 0:
                if form.is_valid():
                    fs = form.save(commit=False)
                    fs.reference_number = ref
                    ref.count += 1
                    ref.save()
                    fs.save()
                    return redirect('success')
        return redirect('error')

    context = {'form': form}
    return render(request, 'homepage/pages/health_declaration.html', context)


def success(request):
    return render(request, 'homepage/pages/success.html')


def error(request):
    return render(request, 'homepage/pages/error.html')


def get_json_year_data(request):
    year = datetime.datetime.now().year
    qs_year = setYear.objects.filter(name__gte=year).values()
    qs_list = list(qs_year)
    return JsonResponse({'data': qs_list})


def get_json_month_data(request, *args, **kwargs):
    selected_year = kwargs.get('year')
    start_date = datetime.date.today() - datetime.timedelta(days=31)
    days_in_month = calendar.monthrange(start_date.year, start_date.month)[1]
    enddate = start_date + datetime.timedelta(days=days_in_month * 10)
    obj_month = list(setMonth.objects.filter(year__name=selected_year, date__range=[start_date, enddate]).values())
    return JsonResponse({'data': obj_month})


def get_json_day_data(request, *args, **kwargs):
    selected_month = kwargs.get('month')
    start_date = datetime.date.today()
    days_in_month = calendar.monthrange(start_date.year, start_date.month)[1]
    enddate = start_date + datetime.timedelta(days=days_in_month * 10)
    obj_day = list(setDay.objects.filter(month__name=selected_month, date__range=[start_date, enddate]).values())
    return JsonResponse({'data': obj_day})


def get_json_time_data(request, *args, **kwargs):
    selected_day = kwargs.get('day')
    obj_time = list(setTime.objects.filter(date=selected_day).exclude(count=4).values())
    return JsonResponse({'data': obj_time})
