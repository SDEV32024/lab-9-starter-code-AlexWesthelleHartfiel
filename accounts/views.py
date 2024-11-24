from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import CustomUserCreationForm
from .models import Profile, CustomUser
from django.contrib.auth.models import Group

# Create your views here.

class CustomerSignUpView(CreateView):
model = CustomUser
form_class = CustomUserCreationForm
template_name = 'registration/signup.html'
success_url = reverse_lazy('login')
def form_valid(self, form):
# Save the new user
response = super().form_valid(form)
# Add user to the Customer group
customer_group, created =
Group.objects.get_or_create(name='Customer')
self.object.groups.add(customer_group)
return response # Redirect to success UR

class ManagerSignUpView(CreateView):
model = CustomUser
form_class = CustomUserCreationForm
template_name = 'registration/signup.html'
success_url = reverse_lazy('login')
def form_valid(self, form):
# Save the new user
response = super().form_valid(form)
# Add user to the Customer group
customer_group, created =
Group.objects.get_or_create(name='Manager')self.object.groups.add(customer_group)
return response # Redirect to success URL


class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ['date_of_birth','fav_author']

class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
