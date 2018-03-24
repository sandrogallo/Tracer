import turtle
import time


def crea_assi(w, h):
    # crea l'asse x
    turtle.pu()
    turtle.fd(-w)
    turtle.pd()
    turtle.fd(w * 2)
    # crea l'asse y
    turtle.pu()
    turtle.lt(90)
    turtle.fd(-h)
    turtle.pd()
    turtle.fd(h * 2)


def readfile():
    try:
        f = open('DataBase.txt', 'r')
        s = f.read()
        f.close()
        rows = s.split('\n')
        coor = []
        for row in rows:
            if row=="":
                continue
            fields = row.split(';')
            if len(fields) != 5:
                print('linea non corretta')
            else:
                coor.append((float(fields[0]), float(fields[1])))
                print('caricate le coordinate' + str(len(coor)))
        return coor
    except Exception as ex:
        print('ERRORE!:'+str(ex))
        return coor

def foundbounds(coor):
    min_lat = max_lat = coor[0][0]
    min_long = max_long = coor[0][1]
    for x in coor:
        if x[0] < min_lat:
            min_lat = x[0]
        elif x[0] > max_lat:
            max_lat = x[0]
        if x[1] < min_long:
            min_long = x[1]
        elif x[1] > max_long:
            max_long = x[1]
    return float(max_lat), float(min_lat), float(max_long), float(min_long)


def plot(x, y):
    try:
        turtle.pu()
        turtle.goto(x, y)
        turtle.pd()
        turtle.dot(4, "red")
    except(KeyboardInterrupt, SystemExit):
        print('Thread finished')

def converti(lat, long, width, height):
    max_lat, min_lat, max_long, min_long = foundbounds(readfile())
    print(max_lat, min_lat, max_long, min_long)
    w = (((lat - min_lat) / (max_lat - min_lat)) * width * 2) - width
    h = (((long - min_long) / (max_long - min_long)) * height * 2) - height
    plot(w, h)


def run():
    width = 400
    height = 400
    turtle.screensize(width, height)
    coor = readfile()
    for c in coor:
        try:
            converti(c[0], c[1], width, height)
        except(KeyboardInterrupt,SystemExit):
            print('Thread finished')
    turtle.exitonclick()


if __name__ == '__main__':
    run()
