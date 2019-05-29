import sys
import car_create, car_remove, decrease_price, car_average

if sys.argv[1] == "-l":
    rows = car_create.caradd()
    for i in rows:
        print(i)

elif sys.argv[1] == "-r":
    rows = car_remove.carremove()
    for i in rows:
        print(i)

elif sys.argv[1] == "-d":
    rows = decrease_price.decreaseprice()
    for i in rows:
        print(i)

elif sys.argv[1] == "-avg":
    rows = car_average.caraverage()
    for i in rows:
        print(i)