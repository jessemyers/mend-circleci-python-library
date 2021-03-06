from typing import Iterable, Type

from click import Option, Parameter
from jinja2 import PackageLoader

from mend.generators.template import TemplateGenerator


class CircleCIGenerator(TemplateGenerator):
    """
    Generate CircleCI configuration for a Python library.

    """
    @classmethod
    def iter_parameters(cls: Type["TemplateGenerator"]) -> Iterable[Parameter]:
        yield Option(
            [
                "--project",
            ],
            required=True,
        )
        yield Option(
            [
                "--image",
            ],
            default="cimg/python:3.9.6",
        )

    @classmethod
    def from_parameters(
            cls: Type["TemplateGenerator"],
            *args,
            **kwargs,
    ) -> "TemplateGenerator":
        return cls(
            loader=PackageLoader("mend_circleci_python_library", "templates"),
            context=kwargs,
        )
