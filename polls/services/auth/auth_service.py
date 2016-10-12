from django.contrib.auth.models import User

class AuthService:
    def register_user(self):
        user = User.objects.create_user('john', self.data["email"], self.data["password"])
        print(user);
        return True
