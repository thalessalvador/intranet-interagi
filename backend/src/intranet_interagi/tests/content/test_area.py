from intranet_interagi.content.area import Area
from plone import api
from plone.dexterity.fti import DexterityFTI
from zope.component import createObject
from zope.event import notify
from zope.lifecycleevent import ObjectModifiedEvent
import pytest


CONTENT_TYPE = "Area"


@pytest.fixture
def payload() -> dict:
    """Payload to create a new Area."""
    return {
        "type": CONTENT_TYPE,
        "title": "Secom",
        "description": "Também chamada ascom",
        "email": "secp,@plone.org",
        "ramal": "1975",
        "id": "alex-limi",
    }


class TestArea:
    @pytest.fixture(autouse=True)
    def _fti(self, get_fti, integration):
        self.fti = get_fti(CONTENT_TYPE)

    def test_fti(self):
        assert isinstance(self.fti, DexterityFTI)

    def test_factory(self):
        factory = self.fti.factory
        obj = createObject(factory)
        assert obj is not None
        assert isinstance(obj, Area)

    @pytest.mark.parametrize(
        "behavior",
        [
            "plone.namefromtitle",
            "plone.shortname",
            "plone.excludefromnavigation",
            "plone.versioning",
        ],
    )
    def test_has_behavior(self, get_behaviors, behavior):
        assert behavior in get_behaviors(CONTENT_TYPE)

    def test_create(self, portal, payload):
        with api.env.adopt_roles(["Manager"]):
            content = api.content.create(container=portal, **payload)
        assert content.portal_type == CONTENT_TYPE
        assert isinstance(content, Area)

    def test_review_state(self, portal, payload):
        with api.env.adopt_roles(["Manager"]):
            content = api.content.create(container=portal, **payload)
        assert api.content.get_state(content) == "internal"
        
    def test_subscriber_added_with_predio_value(self, portal):
        with api.env.adopt_roles(["Manager"]):
            area = api.content.create(
                container=portal,
                type=CONTENT_TYPE,
                title="Marketing",
                description="Área de Marketing",
                email="mktg@plone.org",
                predio="sede",
                ramal="2022",
            )
        assert area.excluded_from_nav is False

    def test_subscriber_added_without_predio_value(self, portal):
        with api.env.adopt_roles(["Manager"]):
            area = api.content.create(
                container=portal,
                type=CONTENT_TYPE,
                title="Marketing",
                description="Área de Marketing",
                email="mktg@plone.org",
                ramal="2022",
            )
        assert area.excluded_from_nav is True


    def test_subscriber_modified_with_predio_value(self, portal):
        with api.env.adopt_roles(["Manager"]):
            area = api.content.create(
                container=portal,
                type=CONTENT_TYPE,
                title="Marketing",
                description="Área de Marketing",
                email="mktg@plone.org",
                predio="sede",
                ramal="2022",
            )
            del area.predio;
            notify(ObjectModifiedEvent(area))
        assert area.excluded_from_nav is False

    def test_subscriber_modified_without_predio_value(self, portal):
        with api.env.adopt_roles(["Manager"]):
            area = api.content.create(
                container=portal,
                type=CONTENT_TYPE,
                title="Marketing",
                description="Área de Marketing",
                email="mktg@plone.org",
                ramal="2022",
            )
            area.predio = 'sede';
            notify(ObjectModifiedEvent(area))
        assert area.excluded_from_nav is True