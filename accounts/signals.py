# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import IntegrityError
from django.contrib.auth.models import User
from accounts.models import Avatar


@receiver(post_save, sender=User)
def asignar_avatar_predeterminado(sender, instance, created, **kwargs):
    print("Señal post_save recibida")
    try:
        if created:
            print(f"Nuevo usuario creado: {instance.username}")
            avatar_predeterminado = Avatar.objects.create(user=instance, imagen='avatares/avatar_default.png')
            avatar_predeterminado.save()
    except IntegrityError as e:
        print(f"Error al asignar avatar predeterminado: {e}")