# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime.plugin import Plugin, Int

import q2ninja_ops
# from feature_table.artifact_types import (
    # FeatureTable, Frequency, RelativeFrequency, PresenceAbsence)

plugin = Plugin(
    name='ninja-ops',
    version=q2ninja_ops.__version__,
    website='',
    package='q2ninja_ops'
)

# TODO create decorator for promoting functions to workflows. This info would
# be moved to the decorator calls.
# plugin.register_function(
#     function=feature_table.rarefy,
#     # TODO use more restrictive primitive type for `depth`
#     inputs={'table': FeatureTable[Frequency], 'depth': Int},
#     outputs=[('rarefied_table', FeatureTable[Frequency])],
#     name='Rarefaction',
#     doc="Let's rarefy!"
# )
#
# plugin.register_function(
#     function=feature_table.presence_absence,
#     inputs={'table': FeatureTable[~PresenceAbsence]},
#     outputs=[('presence_absence_table', FeatureTable[PresenceAbsence])],
#     name='Convert to presence/absence',
#     doc="Let's convert to presence/absence!"
# )
#
# plugin.register_function(
#     function=feature_table.relative_frequency,
#     inputs={'table': FeatureTable[Frequency]},
#     outputs=[('relative_frequency_table', FeatureTable[RelativeFrequency])],
#     name='Convert to relative frequencies',
#     doc="Let's convert to relative frequencies!"
# )
#
# plugin.register_workflow('workflows/summarize.md')
