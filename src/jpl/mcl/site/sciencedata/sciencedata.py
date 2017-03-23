# encoding: utf-8

u'''MCL — Sciencedata'''

from . import MESSAGE_FACTORY as _
from zope import schema
from ._base import IScienceDataObject
from plone.formwidget.contenttree import ObjPathSourceBinder
from z3c.relationfield.schema import RelationChoice, RelationList
from jpl.mcl.site.knowledge.protocol import IProtocol
from jpl.mcl.site.knowledge.person import IPerson
from jpl.mcl.site.knowledge.organ import IOrgan
from jpl.mcl.site.knowledge.institution import IInstitution


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
    leadpi = RelationList(
        title=_(u'Lead PI(s)'),
        description=_(u'Lead PI(s) associated with this data collection.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Lead PI'),
            description=_(u'A individual lead pi in this data collection.'),
            source=ObjPathSourceBinder(object_provides=IPerson.__identifier__)
        )
    )
    organ = RelationList(
        title=_(u'Organs'),
        description=_(u'Organs associated with this data collection.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Organ'),
            description=_(u'A individual organ associated with this data collection.'),
            source=ObjPathSourceBinder(object_provides=IOrgan.__identifier__)
        )
    )
    discipline = schema.TextLine(
        title=_(u'Discipline'),
        description=_(u'The discipline of this science data collection.'),
        required=True,
    )
    institution = RelationList(
        title=_(u'Institutions'),
        description=_(u'Institutions associated with this data collection.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Institution'),
            description=_(u'A individual institution in this data collection.'),
            source=ObjPathSourceBinder(object_provides=IInstitution.__identifier__)
        )
    )
    protocol = RelationList(
        title=_(u'Protocols'),
        description=_(u'Protocols associated with this data collection.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Protocol'),
            description=_(u'A individual protocol in this data collection.'),
            source=ObjPathSourceBinder(object_provides=IProtocol.__identifier__)
        )
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
    u'CollectionName': ('title', False, ''),
    u'CollectionDescription': ('description', False, ''),
    u'id': ('collectionid', False, ''),
    u'LeadPIId': ('leadpi', True, 'https://cancer.jpl.nasa.gov/ksdb/personinput/?id='),
    u'InstitutionId': ('institution', True, 'https://cancer.jpl.nasa.gov/ksdb/institutioninput/?id='),
    u'OrganId': ('organ', True, 'https://cancer.jpl.nasa.gov/ksdb/organinput/?id='),
    u'Discipline': ('discipline', False, ''),
    u'ProtocolId': ('protocol', True, 'https://cancer.jpl.nasa.gov/ksdb/protocolinput/?id='),
    u'QAState': ('qastate', False, ''),
    u'Species': ('species', False, ''),
    u'sourceurl': ('sourceurl', False, '')
})
ISciencedata.setTaggedValue('fti', 'jpl.mcl.site.sciencedata.sciencedata')
ISciencedata.setTaggedValue('typeValue', u'MCL')
ISciencedata.setTaggedValue('typeKey', u'Consortium')
