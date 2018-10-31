.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

====================
collective.saml2auth
====================

Integración de saml2 para Plone 4.3, basado en el desarrollo de python-saml https://pythonhosted.org/python-saml/
La mayor parte del código está copiado de ftw.saml2auth, pero se ha eliminado la dependencia de ftw.upgrade 
y de otros paquetes que dificultan la instalación con setuptools.

El sitio plone actuará como un SP ante un IdP.

Features
--------

- Panel de control para definir la configuración.
- Plugin de usuario para la enumeración (IEnumerationPlugin) y los roles (IRolesPlugin)



Examples
--------

This add-on can be seen in action at the following sites:
- Is there a page on the internet where everybody can see the features?


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Translations
------------

This product has been translated into

- Klingon (thanks, K'Plai)


Installation
------------

Install collective.saml2auth by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.saml2auth


and then running ``bin/buildout``

Troubleshooting
---------------
En CentOS 6 y CentOS 7 existe un problema con dm.xmlsec.binding y xmlsec1-config de la
libreria xmlsec1-devel.
En caso de error ImportError: lxml.etree does not export expect C function adoptExternalDocument

1. Desinstala dm.xmlsec.binding ``pip uninstall dm.xmlsec.binding`` o elimina el egg de buildout-cache/eggs.

2. Aplica el parche
::
      --- /usr/bin/xmlsec1-config.orig    2015-02-25 13:47:13.384286257 +0100
      +++ /usr/bin/xmlsec1-config    2015-02-25 13:46:54.849285579 +0100
      @@ -199,7 +199,7 @@
      #
      # Assemble all the settings together
      #
      -the_flags="$the_flags  -D__XMLSEC_FUNCTION__=__FUNCTION__ -DXMLSEC_NO_GOST=1 -DXMLSEC_NO_XKMS=1 -DXMLSEC_DL_LIBLTDL=1 -I/usr/include/xmlsec1   $the_xml_flags $the_xslt_flags $the_crypto_flags"
      +the_flags="$the_flags  -D__XMLSEC_FUNCTION__=__FUNCTION__ -DXMLSEC_NO_GOST=1 -DXMLSEC_NO_XKMS=1 -DXMLSEC_DL_LIBLTDL=1 -DXMLSEC_NO_SIZE_T -I/usr/include/xmlsec1   $the_xml_flags $the_xslt_flags $the_crypto_flags"
      the_libs="$the_libs -L${package_libdir} -lxmlsec1 -lltdl  $the_xmlsec_crypto_lib -lxmlsec1 $the_xml_libs $the_xslt_libs       $the_crypto_libs" if $cflags; then::

3. Reinstala dm.xmlsec.binding, compilando de nuevo.

Contribute
----------

- Issue Tracker: https://github.com/collective/collective.saml2auth/issues
- Source Code: https://github.com/collective/collective.saml2auth
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
