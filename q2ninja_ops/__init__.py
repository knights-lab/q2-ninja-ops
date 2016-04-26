import json
import os.path
import tempfile
import subprocess

import biom
import skbio.io


__version__ = '0.0.0-dev'

# TODO handle wrapping external applications better, this copies/parses a lot
# of data unnecessarily
def pick_reference_otus(sequences):
    # TODO update when https://github.com/biocore/qiime2/issues/12 is resolved
    with tempfile.TemporaryDirectory(prefix='q2ninja-ops-temp-') as tempdir:
        input_fasta_filepath = os.path.join(tempdir, 'input-sequences.fasta')
        output_directory = os.path.join(tempdir, 'ninja-ops-output')
        skbio.io.write(sequences, format='fasta', into=input_fasta_filepath)

        completed_process = subprocess.run(
            ['ninja.py', '-i', input_fasta_filepath, '-o', output_directory],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        with open(os.path.join(output_directory, 'ninja_otutable.biom')) as fh:
            return biom.Table.from_json(json.load(fh))
