# Place code below to do the analysis part of the assignment.

# opens up your cleaned up data file, `clean_data.csv` and imports it using Python's `csv` module
import csv
import statistics
raw_data = open('data/clean_data.csv', 'r', encoding='utf_8')
csv_reader = csv.DictReader(raw_data)
count0 = []
count1=[]
count2=[]
count3=[]
count4=[]
count5=[]
count6=[]
count7=[]
count8=[]
count9=[]
count10=[]
count11=[]
count12=[]
count13=[]
count14=[]

for line in csv_reader:
    # 1880 to 1889
    if int(line['Year']) <= 1889:
        if '.' in line['J-D']:
            count0 += [float(line['J-D'])]
    # 1890 to 1899
    elif int(line['Year']) <= 1899 and int(line['Year']) >= 1890:
        if '.' in line['J-D']:
            count1 += [float(line['J-D'])]
    # 1900 to 1909
    elif int(line['Year']) <= 1909 and int(line['Year']) >= 1900:
        if '.' in line['J-D']:            
            count2 += [float(line['J-D'])]
    # 1910 to 1919
    elif int(line['Year']) <= 1919 and int(line['Year']) >= 1910:
        if '.' in line['J-D']:
            count3 += [float(line['J-D'])]
    # 1920 to 1929
    elif int(line['Year']) <= 1929 and int(line['Year']) >= 1920:
        if '.' in line['J-D']:
            count4 += [float(line['J-D'])] 
    # 1930 to 1939
    elif int(line['Year']) <= 1939 and int(line['Year']) >= 1930:
        if '.' in line['J-D']:
            count5 += [float(line['J-D'])]
    # 1940 to 1949
    elif int(line['Year']) <= 1949 and int(line['Year']) >= 1940:
        if '.' in line['J-D']:
            count6 += [float(line['J-D'])]
    # 1950 to 1959
    elif int(line['Year']) <= 1959 and int(line['Year']) >= 1950:
        if '.' in line['J-D']:
            count7 += [float(line['J-D'])]
    # 1960 to 1969
    elif int(line['Year']) <= 1969 and int(line['Year']) >= 1960:
        if '.' in line['J-D']:
            count8 += [float(line['J-D'])]
    # 1970 to 1979
    elif int(line['Year']) <= 1979 and int(line['Year']) >= 1970:
        if '.' in line['J-D']:
            count9 += [float(line['J-D'])]
    # 1980 to 1989
    elif int(line['Year']) <= 1989 and int(line['Year']) >= 1980:
        if '.' in line['J-D']:
            count10 += [float(line['J-D'])]
    # 1990 to 1999
    elif int(line['Year']) <= 1999 and int(line['Year']) >= 1990:
        if '.' in line['J-D']:
            count11 += [float(line['J-D'])]
    # 2000 to 2009
    elif int(line['Year']) <= 2009 and int(line['Year']) >= 2000:
        if '.' in line['J-D']:
            count12 += [float(line['J-D'])]
    # 2010 to 2019
    elif int(line['Year']) <= 2019 and int(line['Year']) >= 2010:
        if '.' in line['J-D']:
            count13 += [float(line['J-D'])]
    # 2020+
    elif int(line['Year']) >= 2020:
        if '.' in line['J-D']:
            count14 += [float(line['J-D'])]
  
avg_anom0 = statistics.mean(count0)
print(f'1880 to 1889: {avg_anom0}')
avg_anom1 = statistics.mean(count1)
print(f'1890 to 1899: {avg_anom1}')
avg_anom2 = statistics.mean(count2)
print(f'1900 to 1909: {avg_anom2}')
avg_anom3 = statistics.mean(count3)
print(f'1910 to 1919: {avg_anom3}')
avg_anom4 = statistics.mean(count4)
print(f'1920 to 1929: {avg_anom4}')
avg_anom5 = statistics.mean(count5)
print(f'1930 to 1939: {avg_anom5}')
avg_anom6 = statistics.mean(count6)
print(f'1940 to 1949: {avg_anom6}')
avg_anom7 = statistics.mean(count7)
print(f'1950 to 1959: {avg_anom7}')
avg_anom8 = statistics.mean(count8)
print(f'1960 to 1969: {avg_anom8}')
avg_anom9 = statistics.mean(count9)
print(f'1970 to 1979: {avg_anom9}')
avg_anom10 = statistics.mean(count10)
print(f'1980 to 1989: {avg_anom10}')
avg_anom11 = statistics.mean(count11)
print(f'1990 to 1999: {avg_anom11}')
avg_anom12 = statistics.mean(count12)
print(f'2000 to 2009: {avg_anom12}')
avg_anom13 = statistics.mean(count13)
print(f'2010 to 2019: {avg_anom13}')
avg_anom14 = statistics.mean(count14)
print(f'+2020: {avg_anom14}')