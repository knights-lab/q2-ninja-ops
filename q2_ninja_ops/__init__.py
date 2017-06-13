__version__ = '0,0.0-dev'
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

import json
import os.path
import tempfile
import subprocess
from q2_types.per_sample_sequences import SequencesWithQuality

import biom
import skbio.io

def run_commands(cmds, verbose=True):
    if verbose:
        print("Running external command line application(s). This may print "
              "messages to stdout and/or stderr.")
        print("The command(s) being run are below. These commands cannot "
              "be manually re-run as they will depend on temporary files that "
              "no longer exist.")
    for cmd in cmds:
        if verbose:
            print("\nCommand:", end=' ')
            print(" ".join(cmd), end='\n\n')
        subprocess.run(cmd, check=True)

# TODO handle wrapping external applications better, this copies/parses a lot
# of data unnecessarily
def pick_reference_otus(sequences: SequencesWithQuality) -> biom.Table:
    # TODO update when https://github.com/biocore/qiime2/issues/12 is resolved
    with tempfile.TemporaryDirectory(prefix='q2ninja-ops-temp-') as tempdir:
        input_fasta_filepath = os.path.join(tempdir, 'input-sequences.fasta')
        output_directory = os.path.join(tempdir, 'ninja-ops-output')
        skbio.io.write(sequences, format='fasta', into=input_fasta_filepath)

        cmd = ['ninja.py', '-i', input_fasta_filepath, '-o', output_directory]
        try:
            run_commands([cmds])
        except subprocess.CalledProcessError as e:
            raise

        with open(os.path.join(output_directory, 'ninja_otutable.biom')) as fh:
            return biom.Table.from_json(json.load(fh))
