from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from users.forms import CustomUserCreationForm
from django.core.mail import send_mail

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('library:books_list')
    success_message = 'Пользователь успешно зарегистрирован'

    def form_valid(self, form):
        """
        Метод, который вызывается при успешной валидации формы.
        """
        user = form.save()
        self.send_welcome_email(user.email, user.username)
        return super().form_valid(form)

    def send_welcome_email(self, user_email, username):
        """
        Метод отправки приветственного письма
        """
        subject = f'Добро пожаловать в наш сервис {username}!'
        message = 'Спасибо за регистрацию!'
        from_email = 'project.autoemail@gmail.com'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)