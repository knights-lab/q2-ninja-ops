# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os

from q2_types.feature_data import DNAFASTAFormat

from q2_ninja_ops import NinjaOpsDBDirFmt
from q2_ninja_ops._util import run_command


def build_database(reference_sequences: DNAFASTAFormat) -> NinjaOpsDBDirFmt:
    # Input
    ref_filepath = str(reference_sequences)

    # Output
    database = NinjaOpsDBDirFmt()
    database_dir = str(database)

    output_prefix = "db"
    output_dir = os.path.join(database_dir, output_prefix)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Run commands to build NINJA-OPS database inside `database_dir`
    # NINJA prep the database
    ninja_prep_cmd = ['ninja_prep', ref_filepath, output_prefix]
    run_command(ninja_prep_cmd)

    # Build the Bowtie2 from ninja prep
    bt2_build_cmd = ['bowtie2-build-s', output_prefix + ".fa", output_prefix]
    run_command(bt2_build_cmd)

    # Set the required files for db
    output_suffixes = (".1.bt2", ".2.bt2", ".3.bt2", ".4.bt2", ".rev.1.bt2", ".rev.2.bt2", ".db", ".tcf")
    output_files = (output_prefix + _ for _ in output_suffixes)

    # Move all files to database dir from QIIME2 nebula working dir
    for file in output_files:
        os.rename(file, os.path.join(output_dir, file))

    return database
