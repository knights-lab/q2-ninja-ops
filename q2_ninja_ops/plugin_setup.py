from qiime2.plugin import Plugin, Int

import q2_ninja_ops
from q2_ninja_ops.artifact_types import SequenceData, DNA
from feature_table.artifact_types import FeatureTable, Frequency

plugin = Plugin(
    name='ninja-ops',
    version=q2ninja_ops.__version__,
    website='https://github.com/knights-lab/q2-ninja-ops',
    package='q2ninja_ops'
)

plugin.register_function(
    function=q2_ninja_ops.pick_reference_otus,
    # TODO make this accept other types of sequence data as input
    inputs={'sequences': SequenceData[DNA]},
    outputs=[('feature_table', FeatureTable[Frequency])],
    name='Pick closed reference OTUs',
    # TODO write better docs
    doc="Runs NINJA-OPS on sequence data to produce a closed reference OTU "
        "table"
)
