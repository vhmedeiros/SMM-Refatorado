from django import template
from django.template import engines, Context

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def render_template(template_string, context_vars):
    """
    Filtro para processar strings como mini-templates, substituindo {{ titulo }} e {{ link }}.

    Uso no template:
    Exemplo de entrada no campo 'Template Título Notícia':
    <li><a href="{{ link }}">{{ titulo }}</a></li>

    No template de email:
    {{ titulo_noticia_template|safe|render_template:"link, titulo" }}
    """
    try:
        context = Context()
        for var in context_vars.split(','):
            var = var.strip()
            context[var] = template.Variable(var).resolve(context)
        django_engine = engines['django']
        template_obj = django_engine.from_string(template_string)
        return template_obj.render(context)
    except Exception as e:
        return f"[Erro ao processar template: {e}]"
    
@register.filter
def replace_variables(template_str, context):
    """
    Substitui as variáveis {{ titulo }} e {{ link }} dentro de um campo HTML salvo no banco.
    """
    if not template_str:
        return ""

    result = template_str
    for key, value in context.items():
        placeholder = "{{ " + key + " }}"
        result = result.replace(placeholder, value)

    return result