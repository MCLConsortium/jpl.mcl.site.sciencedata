This package provides knowledge content types and RDF ingestion for the
Molecular and Cellular Characterization of Screen-Detected Lesions.


Functional Tests
================

To demonstrate the code, we'll classes in a series of functional tests.  And
to do so, we'll need a test browser::

    >>> app = layer['app']
    >>> from plone.testing.z2 import Browser
    >>> from plone.app.testing import SITE_OWNER_NAME, SITE_OWNER_PASSWORD
    >>> browser = Browser(app)
    >>> browser.handleErrors = False
    >>> browser.addHeader('Authorization', 'Basic %s:%s' % (SITE_OWNER_NAME, SITE_OWNER_PASSWORD))
    >>> portal = layer['portal']    
    >>> portalURL = portal.absolute_url()

Here we go.


Labcas Collections
=======

A labcascollection is an academic rank conferred by a college or university after
examination or after completion of a course of study, or conferred as an honor
on a distinguished person.  They go in Labcas Collection Folders, which can be added
anywhere:

    >>> browser.open(portalURL)
    >>> l = browser.getLink(id='jpl-mcl-site-knowledge-labcascollectionfolder')
    >>> l.url.endswith('++add++jpl.mcl.site.knowledge.labcascollectionfolder')
    True
    >>> l.click()
    >>> browser.getControl(name='form.widgets.title').value = u'My Labcas Collection Folder'
    >>> browser.getControl(name='form.widgets.description').value = u'Some of my favorite labcascollections.'
    >>> browser.getControl(name='form.widgets.url').value = u'testscheme://localhost/rdf/labcascollections1'
    >>> browser.getControl(name='form.widgets.ingestEnabled:list').value = False
    >>> browser.getControl(name='form.buttons.save').click()
    >>> 'my-labcascollection-folder' in portal.keys()
    True

The folder is currently empty::

    >>> folder = portal['my-labcascollection-folder']
    >>> len(folder.keys())
    0

Note that we've set ``ingestEnabled`` to ``False``.  So if we try to ingest
that folder, nothing will happen.  How do we start the ingest process?  By
visiting a view at the root of the site::

    >>> from plone.registry.interfaces import IRegistry
    >>> from zope.component import getUtility
    >>> registry = getUtility(IRegistry)
    >>> registry['jpl.mcl.site.knowledge.interfaces.ISettings.objects'] = [u'my-labcascollection-folder']
    >>> import transaction
    >>> transaction.commit()
    >>> browser.open(portalURL + '/@@ingestContent')

But since the labcascollection folder had ingest disabled, it's still empty::

    >>> len(folder.keys())
    0

So let's enable ingest and try again::

    >>> browser.open(portalURL + '/my-labcascollection-folder/@@edit')    
    >>> browser.getControl(name='form.widgets.ingestEnabled:list').value = True
    >>> browser.getControl(name='form.buttons.save').click()
    >>> browser.open(portalURL + '/@@ingestContent')

And did it work?

    >>> browser.contents
    '...Ingest Complete...Objects Created (2)...'
    >>> len(folder.keys())
    2
    >>> keys = folder.keys()
    >>> keys.sort()
    >>> keys
    ['mph', 'phd']
    >>> mph = folder['mph']
    >>> mph.title
    u'MPH'
    >>> mph.description
    u'Master Public Health'
    >>> mph.subjectURI
    u'http://mcl.jpl.nasa.gov/ksdb/labcascollections/2'
    >>> phd = folder['phd']
    >>> phd.title
    u'PhD'
    >>> phd.description
    u'Doctor of Philosophy'
    >>> phd.subjectURI
    u'http://mcl.jpl.nasa.gov/ksdb/labcascollections/1'

Great!  Now let's see how we work in the face of alterations to data::

    >>> browser.open(portalURL + '/my-labcascollection-folder/@@edit')    
    >>> browser.getControl(name='form.widgets.url').value = u'testscheme://localhost/rdf/labcascollections2'
    >>> browser.getControl(name='form.buttons.save').click()
    >>> browser.open(portalURL + '/@@ingestContent')
    >>> browser.contents
    '...Ingest Complete...Objects Created (1)...Objects Updated (1)...'
    >>> len(folder.keys())
    3
    >>> keys = folder.keys()
    >>> keys.sort()
    >>> keys
    ['md', 'mph', 'phd']
    >>> md = folder['md']
    >>> md.title
    u'MD'
    >>> md.description
    u'Doctor of Medicine'
    >>> mph = folder['mph']
    >>> mph.description
    u'Master of Public Health'

Good, we got a new labcascollection and an updated description to the MPH labcascollection.  Now,
let's see what happens if a labcascollection is deleted::

    >>> browser.open(portalURL + '/my-labcascollection-folder/@@edit')    
    >>> browser.getControl(name='form.widgets.url').value = u'testscheme://localhost/rdf/labcascollections3'
    >>> browser.getControl(name='form.buttons.save').click()
    >>> browser.open(portalURL + '/@@ingestContent')
    >>> browser.contents
    '...Ingest Complete...Objects Created (0)...Objects Updated (0)...Objects Deleted (1)...'
    >>> len(folder.keys())
    2
    >>> keys = folder.keys()
    >>> keys.sort()
    >>> keys
    ['md', 'mph']

Works great!
