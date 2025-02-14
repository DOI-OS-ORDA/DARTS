from django.test import TestCase
from search.operations.document_visibility_engine import DocumentVisibilityEngine

class DocumentVisibilityTest(TestCase):
    def setUp(self):
        self.subject = DocumentVisibilityEngine()

    def test_guest_user_sees_only_public_results(self):
        self.assertEqual(
            { 'public' : 'show' , 'private' : 'hide' },
            self.subject.call("guest")
        )

    def test_superuser_sees_all_results_and_previews(self):
        self.assertEqual(
            { 'public' : 'show' , 'private' : 'show' },
            self.subject.call("superuser")
        )

    def test_staff_sees_case_documents(self):
        self.assertEqual(
            { 'public' : 'show' , 'private' : { 'case_ids': [1, 2, 3] } },
            self.subject.call("staff", case_ids = [1, 2, 3])
        )

    def test_technical_support_group_sees_all_results_and_previews(self):
        self.assertEqual(
            { 'public' : 'show' , 'private' : 'show' },
            self.subject.call("tech_support")
        )

    def test_regional_coordinator_can_see_private_documents_in_region(self):
        self.assertEqual(
            { 'public' : 'show' , 'private' : { 'region_ids': [1] } },
            self.subject.call("regional_coordinator", region_ids = [1])
        )
