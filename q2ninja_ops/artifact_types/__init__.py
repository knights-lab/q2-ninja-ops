import skbio.io
from qiime.plugin import Type


class SequenceData(Type, variant_of=Type.Artifact, fields='SequenceType'):
    class SequenceType:
        def get_constructor(self):
            return skbio.Sequence

    def load(self, data_reader):
        constructor = self.fields[0]().get_constructor()
        fh = data_reader.get_file('sequence-data.fasta')
        return skbio.io.read(fh, format='fasta', constructor=constructor)

    def save(self, data, data_writer):
        fh = data_writer.create_file('sequence-data.fasta')
        skbio.io.write(data, format='fasta', into=fh)


class DNA(Type, variant_of=SequenceData.SequenceType):
    def get_constructor(self):
        return skbio.DNA


class RNA(Type, variant_of=SequenceData.SequenceType):
    def get_constructor(self):
        return skbio.RNA


class Protein(Type, variant_of=SequenceData.SequenceType):
    def get_constructor(self):
        return skbio.Protein
