from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL


class Dashboard(models.Model):
    user = models.OneToOneField(User)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message=
                                 "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    country = (('Nigeria', 'Nigeria'),)
    bank_region = models.CharField(choices=country, max_length=10, default='nigeria')
    bank_account_number = models.CharField(max_length=10)
    banks = (
        ('Access Bank', 'Access Bank'),
        ('Citibank', 'Citibank'),
        ('Diamond Bank', 'Diamond Bank'),
        ('Ecobank', 'Ecobank'),
        ('Fidelity Bank', 'Fidelity Bank'),
        ('First Bank of Nigeria', 'First Bank of Nigeria'),
        ('First City Monument Bank', 'First City Monument Bank'),
        ('Guaranty Trust Bank', 'Guaranty Trust Bank'),
        ('Heritage Bank plc', 'Heritage Bank plc'),
        ('Keystone Bank Limited', 'Skye Bank'),
        ('Stanbic IBTC', 'Stanbic IBTC'),
        ('Standard Chartered Bank', 'Standard Chartered Bank'),
        ('Sterling Bank', 'Sterling Bank'),
        ('Union Bank', 'Union Bank'),
        ('United Bank for Africa', 'United Bank for Africa'),
        ('Unity Bank plc', 'Unity Bank plc'),
        ('Wema Bank', 'Wema Bank'),
        ('Zenith Bank', 'Zenith Bankk'),
    )
    bank = models.CharField(max_length=50, default='Guaranty Trust Bank', choices=banks)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class SbdSellOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sbd = models.DecimalField(max_digits=10, decimal_places=3)
    sbd_ngn = models.DecimalField(max_digits=10, decimal_places=2)
    sbd_usd = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        Dashboard.objects.get_or_create(user=instance)

post_save.connect(post_save_user_receiver, sender=User)
