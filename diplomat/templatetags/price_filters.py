from django import template

register = template.Library()

@register.filter
def format_price(value):
    """
    Raqamni bo'sh joy bilan formatlaydi: 24000000 -> 24 000 000
    """
    try:
        value = int(value)
        return '{:,}'.format(value).replace(',', ' ')
    except (ValueError, TypeError):
        return value
