from urllib.parse import urlparse, parse_qs, urlencode, urlunparse, quote
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def disabled_form(form):
    for field in form:
        field.field.widget.attrs["disabled"] = True
    return form.as_p()


@register.filter
def add_form_bulma_classes(html_content):
    html_content = html_content.replace("<p>", '<p class="block">')
    html_content = html_content.replace("<label", '<label class="label"')
    html_content = html_content.replace("<input", '<input class="input"')
    html_content = html_content.replace(
        '<span class="helptext', '<span class="helptext help'
    )
    return mark_safe(html_content)


@register.filter
def message_class(message_tags):
    return "is-" + message_tags.replace("error", "danger")


@register.filter
def qkey(url, key):
    """
    Adds a key with an empty value to the given URL.
    """
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    query_params[key] = [""]
    encoded_query = urlencode(query_params, doseq=True)
    return urlunparse(
        (
            parsed_url.scheme,
            parsed_url.netloc,
            parsed_url.path,
            parsed_url.params,
            encoded_query,
            parsed_url.fragment,
        )
    )


@register.filter
def qval(url, value):
    parsed_url = urlparse(url)
    if parsed_url.query.endswith("="):
        new_value = str(value)
        new_query = parsed_url.query + quote(new_value)
        return urlunparse(
            (
                parsed_url.scheme,
                parsed_url.netloc,
                parsed_url.path,
                parsed_url.params,
                new_query,
                parsed_url.fragment,
            )
        )
    else:
        return url
