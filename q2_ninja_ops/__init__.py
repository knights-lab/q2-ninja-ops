# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from ._format import (NinjaOpsDBDirFmt, Bowtie2IndexFormat,
                      TerrificCompressedFormat, NinjaReplicateMapFormat)
from ._type import NinjaOpsDB
from ._cluster import cluster_closed_reference
from ._database import build_database
from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

__all__ = ['cluster_closed_reference', 'build_database', 'NinjaOpsDBDirFmt',
           'Bowtie2IndexFormat', 'TerrificCompressedFormat',
           'NinjaReplicateMapFormat', 'NinjaOpsDB']
