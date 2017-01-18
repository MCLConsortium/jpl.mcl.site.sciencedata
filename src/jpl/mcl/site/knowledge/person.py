# encoding: utf-8

u'''MCL — Person'''

from . import MESSAGE_FACTORY as _
from zope import schema
from ._base import IKnowledgeObject
from degree import IDegree
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder

FOAF_SURNAME = u'http://xmlns.com/foaf/0.1/surname'
FOAF_GIVENNAME = u'http://xmlns.com/foaf/0.1/givenname'


class IPerson(IKnowledgeObject):
    u'''An individual member of the MCL consortium.'''
    title = schema.TextLine(
        title=_(u'Name'),
        description=_(u'Full name of this person.'),
        required=True
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'A short summary of this person.'),
        required=False,
    )
    surname = schema.TextLine(
        title=_(u'Surname'),
        description=_(u'Surname (family name, last name, etc.) of this person.'),
        required=False,
    )
    givenName = schema.TextLine(
        title=_(u'Given Name'),
        description=_(u'Given name (first name, etc.) of this person.'),
        required=False,
    )
    degrees = RelationList(
        title=_(u'Degrees'),
        description=_(u'Academic degrees conferred upon this person.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Degree'),
            description=_(u'A single academic degree conferred upon this person.'),
            source=ObjPathSourceBinder(object_provides=IDegree.__identifier__)
        )
    )
    email = schema.TextLine(
        title=_(u'Email Address'),
        description=_(u'Electronic mail address via which this person may be contacted.'),
        required=False,
    )
    phone = schema.TextLine(
        title=_(u'Telephone Number'),
        description=_(u'Public switched telephone network number where this person may be called.'),
        required=False,
    )


IPerson.setTaggedValue('predicateMap', {
    FOAF_SURNAME: ('surname', False),
    FOAF_GIVENNAME: ('givenName', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#degree': ('degrees', True),
    u'http://xmlns.com/foaf/0.1/mbox': ('email', False),
    u'http://xmlns.com/foaf/0.1/phone': ('phone', False)
})
IPerson.setTaggedValue('fti', 'jpl.mcl.site.knowledge.person')
IPerson.setTaggedValue('typeURI', u'https://mcl.jpl.nasa.gov/rdf/types.rdf#Person')
