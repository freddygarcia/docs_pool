from Doc_Pool_Reservas import settings
from django import template

register = template.Library()

@register.filter
def show_pagination_numer(value, arg):
    return abs(value - arg) < settings.PAGINATOR_ITEM_NUMBER

@register.filter
def subtract(value, arg):
    return value - arg

@register.filter('get_value_from_dict')
def get_value_from_dict(dict_data, key):
    if key:
        return dict_data.get(key)

@register.filter('compare_area')
def compare_area(dict_filter, area):
    filtered_area = dict_filter.get('area')
    id_area = area.id

    if filtered_area:
        return int(filtered_area) == id_area

    return False
