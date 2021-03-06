from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Zespol(models.Model):
    nazwa = models.CharField(max_length=100, blank=False)
    ilosc_czlonkow = models.PositiveIntegerField()
    min_kwota_zlecenia = models.PositiveIntegerField()
    manager = models.CharField(max_length=1, choices=[
        ('P', "% wynagrodzenia"),
        ('S', "stawka [zł]"),
        ('C', "jako członek zespolu"),
        ('N', "Nie")], default='N')
    booker = models.CharField(max_length=1, choices=[
        ('P', "% wynagrodzenia"),
        ('S', "stawka [zł]"),
        ('C', "jako członek zespolu"),
        ('N', "Nie")], default='N')
    fundusz = models.CharField(max_length=1, choices=[
        ('P', "% z wynagrodzenia"),
        ('S', "określona stawka [zł]"),
        ('C', "jako członek zespolu"),
        ('N', "Nie")], default='N')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'zespoły'

    def __str__(self):
        return f"{self.nazwa}"


    def get_absolute_url(self):
        return reverse('muzyk:zespol-lista')


class Samochod(models.Model):
    zespol = models.ForeignKey(Zespol,
                               on_delete=models.CASCADE,
                               related_name='samochody')
    nazwa = models.CharField(max_length=50, help_text='', blank=False)
    BENZYNA = 'B'
    DIESEL = 'D'
    LPG = 'G'
    PALIWO = (
        (BENZYNA, 'benzyna'),
        (DIESEL, 'diesel'),
        (LPG, 'gaz')
    )
    paliwo = models.CharField(max_length=1, choices=PALIWO, default=BENZYNA)
    ile_litrow_pali_na_100_km = models.DecimalField(max_digits=4, decimal_places=2, blank=False)
    autor = models.ForeignKey(User,
                              on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'samochody'

    def __str__(self):
        return f"{self.nazwa}"

    def get_absolute_url(self):
        return reverse('muzyk:samochod-lista')


class AnalizaLubWycenaOferty(models.Model):
    oferta = models.DecimalField(max_digits=10, decimal_places=2, blank=False, help_text="Kwota w zł.")
    podatek = models.DecimalField(max_digits=3, decimal_places=1, blank=False, help_text="Jeśli oferta to kwota netto to wpisz tutaj 0.")
    odleglosc = models.DecimalField(max_digits=5, decimal_places=2, blank=False, help_text="Odległość w km.")
    ilosc_aut = models.SmallIntegerField()
    srednie_spalanie = models.DecimalField(max_digits=4, decimal_places=2, blank=False, help_text="Spalanie w L/100km")
    srednia_cena_paliwa = models.DecimalField(max_digits=3, decimal_places=2, help_text="Cena w zł.")
    koszt_noclegu = models.DecimalField(max_digits=7, decimal_places=2, help_text="Cena w zł.")
    dodatkowe_koszty = models.DecimalField(max_digits=8, decimal_places=2)