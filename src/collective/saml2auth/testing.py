# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.saml2auth

from zope.configuration import xmlconfig
from collective.saml2auth.plugin import SAML2Plugin


class CollectiveSaml2authLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.saml2auth
        xmlconfig.file('configure.zcml',
                       collective.saml2auth,
                       context=configurationContext)
        z2.installProduct(app, 'collective.saml2auth')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.saml2auth:default')

        # Setup PAS plugin
        uf = portal.acl_users
        plugin = SAML2Plugin('saml2')
        uf._setObject(plugin.getId(), plugin)
        plugin = uf['saml2']
        plugin.manage_activateInterfaces([
            'IRolesPlugin',
            'IUserEnumerationPlugin',
        ])


COLLECTIVE_SAML2AUTH_FIXTURE = CollectiveSaml2authLayer()
COLLECTIVE_SAML2AUTH_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_SAML2AUTH_FIXTURE,), name="collective.saml2auth:Integration")
COLLECTIVE_SAML2AUTH_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_SAML2AUTH_FIXTURE,), name="collective.saml2auth:Functional")


class CollectiveSaml2AuthLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        self.loadZCML(package=collective.saml2auth)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.saml2auth:default')


COLLECTIVE_SAML2AUTH_FIXTURE = CollectiveSaml2AuthLayer()


COLLECTIVE_SAML2AUTH_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_SAML2AUTH_FIXTURE,),
    name='CollectiveSaml2AuthLayer:IntegrationTesting',
)


COLLECTIVE_SAML2AUTH_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_SAML2AUTH_FIXTURE,),
    name='CollectiveSaml2AuthLayer:FunctionalTesting',
)


COLLECTIVE_SAML2AUTH_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_SAML2AUTH_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectiveSaml2AuthLayer:AcceptanceTesting',
)
