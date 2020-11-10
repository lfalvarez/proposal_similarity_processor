#!/usr/bin/env python

"""Tests for `proposal_similarity_processor` package."""


import unittest

from proposal_similarity_processor import proposal_similarity_processor
from proposal_similarity_processor.document import Document


class TestProposalDocument(unittest.TestCase):
    """Tests for `proposal_similarity_processor` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_instanciate(self):
        """Test something."""
        document = Document(id=1, content='hola esto es una prueba')
        self.assertTrue(document)
        self.assertEqual(1, document.id)
        self.assertEqual('hola esto es una prueba', document.content)
