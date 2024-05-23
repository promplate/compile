from pathlib import Path

from promplate import Template

from .._core import template_to_code


def compile_one(file: str | Path, *, encoding="utf-8"):
    target = Path(file).with_suffix(".py")
    source = template_to_code(Template.read(file, encoding=encoding))
    if target.is_file() and target.read_text(encoding=encoding) == source:
        return
    target.write_text(source, encoding=encoding)


def compile_all(folder: str | Path, pattern="*[!.py]", *, encoding="utf-8"):
    for file in Path(folder).rglob(pattern):
        compile_one(file, encoding=encoding)
