"""Portal settings tests."""
from plone import api


class TestPortalSettings:
    """Test that Portal configuration is correctly done."""

    def test_portal_title(self, portal):
        """Test portal title."""
        value = api.portal.get_registry_record("plone.site_title")
        expected = "Intranet Interagi"
        assert value == expected
    
    def test_portal_timezone(self, portal):
        """Test portal timezone."""
        value = api.portal.get_registry_record("plone.portal_timezone")
        expected = "America/Sao_Paulo"
        assert value == expected

    def test_portal_sitemap(self, portal):
        """Test portal sitemap."""
        value = api.portal.get_registry_record("plone.enable_sitemap")
        assert value is True

    def test_portal_twitter(self, portal):
        """Test portal twitter."""
        value = api.portal.get_registry_record("plone.twitter_username")
        expected = "thalessalvador"
        assert value == expected

    def test_portal_language(self, portal):
        """Test portal language."""
        value = api.portal.get_registry_record("plone.default_language")
        expected = "pt-br"
        assert value == expected

    def test_portal_smtp_host(self, portal):
        """Test portal smtp_host."""
        value = api.portal.get_registry_record("plone.smtp_host")
        expected = "localhost"
        assert value == expected