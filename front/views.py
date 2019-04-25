from django.views.generic import TemplateView
from django.shortcuts import HttpResponseRedirect

from front.models import Plan, Level


class IndexView(TemplateView):
    template_name = 'front/index.html'


class AboutUsView(TemplateView):
    template_name = 'front/about_us.html'

class RegisterView(TemplateView):
    template_name = 'front/register.html'

    def post(self, request):
        return HttpResponseRedirect('/')

class PaymentHistoryView(TemplateView):
    template_name = 'front/payment-history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payments'] = ['payment1', 'payment2']
        return context

class CallPageView(TemplateView):
    template_name = 'front/call_page.html'

class AddKidView(TemplateView):
    template_name = 'front/add_kid.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['levels'] = Level.objects.all()
        return context


class RegisterTutor2View(TemplateView):
    template_name = 'front/register_tutor_2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['levels'] = Level.objects.all()
        return context

class PaymentPageView(TemplateView):
    template_name = 'front/payment_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plans'] = Plan.objects.all()
        return context

class EditKidInfoView(TemplateView):
    template_name = 'front/edit_kid_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['levels'] = Level.objects.all()
        return context

class EditparentInfoView(TemplateView):
    template_name = 'front/edit_parent_info.html'


class KidAccountView(TemplateView):
    template_name = 'front/kid_account.html'


class LoginView(TemplateView):
    template_name = 'front/login.html'

class MyAccountView(TemplateView):
    template_name = 'front/my_account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kids'] = ['Jean-Michel', 'Jean-Eudes', 'Jean-Chirstophe']
        return context


class PleaseWaitView(TemplateView):
    template_name = 'front/please_wait.html'

class RegisterKidView(TemplateView):
    template_name = 'front/register_kid.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['levels'] = Level.objects.all()
        return context

class RegisterParentView(TemplateView):
    template_name = 'front/register_parent.html'

class RegisterTutor1View(TemplateView):
    template_name = 'front/register_tutor_1.html'

class RegisterTutor3View(TemplateView):
    template_name = 'front/register_tutor_3.html'

class RegisterTutorView(TemplateView):
    template_name = 'front/register_tutor.html'

class SorryNoMinsView(TemplateView):
    template_name = 'front/sorry_no_mins.html'

class SorryNoTutorView(TemplateView):
    template_name = 'front/sorry_no_tutor.html'

class SubscriptionConfirmationView(TemplateView):
    template_name = 'front/subscription_confirmation.html'

class TermsConditionsParentsView(TemplateView):
    template_name = 'front/terms_conditions_parents.html'

class TermsConditionsTutorsView(TemplateView):
    template_name = 'front/terms_conditions_tutors.html'

class SessionThankYouTutorView(TemplateView):
    template_name = 'front/session_thank_you_tutor.html'

class SessionThankYouView(TemplateView):
    template_name = 'front/session_thank_you.html'

class TutoDetailsView(TemplateView):
    template_name = 'front/tuto_details.html'

class TutorAccountView(TemplateView):
    template_name = 'front/tutor_account.html'

class TutorInvoiceHistoryView(TemplateView):
    template_name = 'front/tutor_invoice_history.html'

class WelcomeView(TemplateView):
    template_name = 'front/welcome.html'

class ForgotLogin1View(TemplateView):
    template_name = 'front/forgot_login1.html'

class ForgotLogin2View(TemplateView):
    template_name = 'front/forgot_login2.html'

class PaymentConfirmationView(TemplateView):
    template_name = 'front/payment_confirmation.html'

class ChooseKidNameView(TemplateView):
    template_name = 'front/choose_kid_name.html'

class ChooseSubjectView(TemplateView):
    template_name = 'front/choose_subject.html'

class EditTutorInfo1(TemplateView):
    template_name = 'front/edit_tutor_info_1.html'

class EditTutorInfo2(TemplateView):
    template_name = 'front/edit_tutor_info_2.html'

class EditTutorInfo3(TemplateView):
    template_name = 'front/edit_tutor_info_3.html'

class ChangePass(TemplateView):
    template_name = 'front/change_pass.html'

class ForgotLoginTutor1View(TemplateView):
    template_name = 'front/forgot_login_tutor1.html'

class ForgotLoginTutor2View(TemplateView):
    template_name = 'front/forgot_login_tutor2.html'

class ForgotUser1View(TemplateView):
    template_name = 'front/forgot_user1.html'

class ForgotUser2View(TemplateView):
    template_name = 'front/forgot_user2.html'

class LoginTutorView(TemplateView):
    template_name = 'front/login_tutor.html'

class NewPass(TemplateView):
    template_name = 'front/new_pass.html'

class SubscriptionConfirmationTutorView(TemplateView):
    template_name = 'front/subscription_confirmation_tutor.html'
