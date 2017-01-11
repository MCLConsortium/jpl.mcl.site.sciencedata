# encoding: utf-8

u'''MCL — Degree'''

from . import MESSAGE_FACTORY as _
from zope import schema
from ._base import IKnowledgeObject


class IDegree(IKnowledgeObject):
    u'''An academic degree that a university typically confers upon an individual.'''
    title = schema.TextLine(
        title=_(u'Title'),
        description=_(u'The name of this degree.'),
        required=True,
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'A brief description of this degree.'),
        required=False,
    )


IDegree.setTaggedValue('predicateMap', {
    u'http://purl.org/dc/terms/title': 'title',
    u'http://purl.org/dc/terms/description': 'description'
})
IDegree.setTaggedValue('fti', 'jpl.mcl.site.knowledge.degree')
IDegree.setTaggedValue('typeURI', u'https://mcl.jpl.nasa.gov/rdf/types.rdf#Degree')
