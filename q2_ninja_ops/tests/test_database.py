# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os
import tempfile

from qiime2.plugin.testing import TestPluginBase
from qiime2.util import redirected_stdio

from q2_types.feature_data import DNAFASTAFormat

from q2_ninja_ops._database import build_database


class DatabaseTests(TestPluginBase):
    package = 'q2_ninja_ops.tests'

    def setUp(self):
        super().setUp()
        self.reference_seqs = DNAFASTAFormat(
            self.get_data_path('references.fna'), 'r')

    def test_database(self):
        with redirected_stdio(stderr=os.devnull):
            build_database(self.reference_seqs)
