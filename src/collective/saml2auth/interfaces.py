# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from zope.interface import Interface
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from collective.saml2auth import _

dig_algorithm = SimpleVocabulary([
    SimpleTerm(
        value=u'http://www.w3.org/2000/09/xmldsig#sha1',
        title=u'SHA1'),
    SimpleTerm(
        value=u'http://www.w3.org/2001/04/xmlenc#sha256',
        title=u'SHA256'),
    SimpleTerm(
        value=u'http://www.w3.org/2001/04/xmldsig-more#sha384',
        title=u'SHA384'),
    SimpleTerm(
        value=u'http://www.w3.org/2001/04/xmlenc#sha512',
        title=u'SHA512'),
])

sig_algorithm = SimpleVocabulary([
    SimpleTerm(
        value=u'http://www.w3.org/2000/09/xmldsig#dsa-sha1',
        title=u'DSA_SHA1'),
    SimpleTerm(
        value=u'http://www.w3.org/2000/09/xmldsig#rsa-sha1',
        title=u'RSA_SHA1'),
    SimpleTerm(
        value=u'http://www.w3.org/2001/04/xmldsig-more#rsa-sha256',
        title=u'RSA_SHA256'),
    SimpleTerm(
        value=u'http://www.w3.org/2001/04/xmldsig-more#rsa-sha384',
        title=u'RSA_SHA384'),
    SimpleTerm(
        value=u'http://www.w3.org/2001/04/xmldsig-more#rsa-sha512',
        title=u'RSA_SHA512'),
])

authn_bindings = SimpleVocabulary([
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST',
        title=u'HTTP-POST'),
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect',
        title=u'HTTP-Redirect'),
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact',
        title=u'HTTP-Artifact'),
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:2.0:bindings:SOAP',
        title=u'SOAP'),
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:2.0:bindings:URL-Encoding:DEFLATE',
        title=u'DEFLATE'),
])

authn_context_classes = SimpleVocabulary([
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:2.0:ac:classes:unspecified',
        title=u'Unspecified'),
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport',
        title=u'Password Protected Transport'),
    SimpleTerm(
        value=u'urn:federation:authentication:windows',
        title=u'Integrated Windows Authentication'),
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:2.0:ac:classes:Kerberos',
        title=u'Kerberos'),
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:2.0:ac:classes:X509',
        title=u'X509'),
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:2.0:ac:classes:Password',
        title=u'Password'),
])


authn_context_comparison_methods = SimpleVocabulary([
    SimpleTerm(
        value=u'exact',
        title=u'Exact'),
    SimpleTerm(
        value=u'minimum',
        title=u'Minimum'),
    SimpleTerm(
        value=u'maximum',
        title=u'Maximum'),
    SimpleTerm(
        value=u'better',
        title=u'Better'),
])

nameid_formats = SimpleVocabulary([
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified',
        title=u'Unspecified'),
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress',
        title=u'E-Mail'),
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:2.0:nameid-format:persistent',
        title=u'Persistent'),
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:2.0:nameid-format:transient',
        title=u'Transient'),
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName',
        title=u'509SubjectName'),
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName',
        title=u'WindowsDomainQualifiedName'),
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:2.0:nameid-format:kerberos',
        title=u'Kerberos'),
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:2.0:nameid-format:entity',
        title=u'Entity'),
    SimpleTerm(
        value=u'urn:oasis:names:tc:SAML:2.0:nameid-format:encrypted',
        title=u'encrypted'),

])

class IServiceProviderSettings(Interface):

    enabled = schema.Bool(
        title=u'Enable',
        description=u'Enables SAML 2.0 Service Provider role for this Plone site',
        default=False,
    )

    idp_issuer_id = schema.TextLine(
        title=u'IdP Issuer Id',
        description=u'Identifier of the IdP which will issue SAML assertions',
        default=u'',
    )

    idp_sso_binding = schema.Choice(
        title=u'IdP SingleSignOnService Binding',
        vocabulary=authn_bindings,
        default=u'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect',
    )

    idp_url = schema.TextLine(
        title=u'IdP URL',
        description=u'URL of the IdP endpoint where AuthnRequests are send to.',
        default=u'',
    )

    sp_issuer_id = schema.TextLine(
        title=u'SP Issuer ID',
        description=u'Unique identifier of the service provider',
        default=u'',
    )

    sp_acs_binding = schema.Choice(
        title=u'SP assertionConsumerService Binding',
        vocabulary=authn_bindings,
        default=u'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST',
    )
    
    authn_context = schema.List(
        title=u'AuthN Context',
        value_type=schema.Choice(vocabulary=authn_context_classes),
        default=[
            u'urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport',
            u'urn:federation:authentication:windows',
            u'urn:oasis:names:tc:SAML:2.0:ac:classes:Kerberos',
        ],
        required=False,
    )

    authn_context_comparison = schema.Choice(
        title=u'AuthN Context Comparison',
        vocabulary=authn_context_comparison_methods,
        default=u'exact',
    )

    signature_algorithm  = schema.Choice(
        title=u'Signature Algorithm',
        vocabulary=sig_algorithm,
        default=u'http://www.w3.org/2001/04/xmldsig-more#rsa-sha256',
    )

    digest_algorithm  = schema.Choice(
        title=u'Digest Algorithm',
        vocabulary=dig_algorithm,
        default=u'http://www.w3.org/2001/04/xmlenc#sha256',
    )

    nameid_format = schema.Choice(
        title=u'NameID Format',
        vocabulary=nameid_formats,
        default=u'urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified',
    )

    sign_authnrequest = schema.Bool(
        title=u'Sign AuthNRequest',
        description=u'Enable signing of AuthNRequests',
        default=False,
    )

    signing_key = schema.Text(
        title=u'Signing Key',
        description=u'The private key used for signing AuthNRequests',
        required=False,
    )

    signing_cert = schema.Text(
        title=u'Signing Certificate',
        description=u'The certificate for verifying signatures in '
                    'AuthNRequests',
        required=False,
    )

    idp_cert = schema.Text(
        title=u'IdP Certificate',
        description=u'The certificate of the IdP to verify signatures in SAML '
                    'assertions.',
    )

    max_clock_skew = schema.Int(
        title=u'Max. Clock Skew',
        description=u'The maximum acceptable clock skew in seconds.',
        default=60,
    )

    autoprovision_users = schema.Bool(
        title=u'Autoprovision Users',
        description=u"If enabled, users will be created if they don't exist",
        default=False,
    )

    store_requests = schema.Bool(
        title=u'Store Requests',
        description=u"If enabled, the id of an AuthNRequest is stored and "
                    "verified when processing a response.",
        default=False,
    )

    update_user_properties = schema.Bool(
        title=u'Update User Properties',
        description=u"If enabled, the user's properties are updated with the "
                    "attributes contained in the SAML assertion.",
        default=True,
    )

    internal_network = schema.Tuple(
        title=u'Subnets or ip-addresses from the internal network',
        description=u'Defines subnets (192.0.2.0/24) or ip-addresses (192.0.2.1) '
                    u'to define your internal netzwork. A user accessing the '
                    u'Plone Site from an internal network will be auto-logged-in. '
                    u'Write each subnet/ip-address on a separate line.',
        value_type=schema.TextLine(),
        default=(),
        missing_value=(),
        required=False,
    )


class ICollectiveSaml2AuthLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""



class IAuthNRequestStorage(Interface):
    """Storage for issued AuthNRequest IDs"""
