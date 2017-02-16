# encoding: utf-8

u'''MCL — Sciencedata'''

from . import MESSAGE_FACTORY as _
from zope import schema
from ._base import IScienceDataObject


class ISciencedata(IScienceDataObject):
    u'''An academic sciencedata that a university typically confers upon an individual.'''
    title = schema.TextLine(
        title=_(u'Title'),
        description=_(u'The name of this science data collection.'),
        required=True,
    )
    collectionid = schema.TextLine(
        title=_(u'Collection ID'),
        description=_(u'The id of this science data collection.'),
        required=True,
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'A brief description of this science data collection.'),
        required=False,
    )
    sourceurl = schema.TextLine(
        title=_(u'Science data URL'),
        description=_(u'The url of this science data collection.'),
        required=True,
    )
    leadpi = schema.TextLine(
        title=_(u'Lead PI'),
        description=_(u'The Lead PI associated with this science data collection.'),
        required=True,
    )
    organ = schema.TextLine(
        title=_(u'Organ'),
        description=_(u'The organ associated with this science data collection.'),
        required=True,
    )
    discipline = schema.TextLine(
        title=_(u'Discipline'),
        description=_(u'The discipline of this science data collection.'),
        required=True,
    )
    protocol = schema.TextLine(
        title=_(u'Protocol'),
        description=_(u'The protocol of this science data collection.'),
        required=True,
    )
    qastate = schema.TextLine(
        title=_(u'QA Status'),
        description=_(u'The QA status of this science data collection.'),
        required=True,
    )
    species = schema.TextLine(
        title=_(u'Species'),
        description=_(u'The species of this science data collection.'),
        required=True,
    )

ISciencedata.setTaggedValue('predicateMap', {
    u'CollectionName': ('title', False),
    u'CollectionDescription': ('description', False),
    u'id': ('collectionid', False),
    u'LeadPI': ('leadpi', False),
    u'OrganSite': ('organ', False),
    u'Discipline': ('discipline', False),
    u'ProtocolId': ('protocol', False),
    u'QAState': ('qastate', False),
    u'Species': ('species', False),
    u'sourceurl': ('sourceurl', False)
})
ISciencedata.setTaggedValue('fti', 'jpl.mcl.site.sciencedata.sciencedata')
ISciencedata.setTaggedValue('typeValue', u'MCL')
ISciencedata.setTaggedValue('typeKey', u'Consortium')
