from setuptools import setup, find_packages

setup(
    name="q2-ninja-ops",
    # TODO stop duplicating version string
    version='0.0.0-dev',
    packages=find_packages(),
    # TODO this plugin depends on conda package bowtie2
    install_requires=['qiime >= 2.0.0', 'feature_table', 'scikit-bio',
                      'biom-format'],
    package_data={'q2ninja_ops': ['workflows/*md']},
    author="Ben, Gabe, Jai",
    author_email="hillmannben@gmail.com",
    description="QIIME 2 plugin for working with NINJA-OPS.",
    license="",
    url="http://www.ninja-ops.ninja",
    entry_points={
        'qiime.plugin': ['q2-ninja-ops=q2ninja_ops.plugin_setup:plugin']
    }
)
