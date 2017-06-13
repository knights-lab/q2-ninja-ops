# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages

import versioneer

setup(
    name="q2-ninja-ops",
    # TODO stop duplicating version string
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    # TODO this plugins depends on conda package bowtie2
    install_requires=['qiime >= 2.0.0', 'feature_table', 'scikit-bio', 'biom-format'],
    package_data={'feature_table': ['workflows/*md']},
    author="Ben, Gabe, Jai",
    author_email="hillm096@umn.edu",
    description="Functionality for working with NINJA-OPS.",
    license="ISC",
    url="http://www.ninja-ops.ninja",
    entry_points={
        'qiime.plugin': ['q2-ninja-ops=q2ninja_ops.plugin_setup:plugin']
    }
)
