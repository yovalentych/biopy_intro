from Bio.SeqUtils import MeltingTemp
from Bio.Seq import Seq
import math

seq = "ACCTACGTCGACTCA"
seq2 = "TTTCTTCGCATCGATCGC"
seq3 = "TACCACGCGCTCGTCT"
print(math.ceil(MeltingTemp.Tm_GC(seq)))

print(Seq(seq).reverse_complement())
