import csv
import numpy as np
import re
from collections import Counter
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()
# array buat nampung kumpulan kata
kumpulan_kata = []
row = []
kumpulan_kata_fix = []

with open('ulasan_tiket_com.csv','r') as data : 
    ulasan = csv.reader(data)
    for idx,data in enumerate(ulasan):
        # hapus nomor
        pattern = r'[0-9]'
        remove_string = re.sub(pattern,'',data[0])        
        # hapus simbol (baru ;)
        remove_char = remove_string.replace(';','')
        # ubah ke non-kapital
        lower_case = remove_char.lower()
        #  stemmer     
        kata = stemmer.stem(lower_case)
        # split jadi perkata
        split_kata = kata.split()
        # tampung kedalam array
        kumpulan_kata.append(split_kata)

    # buat benerin kata
    def words(text): return re.findall(r'\w+', text.lower())

    WORDS = Counter(words(open('typo.txt').read()))

    def P(word, N=sum(WORDS.values())):
        # "Probability of `word`."
        return WORDS[word] / N

    def correction(word):
        # "Most probable spelling correction for word."
        return max(candidates(word), key=P)

    def candidates(word):
        # "Generate possible spelling corrections for word."
        return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

    def known(words):
        # "The subset of `words` that appear in the dictionary of WORDS."
        return set(w for w in words if w in WORDS)

    def edits1(word):
        # "All edits that are one edit away from `word`."
        letters    = 'abcdefghijklmnopqrstuvwxyz'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)] # [('', 'kemarin'), ('k', 'emarin'), ('ke', 'marin'), dst]
        deletes    = [L + R[1:]               for L, R in splits if R] # ['emarin', 'kmarin', 'kearin', dst]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1] # ['ekmarin', 'kmearin', 'keamrin', dst]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters] # ['aemarin', 'bemarin', 'cemarin', dst]
        inserts    = [L + c + R               for L, R in splits for c in letters] # ['akemarin', 'bkemarin', 'ckemarin', dst]
        return set(deletes + transposes + replaces + inserts)

    def edits2(word):
        # "All edits that are two edits away from `word`."
        return (e2 for e1 in edits1(word) for e2 in edits1(e1))

    # np_kumpulan_kata =  np.array(kumpulan_kata)
    # print(np_kumpulan_kata[1][1])
    # for data in kumpulan_kata:
    #     print(data)
    # print(kumpulan_kata[1][0])
    for index,data in enumerate(kumpulan_kata):
        for idx,dt in enumerate(data):
            # print(correction(dt),end=' ')
            row.append(dt)
        print()      
        kumpulan_kata_fix.append(row)
        row = []
    print(*kumpulan_kata_fix,sep='\n')          