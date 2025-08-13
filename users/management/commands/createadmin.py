from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create a superuser with the specified username and password'

    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            email = 'testadmin@test.com',
            first_name = 'Admin',
            last_name = 'Admin',
        )

        user.set_password('1234')

        user.is_superuser = True
        user.is_staff = True
        user.save()

        self.stdout.write(self.style.SUCCESS(f'Admin {user.email} created successfully!'))
