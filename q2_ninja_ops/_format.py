# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import qiime2.plugin.model as model
from qiime2.plugin import ValidationError


# TODO is the bowtie2 index format documented somewhere? Need to implement
# validation, for now any file is accepted. The .bt2 files don't appear to have
# a standard header to sniff. Also, I'm currently assuming the .rev.*.bt2 files
# follow the same format as the non-rev .bt2 files.
#
# TODO consider migrating to q2-types if this format will be generally useful
class Bowtie2IndexFormat(model.BinaryFileFormat):
    def _validate_(self, level):
        pass


class TerrificCompressedFormat(model.BinaryFileFormat):
    def _validate_(self, level):
        with self.open() as fh:
            if fh.peek(2)[:2] != b'>\x00':
                raise ValidationError(
                    "The first two bytes of the file do not match the "
                    "expected magic number.")


# TODO the file format I found in greengenes97/greengenes97.db differs from
# what Gabe described on the call. The file I have appears to list reference
# sequence ID and the number of occurrences on each line (the counts are
# sorted):
#
# <ref-seq-id><tab><count>
#
# Is the implementation below the correct validation?
class NinjaReplicateMapFormat(model.TextFileFormat):
    def _validate_(self, level):
        with self.open() as fh:
            if level == 'min':
                # Up to 20 lines
                file_ = zip(range(1, 21), fh)
            else:  # level == 'max'
                # All lines
                file_ = enumerate(fh, start=1)

            ids = set()
            for line_num, line in file_:
                try:
                    id, count = line.rstrip('\n').split('\t')
                except ValueError:
                    raise ValidationError(
                        "Invalid format on line %d. Each line must consist "
                        "of a reference sequence ID and its count separated "
                        "by a tab character." % line_num)

                if id in ids:
                    raise ValidationError(
                        "Encountered duplicate reference sequence ID on line "
                        "%d: %s" % (line_num, id))
                else:
                    ids.add(id)

                try:
                    int(count)
                except ValueError:
                    raise ValidationError(
                        "Line %d does not contain an integer as its second "
                        "field: %s" % (line_num, count))


class NinjaOpsDBDirFmt(model.DirectoryFormat):
    # NOTE: `db` is used as a placeholder prefix -- NINJA-OPS doesn't care
    # what the prefix is, just that it's constant. The prefix must be used as
    # the enclosing directory name, as well as the prefix of each filename
    # within the directory.
    index1 = model.File('db.1.bt2', format=Bowtie2IndexFormat)
    index2 = model.File('db.2.bt2', format=Bowtie2IndexFormat)
    index3 = model.File('db.3.bt2', format=Bowtie2IndexFormat)
    index4 = model.File('db.4.bt2', format=Bowtie2IndexFormat)
    rev_index1 = model.File('db.rev.1.bt2', format=Bowtie2IndexFormat)
    rev_index2 = model.File('db.rev.2.bt2', format=Bowtie2IndexFormat)

    replicate_map = model.File('db.db', format=NinjaReplicateMapFormat)

    # TODO does the name `sequences` make sense or is there something more
    # descriptive?
    sequences = model.File('db.tcf', format=TerrificCompressedFormat)

    # TODO is there any additional validation that needs to happen on the
    # directory format that isn't taken care of by the individual FileFormat
    # classes above?
    def _validate_(self, level):
        pass
