from bot.models import Telegram
from companies.models import Company
from django.contrib.auth.models import User
from django.db import models
from model_utils import Choices
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    OWNER = "OWNER"
    DRIVER = "DRIVER"
    DISPATCHER = "DISPATCHER"

    USER_TYPES = Choices(
        (OWNER, "Владелец"),
        (DRIVER, "Водитель"),
        (DISPATCHER, "Диспетчер"),
    )

    company = models.ForeignKey(Company, verbose_name="Компания", on_delete=models.PROTECT)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    user_type = models.CharField("Тип пользователя", choices=USER_TYPES, max_length=20)
    phone_number = PhoneNumberField("Телефонный номер")
    telegram = models.ForeignKey(Telegram, on_delete=models.PROTECT, help_text="Введите username или имя и фамилию указанную в телеграме", null=True, blank=True)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

        indexes = [
            models.Index(name="profile_user_type_idx", fields=["user_type"]),
            models.Index(name="profile_telegram_id_idx", fields=["telegram_id"]),
        ]

    def __str__(self):
        return f"{self.get_user_type_display()}-{self.company}"
