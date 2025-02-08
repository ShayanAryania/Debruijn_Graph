def rev_comp(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join(complement[base] for base in reversed(seq))

def DBgraph(kmers):
    edges = set()
    for kmer in kmers:
        for seq in [kmer, rev_comp(kmer)]:
            edges.add((seq[:-1], seq[1:]))
    return edges

def Out(edges):
    return '\n'.join(f"({src} , {dst})" for src, dst in sorted(edges))

N = int(input())
dna_strings = []
for _ in range(N):
    dna_string = input().strip()
    dna_strings.append(dna_string)

edges = DBgraph(dna_strings)
print(Out(edges))
