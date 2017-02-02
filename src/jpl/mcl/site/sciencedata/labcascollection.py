# encoding: utf-8

u'''MCL — Labcascollection'''

from . import MESSAGE_FACTORY as _
from zope import schema
from ._base import IScienceDataObject


class ILabcascollection(IScienceDataObject):
    u'''An academic labcascollection that a university typically confers upon an individual.'''
    title = schema.TextLine(
        title=_(u'Title'),
        description=_(u'The name of this labcascollection.'),
        required=True,
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'A brief description of this labcascollection.'),
        required=False,
    )


ILabcascollection.setTaggedValue('predicateMap', {
    u'http://purl.org/dc/terms/title': ('title', False),
    u'http://purl.org/dc/terms/description': ('description', False)
})
ILabcascollection.setTaggedValue('fti', 'jpl.mcl.site.sciencedata.labcascollection')
ILabcascollection.setTaggedValue('typeURI', u'https://mcl.jpl.nasa.gov/rdf/types.rdf#Labcascollection')
