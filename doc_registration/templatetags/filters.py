from Doc_Pool_Reservas import settings
from django import template

register = template.Library()

@register.filter
def show_pagination_numer(value, arg):
	return abs(value - arg) < settings.PAGINATOR_ITEM_NUMBER

@register.filter
def subtract(value, arg):
	return value - arg
