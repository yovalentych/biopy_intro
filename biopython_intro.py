from Bio.SeqUtils import MeltingTemp
from Bio.Seq import Seq
import math

seq = "ACCTACGTCGACTCA"
seq2 = "TTTCTTCGCATCGATCGC"

print(math.ceil(MeltingTemp.Tm_GC(seq)))

print(f'Res: {Seq(seq).reverse_complement()}')
