# Place code below to do the munging part of this assignment.
opendata = open('data/GLB.Ts+dSST.txt', 'r', encoding='utf_8')
listlines = opendata.readlines()
# counter for index
count = -1
for line in listlines:
    count += 1
    if line[0:4] == 'Year' and 'Jan' in line:
        heading_list = line.split()
        break
heading_str = ','.join(heading_list)
# save in a new file
csvfile = open('data/clean_data.csv', 'w', encoding='utf_8')
csvfile.write(heading_str + '\n')
print(heading_str)
for line in listlines[count:]:
    if line[0] == '1' or line[0] == '2':
        dataline_list = line.split()
        counter = -1
        for x in dataline_list:
            counter += 1
            if '*' in x:
                dataline_list[counter] = ''
            elif dataline_list[0] == x:
                continue
            else:
                try:
                    integer = int(x)
                except:
                    continue
                else:
                    # Divide by 100 to get changes in degrees Celsius (deg-C)
                    # Multiply that result by 1.8(=9/5) to get changes in degrees Fahrenheit (deg-F)
                    fahrenheit = (integer/100) * 1.8
                    dataline_list[counter] = format(fahrenheit, '.1f')
        dataline_str = ','.join(dataline_list)
        csvfile.write(dataline_str + '\n')
        print(dataline_str)
csvfile.close()