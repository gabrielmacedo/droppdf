from django import template

register = template.Library()

@register.filter(name='format_utf8')
def format_utf8(value):
    try:
        return value.decode('utf8', 'replace')
        #return value.format('utf8')
    except:
        return value
