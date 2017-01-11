# encoding: utf-8

u'''MCL — Organ'''

from . import MESSAGE_FACTORY as _
from zope import schema
from ._base import IKnowledgeObject


class IOrgan(IKnowledgeObject):
    u'''An organ is a collection of tissues joined in a structural unit to serve a common function.'''
    title = schema.TextLine(
        title=_(u'Title'),
        description=_(u'The name of this organ.'),
        required=True,
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'A brief description of this organ.'),
        required=False,
    )


IOrgan.setTaggedValue('predicateMap', {
    u'http://purl.org/dc/terms/title': 'title',
    u'http://purl.org/dc/terms/description': 'description'
})
IOrgan.setTaggedValue('fti', 'jpl.mcl.site.knowledge.organ')
IOrgan.setTaggedValue('typeURI', u'https://mcl.jpl.nasa.gov/rdf/types.rdf#Organ')
