# encoding: utf-8

u'''JPL MCL Site Science Data — setup handlers.'''

from ._utils import publish
from plone.dexterity.utils import createContentInContainer
from plone.registry.interfaces import IRegistry
from ZODB.DemoStorage import DemoStorage
from zope.component import getUtility
import socket, logging

_logger = logging.getLogger(__name__)


# There has to be a better way of doing this:
if socket.gethostname() == 'tumor.jpl.nasa.gov' or socket.gethostname().endswith('.local'):
    _logger.warn(u'Using development KSDB on edrn-dev.jpl.nasa.gov instead of production')
    _rdfBaseURL = u'https://edrn-dev.jpl.nasa.gov/ksdb/publishrdf/?rdftype='
else:
    _rdfBaseURL = u'https://mcl.jpl.nasa.gov/ksdb/publishrdf/?rdftype='


def createScienceDataFolders(setupTool):
    if setupTool.readDataFile('jpl.mcl.site.sciencedata.txt') is None: return
    portal = setupTool.getSite()
    # Don't bother if we're running in the test fixture
    if hasattr(portal._p_jar, 'db') and isinstance(portal._p_jar.db().storage, DemoStorage): return
    if 'sciencedata' in portal.keys(): return
    sciencedata = createContentInContainer(
        portal, 'Folder', title=u'Science Data',
        description=u"MCL's Science Data Environment"
    )
    createContentInContainer(
        sciencedata, 'jpl.mcl.site.sciencedata.labcascollectionfolder', title=u'Labcas Collections',
        description=u'Labcas collections sourced from labcas.',
        url=_rdfBaseURL + u'labcascollection', ingestEnabled=True
    )
    publish(sciencedata)
    registry = getUtility(IRegistry)
    registry['jpl.mcl.site.sciencedata.interfaces.ISettings.objects'] = [
        u'sciencedata/labcascollection'
    ]
