from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from users.forms import CustomUserCreationForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('library:books_list')
    success_message = 'Пользователь успешно зарегистрирован'
