mark = 0 # Оценка

print ("""
          Сколько бит в одном байте
          1) 8
          2) 6
          3) 4
          4) 2
          """)
а = int(input("Ваш ответ: "))
if а == 1:
    mark = mark + 1
    print("""
          Сколько байт в одном килобайте
          1) 1000
          2) 1024
          3) 1048
          4) 256
          """)
а = int(input("Ваш ответ: "))
if а == 2:
   mark = mark + 1
print("""Компания-разработчик Windows
         1) Mikrosoft
         2) Melkosoft
         3) Cybersoft
         4) Microsoft
        """)
а = int(input("Ваш ответ: "))
if а == 4:
    mark = mark + 1

print("""Самая "яблочная" операционная система
         1) AppleOS
         2) Linux
         3) macOS
         4) FreeBSD
        """)
а = int(input("Ваш ответ: "))
if а == 3:
     mark = mark + 1

print("""Символом какой операционной системы является пингвин
         1) Linux
         2)FreeBSD
         3) OS/2
         4) Windows
        """)
a = int(input("Ваш ответ: "))

if a ==1:
    mark = mark + 1
print("Ваша оценка: ", mark)

