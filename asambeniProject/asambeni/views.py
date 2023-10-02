# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import CustomUser, Learner
from .forms import DriverRegistrationForm, LearnerRegistrationForm

## -_-_ Stripe key
# stripe.api_key = settings.STRIPE_SECRET_KEY

## -_-_ Index
def index(request):
    asambeniUsers = CustomUser.objects.all()

    # Check if user is logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to the appropriate dashboard based on user type
            if user.is_superuser:
                return redirect('admin')

            user_type = getattr(user.asambeniUser, 'user_type', None) if hasattr(user, 'asambeniUser') else None

            if user_type == 'driver':
                return redirect('driver')
            elif user_type == 'Learner':
                return redirect('learner')

            messages.success(request, 'Logged in! Welcome back.')
            return redirect('index')
        else:
            messages.success(request, 'Invalid username or password. Please try again.')
            return redirect('index')
    return render(request, 'index.html', {})

# def signUp(request):
#     registered = False
#     if request.method == 'POST':
#         user_type = request.POST.get('user_type')

#         if user_type == 'driver':
#             form = DriverRegistrationForm(data=request.POST)

#         elif user_type == 'learner':
#             form = LearnerRegistrationForm(data=request.POST)

#         if form.is_valid():
#             user = form.save()
#             messages.success(request, 'Registration successful. You can now log in.')
#             return redirect('index')

#     else:
#         form = DriverRegistrationForm()

#     context = {
#         'form' : form,
#         'registered' : registered,
#     }
#     return render(request, 'signUp.html', context)

## -_-_ SignUp & Logout
## -_-_ Multi User Auth
## -_-_ Learner Redirect
def LearnerSignUpView(request):
    if request.method == 'POST':
        model = CustomUser
        learner_form = LearnerRegistrationForm(request.POST)
        if learner_form.is_valid():
            user = learner_form.save()
            my_driver = learner_form.cleaned_data['my_driver']

            if my_driver:
                learner = Learner.objects.create(user=user, my_driver=my_driver)
            login(request, user)
            return redirect('learner')
    else:
        learner_form = LearnerRegistrationForm()
    context = {
        'learner_form' : learner_form
    }
    return render(request, 'learner_signup.html', context)
## -_-_ Driver Redirect
class DriverSignUpView(CreateView):
    model = CustomUser
    form_class = DriverRegistrationForm
    template_name = 'driver_signup.html'

    def form_valid(self, form):
        user = form.user()
        login(self.request, user)
        return redirect('driver')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('index')

## -_-_ Admin Dash Features
@login_required
def admin_dash(request):
    return render(request, 'panels/admin.html')
# @login_required
# def user_mgnt(request):
#     return render(request, 'panels/admin/user.html')
# @login_required
# def driver_mgnt(request):
#     return render(request, 'panels/admin/driver.html')

## -_-_ Student Dash Features
@login_required
def learner_dash(request):
    user = request.user
    return render(request, 'panels/learner_dashboard.html', {'user': user})

# @login_required
# def edit_profile(request):
#     user = request.user
#     if request.method == 'POST':
#         form = UserChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             user.first_name = request.POST['first_name']
#             user.last_name = request.POST['last_name']
#             user.email = request.POST['email']
#             form.save()
#             user.save()
#             return redirect('profile')
#     else:
#         form = UserChangeForm(instance=request.user)
#         return render(request, 'edit_profile.html', {'user': user})

# @login_required
# class PaymentView(TemplateView):
#     template_name = 'payment.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY
#         return context

#     def post(self, request, *args, **kwargs):
#         token = request.POST.get('stripeToken')
#         amount = 1000  # Amount in cents

#         try:
#             charge = stripe.Charge.create(
#                 amount=amount,
#                 currency='usd',
#                 source=token,
#                 description='Payment for Services'
#             )
#             # Handle successful payment
#             return redirect('payment_success')
#         except stripe.error.CardError as e:
#             # Handle card error
#             error_message = e.error.message
#             return render(request, 'payment.html', {'error_message': error_message})
#         except stripe.error.StripeError:
#             # Handle other Stripe errors
#             error_message = 'An error occurred during payment. Please try again later.'
#             return render(request, 'payment.html', {'error_message': error_message})

# @login_required
# def chat_too(request):
#     return render(request, '')
# @login_required
# def track_me(request):
#     return render(request, '')

# ## -_-_ Driver Dash Features
@login_required
def driver_dash(request):
    return render(request, 'panels/driver_dashboard.html')

## -_-_ App Pages
def aboutUs(request):
    return render(request, 'about.html')