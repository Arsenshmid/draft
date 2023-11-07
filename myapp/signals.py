from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission

@receiver(post_save, sender=User)
def add_view_tour_permission(sender, instance, created, **kwargs):
    if created:
        view_tour_permission = Permission.objects.get(codename='view_tour')
        instance.user_permissions.add(view_tour_permission)
