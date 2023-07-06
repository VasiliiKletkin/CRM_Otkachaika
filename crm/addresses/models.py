from django.db import models

class Address(models.Model):
    title = models.CharField("Полное название адреса", max_length=500)
    uid = models.CharField("Уникальный номер адреса", max_length=100, unique=True)
    
    country = models.CharField("Страна", max_length=120, null= True, blank=True)
    country_iso_code = models.CharField("ISO-код страны", max_length=2, null= True, blank=True)
    
    region_fias_id = models.CharField("ФИАС-код региона", max_length=36, null= True, blank=True)
    region_with_type= models.CharField("Регион с типом", max_length=131, null= True, blank=True)
    region_type= models.CharField("Тип региона (сокращенный)", max_length=10, null= True, blank=True)
    region_type_full= models.CharField("Тип региона ", max_length=50, null= True, blank=True)
    region= models.CharField("Регион", max_length=120, null= True, blank=True)

    city_fias_id= models.CharField("ФИАС-код города", max_length=36, null= True, blank=True)
    city_with_type= models.CharField("Город с типом", max_length=131, null= True, blank=True)
    city_type= models.CharField("Тип города (сокращенный)", max_length=10, null= True, blank=True)
    city_type_full= models.CharField("Тип города", max_length=50, null= True, blank=True)
    city= models.CharField("Город", max_length=120, null= True, blank=True)
    
    street_fias_id= models.CharField("ФИАС-код улицы", max_length=36, null= True, blank=True)
    street_with_type= models.CharField("Улица с типом", max_length=131, null= True, blank=True)
    street_type= models.CharField("Тип улицы (сокращенный)", max_length=10, null= True, blank=True)
    street_type_full= models.CharField("Тип улицы", max_length=50, null= True, blank=True)
    street= models.CharField("Улица", max_length=120, null= True, blank=True)
    
    # geo_lat": "55.821168",
    # geo_lon": "37.82608",


    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"
        indexes = [
            models.Index(name="address_uid_idx", fields=["uid"]),
        ]

    def __str__(self):
        return f"{self.title}"
