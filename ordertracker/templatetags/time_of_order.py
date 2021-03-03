from django import template
from datetime import datetime, timezone

register = template.Library()


@register.filter(name='calc_order_time')
def calc_order_time(order_time):
    current_time = datetime.now(timezone.utc)
    time_passed = current_time - order_time
    minutes = round(time_passed.total_seconds() / 60)
    return minutes
