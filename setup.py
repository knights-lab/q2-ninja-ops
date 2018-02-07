# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages

import versioneer

setup(
    name="q2-ninja-ops",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    author="Ben, Gabe, Jai",
    author_email="hillm096@umn.edu",
    description="QIIME 2 NINJA-OPS plugin",
    license="ISC",
    url="http://www.ninja-ops.ninja",
    entry_points={
        'qiime2.plugins': ['q2-ninja-ops=q2_ninja_ops.plugin_setup:plugin']
    },
    package_data={'q2_ninja_ops.data': ['data/*']},
    zip_safe=False
)
