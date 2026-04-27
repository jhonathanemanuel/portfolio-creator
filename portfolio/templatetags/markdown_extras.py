from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    if text:
        # Converte o texto para HTML
        html = markdown.markdown(text, extensions=['extra', 'codehilite', 'nl2br'])
        return mark_safe(html)
    return ""