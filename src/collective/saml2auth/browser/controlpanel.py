# -*- coding: utf-8 -*-
from z3c.form import button
from z3c.form.group import GroupForm

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage

from plone.app.registry.browser.controlpanel import (
        RegistryEditForm, 
        ControlPanelFormWrapper,
        )

from collective.saml2auth import _
from collective.saml2auth.interfaces import IServiceProviderSettings


class SettingsEditForm(RegistryEditForm, GroupForm):
    schema = IServiceProviderSettings
    label = _('saml2auth_',
            default='Saml2Auth Settings Edit Form')

    @button.buttonAndHandler(_(u'Save'), name='save')
    def handleSave(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return

        self.applyChanges(data)

        IStatusMessage(self.request).addStatusMessage(
            _(u'Changes saved.'), "info")

        return self.request.response.redirect(self.request.getURL())

    @button.buttonAndHandler(_(u'Cancel'), name='cancel')
    def handleCancel(self, action):
        IStatusMessage(self.request).addStatusMessage(
            _(u'Changes canceled.'), "info")
        self.request.response.redirect("%s/%s" % (
                self.context.absolute_url(),
                self.control_panel_view),
            )

class Saml2AuthControlPanelView(ControlPanelFormWrapper):
    form = SettingsEditForm
    index = ViewPageTemplateFile('control_panel_layout.pt')
    title = _(u"Saml2Auth Settings")

    @property
    def title(self):
        return self.form.label()

    