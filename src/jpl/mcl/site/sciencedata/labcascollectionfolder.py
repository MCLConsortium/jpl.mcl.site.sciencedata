# encoding: utf-8

u'''MCL — Labcascollection Folder'''

from ._base import IIngestableFolder, Ingestor, IngestableFolderView
from .labcascollection import ILabcascollection
from five import grok


class ILabcascollectionFolder(IIngestableFolder):
    u'''Folder containing academic labcascollections.'''


class LabcascollectionIngestor(Ingestor):
    u'''RDF ingestor for academic labcascollections.'''
    grok.context(ILabcascollectionFolder)
    def getContainedObjectInterface(self):
        return ILabcascollection


class View(IngestableFolderView):
    u'''View for an labcascollection folder'''
    grok.context(ILabcascollectionFolder)
