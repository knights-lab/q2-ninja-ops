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

from q2_ninja_ops._format import NinjaOpsDBDirFmt, TerrificCompressedFormat, NinjaReplicateMapFormat
from q2_ninja_ops._database import build_database


class NinjaDatabaseTests(TestPluginBase):
    package = 'q2_ninja_ops.tests'

    def setUp(self):
        super().setUp()

        # Reference database creation
        self.reference_seqs = DNAFASTAFormat(
            self.get_data_path('references.fna'), 'r')
        self.temp_dir = tempfile.TemporaryDirectory(prefix='db')

        # Database Directories
        self.database = self.get_data_path('database')
        self.tcf = os.path.join(self.database, 'db', 'db.tcf')
        self.ninja_replicate_format = os.path.join(self.database, 'db', 'db.db')

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_database_creation(self):
        current_dir = os.getcwd()
        os.chdir(self.temp_dir.name)

        with redirected_stdio(stderr=os.devnull, stdout=os.devnull):
            database = build_database(self.reference_seqs)

        format = NinjaOpsDBDirFmt(str(database), mode='r')
        format.validate()

        format = TerrificCompressedFormat(os.path.join(str(database), 'db', 'db.tcf'), mode='r')
        format.validate()

        format = NinjaReplicateMapFormat(os.path.join(str(database), 'db', 'db.db'), mode='r')
        format.validate()

        os.chdir(current_dir)

    def test_database_format(self):
        format = NinjaOpsDBDirFmt(self.database, mode='r')
        format.validate()

    def test_terrific_compressed_format(self):
        format = TerrificCompressedFormat(self.tcf, mode='r')
        format.validate()

    def test_ninja_replicate_format(self):
        format = NinjaReplicateMapFormat(self.ninja_replicate_format, mode='r')
        format.validate()
