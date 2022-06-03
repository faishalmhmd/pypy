import csv 

with open('ulasan_tiket_com.csv','r') as data : 
    ulasan = csv.reader(data)
    for data in ulasan:
        # hapus nomor
        remove_string = ''.join(filter(lambda item: not item.isdigit(), data[0]))
        # hapus simbol (baru ;)
        remove_char = remove_string.replace(';','')
        # ubah ke non-kapital
        lower_case = remove_char.lower()
        print(lower_case)