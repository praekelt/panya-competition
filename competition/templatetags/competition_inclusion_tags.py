from django import template

register = template.Library()

@register.inclusion_tag('competition/inclusion_tags/competition_listing.html')
def competition_listing(object_list):
    return {'object_list': object_list}

@register.inclusion_tag('competition/inclusion_tags/competition_detail.html')
def competition_detail(obj):
    return {'object': obj}
