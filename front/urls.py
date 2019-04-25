from django.urls import path

from . import views

urlpatterns = [
    path('index', views.IndexView.as_view(), name = 'index'),
    path('about_us', views.AboutUsView.as_view(), name = 'about_us'),
    path('register', views.RegisterView.as_view(), name = 'register'),
    path('call_page', views.CallPageView.as_view(), name = 'call_page'),
    path('add_kid', views.AddKidView.as_view(), name = 'add_kid'),
    path('register_tutor_2', views.RegisterTutor2View.as_view(), name = 'register_tutor_2'),
    path('payment_page', views.PaymentPageView.as_view(), name = 'payment_page'),
    path('choose_kid_name', views.ChooseKidNameView.as_view(), name = 'choose_kid_name'),
    path('choose_subject', views.ChooseSubjectView.as_view(), name = 'choose_subject'),
    path('edit_kid_info', views.EditKidInfoView.as_view(), name = 'edit_kid_info'),
    path('edit_parent_info', views.EditparentInfoView.as_view(), name = 'edit_parent_info'),
    path('kid_account/<int:id>/', views.KidAccountView.as_view(), name = 'kid_account'),
    path('login', views.LoginView.as_view(), name = 'login'),
    path('my_account', views.MyAccountView.as_view(), name = 'my_account'),
    path('please_wait', views.PleaseWaitView.as_view(), name = 'please_wait'),
    path('register_kid', views.RegisterKidView.as_view(), name = 'register_kid'),
    path('register_parent', views.RegisterParentView.as_view(), name = 'register_parent'),
    path('register_tutor_1', views.RegisterTutor1View.as_view(), name = 'register_tutor_1'),
    path('register_tutor_3', views.RegisterTutor3View.as_view(), name = 'register_tutor_3'),
    path('register_tutor', views.RegisterTutorView.as_view(), name = 'register_tutor'),
    path('sorry_no_mins', views.SorryNoMinsView.as_view(), name = 'sorry_no_mins'),
    path('sorry_no_tutor', views.SorryNoTutorView.as_view(), name = 'sorry_no_tutor'),
    path('subscription_confirmation', views.SubscriptionConfirmationView.as_view(), name = 'subscription_confirmation'),
    path('terms_conditions_parents', views.TermsConditionsParentsView.as_view(), name = 'terms_conditions_parents'),
    path('terms_conditions_tutors', views.TermsConditionsTutorsView.as_view(), name = 'terms_conditions_tutors'),
    path('session_thank_you_tutor', views.SessionThankYouTutorView.as_view(), name = 'session_thank_you_tutor'),
    path('session_thank_you', views.SessionThankYouView.as_view(), name = 'session_thank_you'),
    path('tuto_details', views.TutoDetailsView.as_view(), name = 'tuto_details'),
    path('tutor_account', views.TutorAccountView.as_view(), name = 'tutor_account'),
    path('tutor_invoice_history', views.TutorInvoiceHistoryView.as_view(), name = 'tutor_invoice_history'),
    path('welcome', views.WelcomeView.as_view(), name = 'welcome'),
    path('forgot_login1', views.ForgotLogin1View.as_view(), name = 'forgot_login1'),
    path('forgot_login2', views.ForgotLogin2View.as_view(), name = 'forgot_login2'),
    path('payment_confirmation', views.PaymentConfirmationView.as_view(), name = 'payment_confirmation'),
    path('edit_tutor_info_1', views.EditTutorInfo1.as_view(), name = 'edit_tutor_info_1'),
    path('edit_tutor_info_2', views.EditTutorInfo2.as_view(), name = 'edit_tutor_info_2'),
    path('edit_tutor_info_3', views.EditTutorInfo3.as_view(), name = 'edit_tutor_info_3'),
    path('change_pass', views.ChangePass.as_view(), name = 'change_pass'),
    path('forgot_login_tutor1', views.ForgotLoginTutor1View.as_view(), name = 'forgot_login_tutor1'),
    path('forgot_login_tutor2', views.ForgotLoginTutor2View.as_view(), name = 'forgot_login_tutor2'),
    path('forgot_user1', views.ForgotUser1View.as_view(), name = 'forgot_user1'),
    path('forgot_user2', views.ForgotUser2View.as_view(), name = 'forgot_user2'),
    path('login_tutor', views.LoginTutorView.as_view(), name = 'login_tutor'),
    path('new_pass', views.NewPass.as_view(), name = 'new_pass'),
    path('subscription_confirmation_tutor', views.SubscriptionConfirmationTutorView.as_view(), name = 'subscription_confirmation_tutor'),














]
