from pathlib import Path

from promplate.prompt.template import Template, TemplateCore

meta_template = Template.read(Path(__file__) / "../template.j2")


def template_to_code(template: TemplateCore):
    return meta_template.render({"template": template})
