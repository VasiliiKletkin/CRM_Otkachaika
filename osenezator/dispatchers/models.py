from django.contrib.auth import get_user_model

user_model = get_user_model()


class Dispatcher(user_model):
    class Meta:
        proxy = True
        verbose_name = "Dispatcher"
        verbose_name_plural = "Dispatchers"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"