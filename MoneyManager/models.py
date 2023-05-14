from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class movimenti(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data = models.DateField()
    nome_icona = models.CharField(max_length=255)
    tipologia = models.CharField(max_length=2)
    cifra = models.FloatField()
    descrizione = models.CharField(max_length=255)



    def __unicode__(self):
        return self.user_id.id
