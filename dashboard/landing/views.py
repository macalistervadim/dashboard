from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView,\
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.base import TemplateView
from django.core.signing import BadSignature
from django.contrib.auth import logout

from .models import AdvUser, ProfileEditForm
from .forms import RegisterForm
from .utilities import signer

def index(request):
    return render(request, 'main/index.html')

def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))

class BBLoginView(LoginView):
    template_name = 'main/login.html'

@login_required
def profile(request):
    return render(request, 'main/profile.html')

class BBLogoutView(LogoutView):
    pass

class ProfileEditView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'main/profile_edit.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('landing:profile')
    success_message = 'Данные пользователя изменены.'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

class PasswordEditView(SuccessMessageMixin, LoginRequiredMixin,
                       PasswordChangeView):
    template_name = 'main/password_edit.html'
    success_url = reverse_lazy('landing:profile')
    success_message = 'Пароль пользователя успешно изменен.'

class RegisterView(CreateView):
    model = AdvUser
    template_name = 'main/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('landing:register_done')

class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'

def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'main/activation_failed.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated == True:
        template = 'main/activation_done_earlier.html'
    else:
        template = 'main/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)

class ProfileDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name = 'main/profile_delete.html'
    success_url = reverse_lazy('landing:index')
    success_message = 'Пользователь удален'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

class PasswordResetView(PasswordResetView):
    template_name = 'main/password_reset.html'
    success_url = reverse_lazy('landing:pass_reset_done')
    subject_template_name = 'email/reset_subject.txt'
    email_template_name = 'email/reset_body.txt'

class PasswordReserDoneView(PasswordResetDoneView):
    template_name = 'main/password_reset_done.html'


class PasswordResetConfirmView(PasswordResetConfirmView):
        template_name = 'main/password_reset_pass.html'
        success_url = reverse_lazy('landing:pass_reset_complete')

class PasswordResetCompleteView(PasswordResetCompleteView):
    tempate_name = 'main/password_reset_complete.html'