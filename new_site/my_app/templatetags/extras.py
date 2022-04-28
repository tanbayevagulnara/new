from atexit import register
from django import template
from my_app.models import *

register = template.Library()

@register.simple_tag(name='getsteps')

def get_steps():
    return First.objects.all()



@register.inclusion_tag('my_app/list_steps.html')

def show_steps():
    steps = First.objects.all()
    return {'steps2': steps}


@register.simple_tag(name='showsteps')

def showsteps(filter=None):
    if not filter:
        return First.objects.all()
    else:
        return First.objects.filter(pk=filter)


@register.inclusion_tag('my_app/list_steps.html')

def show_steps_html(sort=None, step_selected=0):
    if not sort:
        steps = First.objects.all()
    else:
        steps = First.objects.order_by(sort)
    

    return {'steps': steps, 'step_selected': step_selected}