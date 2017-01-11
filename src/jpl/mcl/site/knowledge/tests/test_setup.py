# encoding: utf-8

u'''MCL Site Knowledge — setup tests'''

from jpl.mcl.site.knowledge.testing import JPL_MCL_SITE_KNOWLEDGE_INTEGRATION_TESTING
import unittest, plone.api


class SetupTest(unittest.TestCase):
    layer = JPL_MCL_SITE_KNOWLEDGE_INTEGRATION_TESTING
    def setUp(self):
        super(SetupTest, self).setUp()
        self.portal = self.layer['portal']
    def testCatalogIndexes(self):
        u'''Ensure the catalog has our custom indexes'''
        catalog = plone.api.portal.get_tool('portal_catalog')
        indexes = catalog.indexes()
        self.assertTrue('subjectURI' in indexes, u'"subjectURI" index not installed')
    def testCatalogMetadata(self):
        u'''Check that the catalog has our custom metadata columns'''
        catalog = plone.api.portal.get_tool('portal_catalog')
        columns = catalog.schema()
        self.assertTrue('subjectURI' in columns, u'"subjectURI" column not installed')
    # def testTypes(self):
    #     u'''Check types'''
    #     types = getToolByName(self.portal, 'portal_types')
    #     for t in ('eke.labcas.labcasfolder', 'eke.labcas.labcasdataset'):
    #         self.failUnless(t in types, u'Type {} not in portal_types'.format(t))
    #     folderType = types['eke.labcas.labcasfolder']
    #     self.failUnless('eke.labcas.labcasdataset' in folderType.allowed_content_types,
    #         u"eke.labcas.labcasdataset doesn't appear in eke.labcas.labcasfolder's allowed types")


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
