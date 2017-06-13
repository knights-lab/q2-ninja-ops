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
    cmdclass=versioner.get_cmdclass(),
    packages=find_packages(),
    install_requires=['biom-format >= 2.1.5, < 2.2.0', 'scipy', 'IPython',
                      'ipywidgets', 'seaborn', 'qiime >= 2.0.0'],
    package_data={'feature_table': ['workflows/*md']},
    author="Ben, Gabe, Jai",
    author_email="hillmannben@gmail.com",
    description="Functionality for working with NINJA-OPS.",
    license="BSD",
    url="http://www.ninja-ops.ninja",
    entry_points={
        'qiime.plugin': ['ninja-ops=feature_table.plugin_setup:plugin']
    }
)