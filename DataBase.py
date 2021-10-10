file=open('Data.txt','r',encoding='utf-8')
datalist=(file.readlines())
print(datalist)
for i in datalist:
    datalist[datalist.index(i)]=i.replace('\n','') #Убираю \n из списка
print(datalist)
datadict={}
file.close()
for i in datalist:
    a=i.split(':')
    datadict[a[0]]=[int(a[1]),int(a[2])] #Заполняю словарь/базу данный
print(datadict)
y='да'
while (y=='да' or y=='Да'):
    print('1 - Отсортировать по алфавиту\n'
          '2 - Отсортировать по сумме затрат в месяц\n'
          '3 - Отсортировать по количеству посещений в день\n'
          '4 - Найти клиента по имени\n'
          '5 - Добавить новых клиентов\n'
          '6 - Изменить данные\n'
          '7 - Удалить данные клиента\n'
          '8 - Записать в исходный текстовый файл')
    counter=int(input('Выбирите функцию: '))
    if counter==1:
        templist=list(datadict.keys())
        templist.sort()
        for i in templist:    # templist это временный "буферный" список, который я использую для сортировки, а потом очищаю
            print(i,':','затраты -',datadict[i][0],':','посещаемость -',datadict[i][1])
        templist=[]
        y=input('Будете делать что-то ещё? ')
    elif counter==2:
        templist=list(datadict.items())
        templist.sort(reverse=True,key=lambda i: i[1][0])
        for i in templist:
            print('Затраты -',i[1][0],':',i[0])
        templist=[]
        y = input('Будете делать что-то ещё? ')
    elif counter==3:
        templist = list(datadict.items())
        templist.sort(reverse=True,key=lambda i: i[1][1])
        for i in templist:
            print('Посещаемость -',i[1][1],':',i[0])
        templist = []
        y = input('Будете делать что-то ещё? ')
    elif counter==4:
        name=input('Введите имя клиента о котором хоиите узнать: ')
        if name in datadict:
            print(f'Его траты за месяц = {datadict[name][0]} рублей: его посещаемость = {datadict[name][1]} дней в месяц')
        else:
            print('Такого имени нет в базе данных')
        y = input('Будете делать что-то ещё? ')
    elif counter==5:
        tempname=input('Введите имя клиента: ')
        t1=int(input('Введите его затраты за месяц: '))
        t2=int(input('Введите его посещаемость за месяц: '))
        datadict[tempname]=[t1,t2]
        print("Добавление произошло успешно")
        tempname=''
        y = input('Будете делать что-то ещё? ')
    elif counter==6:
        print('1 - имя\n'
              '2 - затраты\n'
              '3 - посещаемость')
        data=int(input('Введите номер того что хотите изменить: '))
        if data==1:
            tempname=input('Введите новое имя: ')
            tempname2=input('Введите имя которое хотите заменить: ')
            if tempname2 not in datadict:
                print('Ошибка, такого имени нет в базе данных')
            else:
                datadict[tempname]=datadict[tempname2]
                del datadict[tempname2]
                print(f'Имя {tempname2} успешно заменено на {tempname}')
            tempname=''
            tempname2=''
        if data==2:
            tempname = input('Введите имя кому хотите изменить затраты: ')
            z=int(input('Введите новые затраты: '))
            if tempname not in datadict:
                print('Ошибка, такого имени нет в базе данных')
            else:
                tempz=datadict[tempname][0]
                datadict[tempname][0]=z
                print(f'Затраты {tempname} изменены с {tempz} на {z}')
            tempname=''
        if data==3:
            tempname = input('Введите имя кому хотите изменить посещаемость: ')
            p=int(input('Введите новую посещаемость: '))
            if tempname not in datadict:
                print('Ошибка, такого имени нет в базе данных')
            else:
                tempp=datadict[tempname][1]
                datadict[tempname][1]=p
                print(f'Посещаемость {tempname} изменена с {tempp} на {p}')
            tempname = ''
        y = input('Будете делать что-то ещё? ')
    elif counter==7:
        tempname=input('Введите имя того, кого хотите удалить: ')
        if tempname not in datadict:
            print('Такого человека нет в базе данных')
        else:
            del datadict[tempname]
            print(f'Информация о {tempname} удалена из базы данных')
    elif counter==8:
        file=open('Data.txt','w+',encoding='utf-8')
        file.seek(0)
        for i in datadict:
            file.write(f'{i}:{datadict[i][0]}:{datadict[i][1]}\n')
        file.close()
    else:
        print('Ошибка')