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


Degrees
=======

A degree is an academic rank conferred by a college or university after
examination or after completion of a course of study, or conferred as an honor
on a distinguished person.  They go in Degree Folders, which can be added
anywhere:

    >>> browser.open(portalURL)
    >>> l = browser.getLink(id='jpl-mcl-site-knowledge-degreefolder')
    >>> l.url.endswith('++add++jpl.mcl.site.knowledge.degreefolder')
    True
    >>> l.click()
    >>> browser.getControl(name='form.widgets.title').value = u'My Degree Folder'
    >>> browser.getControl(name='form.widgets.description').value = u'Some of my favorite degrees.'
    >>> browser.getControl(name='form.widgets.url').value = u'testscheme://localhost/rdf/degrees1'
    >>> browser.getControl(name='form.widgets.ingestEnabled:list').value = False
    >>> browser.getControl(name='form.buttons.save').click()
    >>> 'my-degree-folder' in portal.keys()
    True

The folder is currently empty::

    >>> folder = portal['my-degree-folder']
    >>> len(folder.keys())
    0

Note that we've set ``ingestEnabled`` to ``False``.  So if we try to ingest
that folder, nothing will happen.  How do we start the ingest process?  By
visiting a view at the root of the site::

    >>> from plone.registry.interfaces import IRegistry
    >>> from zope.component import getUtility
    >>> registry = getUtility(IRegistry)
    >>> registry['jpl.mcl.site.knowledge.interfaces.ISettings.objects'] = [u'my-degree-folder']
    >>> import transaction
    >>> transaction.commit()
    >>> browser.open(portalURL + '/@@ingestContent')

But since the degree folder had ingest disabled, it's still empty::

    >>> len(folder.keys())
    0

So let's enable ingest and try again::

    >>> browser.open(portalURL + '/my-degree-folder/@@edit')    
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
    u'http://mcl.jpl.nasa.gov/ksdb/degrees/2'
    >>> phd = folder['phd']
    >>> phd.title
    u'PhD'
    >>> phd.description
    u'Doctor of Philosophy'
    >>> phd.subjectURI
    u'http://mcl.jpl.nasa.gov/ksdb/degrees/1'

Great!  Now let's see how we work in the face of alterations to data::

    >>> browser.open(portalURL + '/my-degree-folder/@@edit')    
    >>> browser.getControl(name='form.widgets.url').value = u'testscheme://localhost/rdf/degrees2'
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

Good, we got a new degree and an updated description to the MPH degree.  Now,
let's see what happens if a degree is deleted::

    >>> browser.open(portalURL + '/my-degree-folder/@@edit')    
    >>> browser.getControl(name='form.widgets.url').value = u'testscheme://localhost/rdf/degrees3'
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


Organs
======

An organ is a system of the body.  They're pretty much identical to degrees in
that they have just titles and descriptions and go into organ folders::

    >>> browser.open(portalURL)
    >>> l = browser.getLink(id='jpl-mcl-site-knowledge-organfolder')
    >>> l.url.endswith('++add++jpl.mcl.site.knowledge.organfolder')
    True
    >>> l.click()
    >>> browser.getControl(name='form.widgets.title').value = u'My Organ Folder'
    >>> browser.getControl(name='form.widgets.description').value = u'Some of my favorite organs.'
    >>> browser.getControl(name='form.widgets.url').value = u'testscheme://localhost/rdf/organs'
    >>> browser.getControl(name='form.widgets.ingestEnabled:list').value = True
    >>> browser.getControl(name='form.buttons.save').click()
    >>> 'my-organ-folder' in portal.keys()
    True
    >>> folder = portal['my-organ-folder']
    >>> folder.title
    u'My Organ Folder'
    >>> folder.description
    u'Some of my favorite organs.'
    >>> folder.url
    'testscheme://localhost/rdf/organs'
    >>> folder.ingestEnabled
    True

Let's ingest and see what we get::

    >>> registry['jpl.mcl.site.knowledge.interfaces.ISettings.objects'] = [u'my-degree-folder', u'my-organ-folder']
    >>> transaction.commit()
    >>> browser.open(portalURL + '/@@ingestContent')
    >>> browser.contents
    '...Ingest Complete...Objects Created (2)...Objects Updated (0)...Objects Deleted (0)...'
    >>> len(folder.keys())
    2
    >>> keys = folder.keys()
    >>> keys.sort()
    >>> keys
    ['anus', 'spleen']
    >>> anus = folder['anus']
    >>> anus.title
    u'Anus'
    >>> anus.description
    u'The human anus is the external opening of the rectum.'

Works fine!


People
======

OK, let's try people::

    >>> browser.open(portalURL)
    >>> l = browser.getLink(id='jpl-mcl-site-knowledge-personfolder')
    >>> l.url.endswith('++add++jpl.mcl.site.knowledge.personfolder')
    True
    >>> l.click()
    >>> browser.getControl(name='form.widgets.title').value = u'My Person Folder'
    >>> browser.getControl(name='form.widgets.description').value = u'Some of my favorite people.'
    >>> browser.getControl(name='form.widgets.url').value = u'testscheme://localhost/rdf/person'
    >>> browser.getControl(name='form.widgets.ingestEnabled:list').value = True
    >>> browser.getControl(name='form.buttons.save').click()
    >>> 'my-person-folder' in portal.keys()
    True
    >>> folder = portal['my-person-folder']
    >>> folder.title
    u'My Person Folder'
    >>> folder.description
    u'Some of my favorite people.'
    >>> folder.url
    'testscheme://localhost/rdf/person'
    >>> folder.ingestEnabled
    True

Let's ingest and see what we get::

    >>> registry['jpl.mcl.site.knowledge.interfaces.ISettings.objects'] = [u'my-degree-folder', u'my-organ-folder', u'my-person-folder']
    >>> transaction.commit()
    >>> browser.open(portalURL + '/@@ingestContent')
    >>> browser.contents
    '...Ingest Complete...Objects Created (2)...Objects Updated (0)...Objects Deleted (0)...'
    >>> len(folder.keys())
    2
    >>> keys = folder.keys()
    >>> keys.sort()
    >>> keys
    ['92346728-5e785b50', 'liu-beverley']
    >>> liu = folder['liu-beverley']
    >>> liu.title
    u'Liu, Beverley'
    >>> liu.givenName
    u'Beverley'
    >>> liu.surname
    u'Liu'
    >>> degrees = [i.title for i in liu.degrees]
    >>> degrees.sort()
    >>> degrees
    [u'MD', u'MPH']
    >>> liu.email
    u'mailto:bl@mdanderson.org'
    >>> liu.phone
    u'+1 713 555 7856'

Works fine!


Projects
========

Let's try …


Institutions
============


Funded Sites
============


Personnel
=========


Protocols
=========


Publications
============
