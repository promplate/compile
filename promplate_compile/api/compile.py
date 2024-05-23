from pathlib import Path

from promplate import Template

from .._core import template_to_code


def compile_one(file: str | Path, *, encoding="utf-8"):
    Path(file).with_suffix(".py").write_text(template_to_code(Template.read(file, encoding=encoding)), encoding=encoding)


def compile_all(folder: str | Path, pattern="*[!.py]", *, encoding="utf-8"):
    for file in Path(folder).rglob(pattern):
        compile_one(file, encoding=encoding)
