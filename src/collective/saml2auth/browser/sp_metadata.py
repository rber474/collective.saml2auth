# -*- coding: utf-8 -*-
from collective.saml2auth.interfaces import IAuthNRequestStorage
from collective.saml2auth.interfaces import IServiceProviderSettings
from collective.saml2auth.settings import saml2_settings
from onelogin.saml2.authn_request import OneLogin_Saml2_Authn_Request
from plone import api
from plone.memoize.instance import memoize
from plone.registry.interfaces import IRegistry
from Products.Five import BrowserView
from zope.component import queryUtility
import urllib

class MetadataView(BrowserView):
    """ SP Metadata endpoint """
    def __init__(self, context, request):
        super(MetadataView, self).__init__(context, request)

    def __call__(self):

        settings = saml2_settings()
        metadata = settings.get_sp_metadata()
        errors = settings.validate_metadata(metadata)
        resp = self.request.response

        if len(errors) == 0:
            resp.setStatus(200)
            resp.setBody(metadata)
            resp.setHeader('Content-Type', 'text/plain')
        else:
            resp.setStatus(500, lock=1)
            resp.setBody(', '.join(errors), lock=1)

        return resp