import csv 
import re
import array
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# buat stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

kumpulan_kata = []

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
        #stemmer     
        kata = stemmer.stem(lower_case)
        # split jadi perkata
        kumpulan_kata.append([idx,kata])

    print(*kumpulan_kata,sep='\n')
