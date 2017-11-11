# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os.path

import skbio.io
import qiime2.plugin.model as model
from q2_types.feature_table import BIOMV100Format
from q2_types.per_sample_sequences import QIIME1DemuxFormat

from q2_ninja_ops import NinjaOpsDBDirFmt
from q2_ninja_ops._util import run_command


# TODO when writing unit tests, make sure that sample IDs containing
# underscores work correctly with NINJA-OPS.
def cluster_closed_reference(sequences: QIIME1DemuxFormat,
                             reference_database: NinjaOpsDBDirFmt) \
                                     -> (BIOMV100Format, QIIME1DemuxFormat):
    # Input paths supplied to ninja.py.
    sequences_fp = str(sequences)
    reference_database_dir = os.path.join(str(reference_database), 'db')

    # Output directory to store ninja.py results.
    output_dirfmt = model.DirectoryFormat()
    output_dir = str(output_dirfmt)

    cmd = ['ninja.py',
           '--input', sequences_fp, '--database', reference_database_dir,
           '--output', output_dir, '--full_output']
    run_command(cmd)

    biom_fp = os.path.join(output_dir, 'ninja_otutable.biom')
    output_biom_fmt = BIOMV100Format(biom_fp, mode='r')
    # Keep a reference to the DirectoryFormat this BIOM file resides in so that
    # the directory isn't deleted when `output_dirfmt` goes out of scope upon
    # function exit. The directory will be cleaned up appropriately when
    # `output_biom_fmt` is cleaned up and avoids copying the BIOM file.
    output_biom_fmt.__dirfmt = output_dirfmt

    # Get the set of IDs that failed to hit the reference database.
    failed_ids = set()
    failed_ids_fp = os.path.join(output_dir, 'ninja_fail.txt')
    with open(failed_ids_fp, 'r') as fh:
        for line in fh:
            id = line.rstrip('\n')
            failed_ids.add(id)

    # Filter the input sequences to only those that failed to hit the reference
    # database.
    output_failures_fmt = QIIME1DemuxFormat()
    with output_failures_fmt.open() as fh:
        for seq in skbio.io.read(sequences_fp, format='fasta'):
            id = seq.metadata['id']
            if id in failed_ids:
                # Turning off roundtripping options to speed up writing. We can
                # safely turn these options off because we know the sequence
                # IDs are rountrip-safe since we're reading them from a FASTA
                # file.
                #
                # http://scikit-bio.org/docs/latest/generated/
                #     skbio.io.format.fasta.html#writer-specific-parameters
                seq.write(fh, id_whitespace_replacement=None,
                          description_newline_replacement=None)

    return output_biom_fmt, output_failures_fmt
