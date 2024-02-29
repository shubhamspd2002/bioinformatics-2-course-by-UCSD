from collections import defaultdict

def DeBruijnk(k, string):
  dic = defaultdict(list)
  for i in range(len(string)-k+1):
    kmer = string[i:i+k]
    prefix = kmer[:k - 1]
    sufix = kmer[1:]
    dic[prefix].append(sufix)
  return dic

def print_adjacency_list(dic):
    r = ""
    for k, v in dic.items():
        r += k + ": " + " ".join(v) + "\n"
    return r

resultado = print_adjacency_list(DeBruijnk(4, "AAGATTCTCTAAGA"))
print(resultado)