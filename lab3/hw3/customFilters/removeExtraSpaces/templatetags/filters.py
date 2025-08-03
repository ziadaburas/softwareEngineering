from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='removeExtraSpacesFilter')
def removeExtraSpacesFilter(value):
    return ' '.join(value.split())

@register.filter(name='evenOrOdd')
def evenOrOdd(value):
    return 'Even' if value % 2 == 0 else 'Odd'


@register.filter(name='renderJson')
def renderJson(value): 
    html = ""
    if isinstance(value,dict):
        html += "<ul>"
        for key,val in value.items():
            html += "<li>"
            if not isinstance(val, (dict, list)):
                html += f'<h3 style="display:inline">{key}</h3> : <p style="display:inline">{val}</p>'
            else:
                html += f'<h3>{key}:</h3>'
                html += renderJson(val)
            html += "</li>"
        html += "</ul>"

    elif isinstance(value, list):
        html += "<ol>"
        for item in value:
            html += "<li>"
            html += renderJson(item)
            html += "</li>"
        html += "</ol>"

    else:
        html += f"<p>{value}</p>"

    return mark_safe(html)