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
        self.database = self.get_data_path('db')
        self.tcf = self.get_data_path('db/db.tcf')
        self.ninja_replicate_format = self.get_data_path('db/db.db')

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_database_creation(self):
        current_dir = os.getcwd()
        os.chdir(self.temp_dir.name)

        with redirected_stdio(stderr=os.devnull):
            database = build_database(self.reference_seqs)

        db_format = NinjaOpsDBDirFmt(str(database), mode='r')
        db_format.validate()

        # TODO: I'm not sure if we have to validate these formats individually or not
        tcf_format = TerrificCompressedFormat(os.path.join(str(database), 'db.tcf'), mode='r')
        tcf_format.validate()

        map_format = NinjaReplicateMapFormat(os.path.join(str(database), 'db.db'), mode='r')
        map_format.validate()

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
