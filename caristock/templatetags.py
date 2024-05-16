from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def add_form_bulma_classes(html_content):
    html_content = html_content.replace("<p>", '<p class="block">')
    html_content = html_content.replace("<label", '<label class="label"')
    html_content = html_content.replace("<input", '<input class="input"')
    html_content = html_content.replace(
        '<span class="helptext', '<span class="helptext help'
    )
    return mark_safe(html_content)
