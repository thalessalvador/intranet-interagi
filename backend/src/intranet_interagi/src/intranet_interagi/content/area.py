from intranet_interagi import _
from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel import model
from plone.supermodel.model import Schema
from zope import schema
from zope.interface import implementer

import re


def is_valid_email(value: str) -> bool:
    """Validar se o email é @plone.org."""
    return value.endswith("@plone.org") if value else True


def is_valid_extension(value: str) -> bool:
    """Validar se o o ramal tem 4 dígitos numéricos."""
    return re.match(r"^\d{4}$", value) if value else True


class IArea(Schema):
    """Uma Área."""

    model.fieldset(
        "default",
        _("Default"),
        fields=[
            "title",
            "description",
            "email",
            "ramal",
        ],
    )

    # Basic info
    title = schema.TextLine(title=_("Área"), required=True)
    description = schema.Text(title=_("Descrição"), required=False)
    email = Email(
        title=_("Email"),
        required=False,
        constraint=is_valid_email,
    )
    ramal = schema.TextLine(
        title=("Ramal"),
        required=False,
        constraint=is_valid_extension,
    )


@implementer(IArea)
class Area(Container):
    """Uma Área."""
