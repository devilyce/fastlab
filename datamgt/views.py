from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic import UpdateView, DetailView, CreateView, ListView

from clients.forms import clinic_ClientForms, lab_ClientForms, ClientForms
from clients.models import Client
from corporate.forms import CorporateFrom, clinic_CorporateForms, booking_CorporateForms, lab_CorporateForms
from corporate.models import Corporate
from customers.forms import admin_edit_CustomerForms
from customers.models import Customers


def is_valid_query(param):
    return param != '' and param is not None


@login_required
def management(request):
    return render(request, 'datamgt/pages/datamgt.html', {})


class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            return redirect('management')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)


class view_appointment(UserAccessMixin, ListView):
    permission_required = 'customers.view_customers'
    model = Customers
    template_name = 'datamgt/pages/view_appointment.html'
    context_object_name = 'data'


class view_clients(UserAccessMixin, ListView):
    permission_required = 'clients.view_client'
    model = Client
    template_name = 'datamgt/pages/view_clients.html'
    context_object_name = 'data'


class view_corporate(UserAccessMixin, ListView):
    permission_required = 'corporate.view_corporate'
    model = Corporate
    template_name = 'datamgt/pages/view_corporate.html'
    context_object_name = 'data'

    def get_queryset(self):
        if self.request.user.groups.filter(name='corporate').exists():
            return Corporate.objects.filter(user=self.request.user)
        else:
            return Corporate.objects.all()


class admin_create_appointment(UserAccessMixin, CreateView):
    permission_required = 'corporate.add_corporate'
    model = Corporate
    form_class = CorporateFrom
    template_name = 'datamgt/pages/create_appointment.html'

    def post(self, request, *args, **kwargs):
        form = CorporateFrom(request.POST or None, request.FILES or None)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user
            fs.save()
        return self.form_valid(form)


class corporate_detail(UserAccessMixin, DetailView):
    permission_required = 'corporate.view_corporate'
    model = Corporate
    template_name_suffix = '_detail'
    context_object_name = 'data'


class corporate_print(UserAccessMixin, DetailView):
    permission_required = 'corporate.view_corporate'
    model = Corporate
    template_name_suffix = '_print'
    context_object_name = 'data'

class corporate_print_health_dec(UserAccessMixin, DetailView):
    permission_required = 'corporate.view_corporate'
    model = Corporate
    template_name_suffix = '_print_health_dec'
    context_object_name = 'form'

class corporate_detail_edit(UserAccessMixin, UpdateView):
    permission_required = 'corporate.change_corporate'
    model = Corporate
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.object
        return context

    def get_template_names(self):
        if self.request.user.groups.filter(name='clinic').exists():
            return 'corporate/corporate_clinic_update.html'
        else:
            return 'corporate/corporate_booking_update.html'

    def get_form_class(self):
        if self.request.user.groups.filter(name='clinic').exists():
            return clinic_CorporateForms
        return booking_CorporateForms


class admin_view_appointment(UserAccessMixin, DetailView):
    permission_required = 'customers.view_customers'
    model = Customers
    template_name_suffix = '_detail'
    context_object_name = 'data'


class customers_print(UserAccessMixin, DetailView):
    permission_required = 'customers.view_customers'
    model = Customers
    template_name_suffix = '_print'
    context_object_name = 'data'


class admin_view_appointment_edit(UserAccessMixin, UpdateView):
    permission_required = 'customers.change_customers'
    model = Customers
    form_class = admin_edit_CustomerForms
    template_name_suffix = '_update_form'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.object
        return context

@permission_required('customers.change_customers')
def client_fill_up_onsite(request, pk):
    form = ClientForms()

    if request.method == 'POST':
        form = ClientForms(request.POST)
        ref = Customers.objects.get(pk=pk)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.reference_number = ref
            fs.save()
            return redirect('view_clients')

    context = {'form': form}
    return render(request, 'clients/client_fill_up_onsite.html', context)

class admin_view_client(UserAccessMixin, DetailView):
    permission_required = 'clients.view_client'
    model = Client
    template_name_suffix = '_detail'
    context_object_name = 'data'


class client_print(UserAccessMixin, DetailView):
    permission_required = 'clients.view_client'
    model = Client
    template_name_suffix = '_print'
    context_object_name = 'data'

class client_print_health_dec(UserAccessMixin, DetailView):
    permission_required = 'clients.view_client'
    model = Client
    template_name_suffix = '_print_health_dec'
    context_object_name = 'form'

class clinic_view_client_edit(UserAccessMixin, UpdateView):
    permission_required = 'clients.change_client'
    model = Client
    form_class = clinic_ClientForms
    template_name = 'clients/client_clinic_update.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.object
        return context

@permission_required('clients.email_client')
def lab_view_client_edit(request, pk):
    data = Client.objects.get(pk=pk)
    form = lab_ClientForms()
    if request.method == 'POST':
        email = Client.objects.get(pk=pk).email
        form = lab_ClientForms(request.POST, request.FILES)
        subject = 'Test Result'
        message = render_to_string('mail/test_result.html', {
        })
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]
        mail = EmailMessage(subject, message, from_email, recipient_list)
        mail.content_subtype = 'html'
        file = request.FILES['result_file']
        mail.attach(file.name, file.read(), file.content_type)
        mail.send()
        messages.success(request, 'Email Sent')

        client = Client.objects.get(pk=pk)
        client.pending_result = 'COMPLETED'
        client.result_sent = 'COMPLETED'
        client.result_file = request.FILES['result_file']
        client.save()


    context = {'data': data, 'form': form}
    return render(request, 'clients/client_lab_update.html', context)


# @login_required
@permission_required('corporate.email_corporate')
def lab_view_corporate_edit(request, pk):
    data = Corporate.objects.get(pk=pk)
    form = lab_CorporateForms()
    if request.method == 'POST':
        email = Corporate.objects.get(pk=pk).user.email
        cc = Corporate.objects.get(pk=pk).email
        client = Corporate.objects.get(pk=pk)
        form = lab_CorporateForms(request.POST, request.FILES)
        subject = 'Test Result'
        message = render_to_string('mail/test_result.html', {})
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email, cc]
        mail = EmailMessage(subject, message, from_email, recipient_list)
        mail.content_subtype = 'html'
        file = request.FILES['result_file']
        mail.attach(file.name, file.read(), file.content_type)
        mail.send()
        messages.success(request, 'Email Sent')

        client.pending_result = 'COMPLETED'
        client.result_sent = 'COMPLETED'
        client.result_file = request.FILES['result_file']
        client.save()

    context = {'data': data, 'form': form}
    return render(request, 'corporate/corporate_lab_update.html', context)


def admin_success(request):
    return render(request, 'datamgt/pages/success.html')

# def datamgt(request):
#     data = Customers.objects.all()
#     # booked = booked.filter(set_date=datetime.date.today())
#     reference_number_query = request.GET.get('reference_number')
#     payment_status_query = request.GET.get('payment_status')
#     test_result_status_query = request.GET.get('test_result_status')
#     date_day_query = request.GET.get('date_day')
#     date_month_query = request.GET.get('date_month')
#     date_year_query = request.GET.get('date_year')
#
#     if is_valid_query(reference_number_query):
#         data = data.filter(reference_number__icontains=reference_number_query)
#
#     if is_valid_query(payment_status_query):
#         data = data.filter(payment_status__icontains=payment_status_query)
#
#     if is_valid_query(test_result_status_query):
#         data = data.filter(test_result_status__icontains=test_result_status_query)
#
#     if is_valid_query(date_day_query):
#         data = data.filter(set_date=date_day_query)
#
#     if is_valid_query(date_month_query):
#         data = data.filter(set_date__month=date_month_query)
#
#     if date_year_query == '' or date_year_query is None:
#         data = data.filter(set_date__year=datetime.date.today().year)
#
#     elif is_valid_query(date_year_query):
#         data = data.filter(set_date__year=date_year_query)
#
#     context = {
#         'data': data
#     }
#     return render(request, 'datamgt/pages/datamgt.html', context)
