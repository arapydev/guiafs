import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Sets the password for the admin user from an environment variable.'

    def handle(self, *args, **options):
        User = get_user_model()
        password = os.environ.get('ADMIN_PASSWORD')
        if not password:
            self.stdout.write(self.style.ERROR('ADMIN_PASSWORD environment variable not set.'))
            return

        try:
            admin = User.objects.get(username='admin')
            admin.set_password(password)
            admin.save()
            self.stdout.write(self.style.SUCCESS("Successfully set password for 'admin' user."))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("User 'admin' does not exist. Please create it first."))

            