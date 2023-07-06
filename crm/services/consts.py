from model_utils import Choices

ONE_MONTH = "30"
THREE_MONTHS = "90"
SIX_MONTHS = "180"
TWELVE_MONTHS = "360"

PERIOD = Choices(
    (ONE_MONTH, "1 Месяц"),
    (THREE_MONTHS, "3 Месяца"),
    (SIX_MONTHS, "6 Месяцев"),
    (TWELVE_MONTHS, "12 Месяцев"),
)

