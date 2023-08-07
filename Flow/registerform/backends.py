from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
            print("EmailBackend - Found user:", user)
            if user.check_password(password):
                print("EmailBackend - Password is correct.")
                return user
            else:
                print("EmailBackend - Incorrect password.")
        except UserModel.DoesNotExist:
            print("EmailBackend - User not found.")
            return None

