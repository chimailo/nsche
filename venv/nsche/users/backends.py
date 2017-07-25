from __future__ import unicode_literals
from django.contrib.auth.backends import ModelBackend as MyModelBackend
from django.contrib.auth import get_user_model


class CustomUserAuth(MyModelBackend):
    """
    Authenticates against settings.AUTH_USER_MODEL.
    """

    def authenticate(self, matric_no=None, password=None, **kwargs):
        UserModel = get_user_model()
        # if email is None:
        #     email = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = UserModel._default_manager.get_by_natural_key(matric_no)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            UserModel().set_password(password)

	