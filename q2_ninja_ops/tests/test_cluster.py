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

from q2_types.per_sample_sequences import QIIME1DemuxFormat

from q2_ninja_ops._format import NinjaOpsDBDirFmt
from q2_ninja_ops._cluster import cluster_closed_reference


class NinjaClusterTests(TestPluginBase):
    package = 'q2_ninja_ops.tests'

    def setUp(self):
        super().setUp()

        # Reference database creation
        self.queries = QIIME1DemuxFormat(self.get_data_path('queries.fna'), 'r')

        self.temp_dir = tempfile.TemporaryDirectory(prefix='db')

        # Database
        self.database = NinjaOpsDBDirFmt(self.get_data_path('database'), 'r')

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_cluster_closed_references(self):
        with redirected_stdio(stderr=os.devnull, stdout=os.devnull):
            output_biom_fmt, output_failures_fmt = cluster_closed_reference(self.queries, self.database)

# TODO: Dig into what the output formats are. Add more test cases?
