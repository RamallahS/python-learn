from django.contrib.auth.models import User


class AuthService:
    def register_user(self):
        User.objects.create_user('john', self.data["email"], self.data["password"])
