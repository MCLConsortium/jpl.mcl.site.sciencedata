# encoding: utf-8

u'''MCL — Organ Folder'''

from ._base import IIngestableFolder, Ingestor
from .organ import IOrgan
from five import grok


class IOrganFolder(IIngestableFolder):
    u'''Folder containing body systems, also known as organs.'''


class OrganIngestor(Ingestor):
    u'''RDF ingestor for organs.'''
    grok.context(IOrganFolder)
    def getContainedObjectInterface(self):
        return IOrgan
