import csv 

with open('ulasan_tiket_com.csv','r') as data : 
    ulasan = csv.reader(data)
    for data in ulasan:
        print(data[0])