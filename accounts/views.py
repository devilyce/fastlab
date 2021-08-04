from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import generic

from accounts.forms import CreateUserForm, userForm
from accounts.token import account_activation_token


@permission_required('auth.add_user')
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        group = request.POST['group']
        group = Group.objects.get(id=group)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.is_active = False
            username = form.cleaned_data.get('username')
            user.groups.add(group)
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            message = render_to_string('accounts/mail/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            messages.success(request, 'Account was created for ' + username)

    context = {'form': form}
    return render(request, 'registration/create_user.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('management')
    else:
        return render(request, 'registration/activation_invalid.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('management')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'registration/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


class user_profile(generic.UpdateView):
    form_class = userForm
    template_name = 'accounts/user_profile.html'
    success_url = reverse_lazy('user_profile')

    def get_object(self):
        return self.request.user

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['data'] = profileForm()
    #     return context


class change_password(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "accounts/change_password.html"
    success_url = reverse_lazy('user_profile')


# def user_profile(request):
#     if request.method == 'POST':
#         u_form = userForm(instance=request.user)
#         p_form = profileForm(instance=request.user)
#         if u_form.is_valid() or p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.info(request, 'Your profile has been updated')
#             return redirect('user_profile')
#     else:
#         u_form = userForm(instance=request.user)
#         p_form = profileForm(instance=request.user)
#
#     context = {'u_form': u_form, 'p_form': p_form}
#     return render(request, 'accounts/user_profile.html', context)