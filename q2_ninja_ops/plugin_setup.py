from qiime2.plugin import Plugin, Int

import q2_ninja_ops
from q2_types.per_sample_sequences import SequencesWithQuality
from q2_types.feature_table import FeatureTable, Frequency

plugin = Plugin(
    name='ninja-ops',
    version=q2_ninja_ops.__version__,
    website='https://github.com/knights-lab/q2-ninja-ops',
    package='q2ninja_ops'
)

plugin.methods.register_function(
    function=q2_ninja_ops.pick_reference_otus,
    # TODO make this accept other types of sequence data as input
    inputs={'sequences': SequencesWithQuality},
    outputs=[('feature_table', FeatureTable[Frequency])],
    parameters={},
    name='Pick closed reference OTUs',
    # TODO write better docs
    description="Runs NINJA-OPS on sequence data to produce a closed reference OTU "
        "table"
)
