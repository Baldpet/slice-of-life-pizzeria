from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Offer


@receiver(pre_save, sender=Offer)
def update_pre_save(sender, instance, **kwargs):
    """
    Update the original cost of an offer
    Update the potential savings from the offer
    """
    instance.original_price_calculation()
    instance.calculate_saving()
