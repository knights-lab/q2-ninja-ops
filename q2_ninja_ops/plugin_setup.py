# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import Plugin
from q2_types.sample_data import SampleData
from q2_types.per_sample_sequences import Sequences
from q2_types.feature_table import FeatureTable, Frequency
from q2_types.feature_data import FeatureData, Sequence

from q2_ninja_ops import (NinjaOpsDB, NinjaOpsDBDirFmt, Bowtie2IndexFormat,
                          TerrificCompressedFormat, NinjaReplicateMapFormat,
                          cluster_closed_reference, build_database)
import q2_ninja_ops


plugin = Plugin(
    name='ninja-ops',
    version=q2_ninja_ops.__version__,
    website='https://github.com/knights-lab/q2-ninja-ops',
    package='q2_ninja_ops',
    citation_text='Al-Ghalith GA, Montassier E, Ward HN, Knights D. '
                  'NINJA-OPS: Fast Accurate Marker Gene Alignment Using '
                  'Concatenated Ribosomes. PLoS Computational Biology. '
                  '2016 Jan;12(1).',
    short_description='Plugin for OTU picking with NINJA-OPS.',
    description='This plugin wraps the NINJA-OPS application and provides '
                'methods for clustering sequence data into OTUs.'
)

plugin.register_semantic_types(NinjaOpsDB)

plugin.register_formats(NinjaOpsDBDirFmt, Bowtie2IndexFormat,
                        TerrificCompressedFormat, NinjaReplicateMapFormat)

plugin.register_semantic_type_to_format(NinjaOpsDB,
                                        artifact_format=NinjaOpsDBDirFmt)

plugin.methods.register_function(
    function=cluster_closed_reference,
    inputs={
        'sequences': SampleData[Sequences],
        'reference_database': NinjaOpsDB
    },
    parameters={
        # TODO expose relevant NINJA-OPS parameters here
    },
    outputs=[
        ('clustered_table', FeatureTable[Frequency]),
        ('unmatched_sequences', SampleData[Sequences])
    ],
    input_descriptions={
        # TODO document inputs
    },
    parameter_descriptions={
        # TODO document parameters
    },
    output_descriptions={
        # TODO document outputs
    },
    name='Closed-reference clustering of sequences.',
    # TODO write better docs
    description="Run NINJA-OPS on sequence data to produce a closed-reference "
                "OTU table."
)

plugin.methods.register_function(
    function=build_database,
    inputs={
        'reference_sequences': FeatureData[Sequence]
    },
    parameters={},
    outputs=[
        ('database', NinjaOpsDB)
    ],
    input_descriptions={
        # TODO document inputs
    },
    output_descriptions={
        # TODO document outputs
    },
    name='Build a NINJA-OPS reference database.',
    # TODO write better docs
    description="Build a NINJA-OPS database from reference sequences."
)
