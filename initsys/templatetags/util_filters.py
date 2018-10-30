from django import template
from django.template.defaultfilters import stringfilter
from random import randint

from initsys.models import Setting

register = template.Library()


@register.filter
@stringfilter
def summary(text):
    number_of_words = 25
    if len(text.split(" ")) > number_of_words:
        return " ".join(text.split(" ")[: number_of_words]) + "..."
    return text


@register.filter
@stringfilter
def as_paragraph(text):
    pars = []
    for p in text.split('\n'):
        if "" != p.strip():
            pars.append('<p>{}</p>'.format(p.strip()))
    return "".join(pars)


@register.filter
def random_num(num_ini, num_fin):
    return "{:3d}".format(randint(num_ini, num_fin))


@register.filter
def money2display(num):
    return "{:0,.2f}".format(num)


@register.filter
@stringfilter
def get_setting(sectionvalue):
    """
    Obtiene el valor de un setting

    (string) sectionvalue   Setting a obtener en formato section.value

    return string
    """
    section, value = sectionvalue.split(".")
    return Setting.get_value(section, value)
