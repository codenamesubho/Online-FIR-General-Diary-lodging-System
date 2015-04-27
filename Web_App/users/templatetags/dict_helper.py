from django import template
register = template.Library()
@register.filter(name='dict_get')
def dict_get(value, arg):
    #custom template tag used like so:
    #{{dictionary|dict_get:var}}
    #where dictionary is duh a dictionary and var is a variable representing
    #one of it's keys
    return value[arg]

@register.filter(name='get_val')
def get_val(value, arg):
	#custom template tag used like so:
    #{{dictionary|dict_get:var}}
    #where dictionary is duh a dictionary and var is a variable representing
    #one of it's keys
    try:
    	return value.__getattribute__(arg)
    except AttributeError:
    	return "None"

