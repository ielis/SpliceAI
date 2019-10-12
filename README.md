## SpliceAI: A deep learning-based tool to identify splice variants
[![Downloads](https://pepy.tech/badge/spliceai)](https://pepy.tech/project/spliceai)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This package annotates genetic variants with their predicted effect on splicing, as described in [Jaganathan *et al*, Cell 2019 in press](https://doi.org/10.1016/j.cell.2018.12.015).

**Update**: SpliceAI annotations for all SNVs, 1-base insertions, and 1-4 base deletions within genes are available [here](https://basespace.illumina.com/s/5u6ThOblecrh) for download.

### Installation
The simplest way to install SpliceAI is through pip or conda:
```sh
pip install spliceai
# or
conda install -c bioconda spliceai
```

Alternately, SpliceAI can be installed from the [github repository](https://github.com/Illumina/SpliceAI.git):
```sh
git clone https://github.com/Illumina/SpliceAI.git
cd SpliceAI
python setup.py install
```

SpliceAI requires [tensorflow](https://www.tensorflow.org/install/)>=1.2.0, which is best installed separately via pip: `pip install tensorflow`. See the TensorFlow website for other installation options.

### Usage
SpliceAI can be run from the command line:
```sh
spliceai -I input.vcf -O output.vcf -R genome.fa -A grch37
# or you can pipe the input and output VCFs
cat input.vcf | spliceai -R genome.fa -A grch37 > output.vcf
```

Required parameters:
 - ```-I```: Input VCF with variants of interest.
 - ```-O```: Output VCF with SpliceAI predictions `SpliceAI=ALLELE|SYMBOL|DS_AG|DS_AL|DS_DG|DS_DL|DP_AG|DP_AL|DP_DG|DP_DL` included in the INFO column (see table below for details). Only SNVs and simple INDELs (REF or ALT is a single base) within genes are annotated. Variants in multiple genes have separate predictions for each gene.
 - ```-R```: Reference genome fasta file ([GRCh37/hg19](http://hgdownload.cse.ucsc.edu/goldenPath/hg19/bigZips/hg19.fa.gz), [GRCh38/hg38](http://hgdownload.cse.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.gz)).
 - ```-A```: Gene annotation file. Can instead provide `grch37` or `grch38` to use GENCODE V24 canonical annotation files included with the package. To create custom gene annotation files, use `spliceai/annotations/grch37.txt` in repository as template.

Optional parameters:
 - ```-D```: Maximum distance between the variant and gained/lost splice site (default: 50).
 - ```-M```: Mask scores representing annotated acceptor/donor gain and unannotated acceptor/donor loss (default: False).

Details of SpliceAI INFO field:

|    ID    | Description |
| -------- | ----------- |
|  ALLELE  | Alternate allele |
|  SYMBOL  | Gene symbol |
|  DS_AG   | Delta score (acceptor gain) |
|  DS_AL   | Delta score (acceptor loss) |
|  DS_DG   | Delta score (donor gain) |
|  DS_DL   | Delta score (donor loss) |
|  DP_AG   | Delta position (acceptor gain) |
|  DP_AL   | Delta position (acceptor loss) |
|  DP_DG   | Delta position (donor gain) |
|  DP_DL   | Delta position (donor loss) |

**Delta score** of a variant ranges from 0 to 1, and can be interpreted as the probability of the variant being splice-altering. In the paper, a detailed characterization is provided for 0.2 (high recall/likely pathogenic), 0.5 (recommended/pathogenic), and 0.8 (high precision/pathogenic) cutoffs. **Delta position** conveys information about the location where splicing changes relative to the variant position (positive values are downstream of the variant, negative values are upstream).

### Examples
A sample input file and the corresponding output file can be found at `examples/input.vcf` and `examples/output.vcf` respectively (`grch37` annotation). The output `SpliceAI=T|RYR1|0.00|0.00|0.91|0.08|-28|-46|-2|-31` for the variant `19:38958362 C>T` can be interpreted as follows:
* The probability that the position `19:38958360` is used as a splice donor increases by `0.91`.
* The probability that the position `19:38958331` is used as a splice donor decreases by `0.08`.

### Contact
Kishore Jaganathan: kishorejaganathan@gmail.com
