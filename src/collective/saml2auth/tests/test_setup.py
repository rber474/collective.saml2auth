# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from collective.saml2auth.testing import COLLECTIVE_SAML2AUTH_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.saml2auth is properly installed."""

    layer = COLLECTIVE_SAML2AUTH_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.saml2auth is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.saml2auth'))

    def test_browserlayer(self):
        """Test that ICollectiveSaml2AuthLayer is registered."""
        from collective.saml2auth.interfaces import (
            ICollectiveSaml2AuthLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveSaml2AuthLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_SAML2AUTH_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['collective.saml2auth'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.saml2auth is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.saml2auth'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveSaml2AuthLayer is removed."""
        from collective.saml2auth.interfaces import \
            ICollectiveSaml2AuthLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ICollectiveSaml2AuthLayer,
            utils.registered_layers())
