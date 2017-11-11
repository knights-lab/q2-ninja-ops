# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from q2_types.feature_data import DNAFASTAFormat

from q2_ninja_ops import NinjaOpsDBDirFmt


def build_database(reference_sequences: DNAFASTAFormat) -> NinjaOpsDBDirFmt:
    # Input
    ref_filepath = str(reference_sequences)

    # Output
    database = NinjaOpsDBDirFmt()
    database_dir = str(database)

    # TODO run commands to build NINJA-OPS database inside `database_dir`

    return database
