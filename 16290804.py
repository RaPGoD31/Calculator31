from graphics import *

def Yasmin():
    yasmin = GraphWin("Calculator", 600, 600)
    yasmin.setCoords(0.0,0.0,6.0,6.0)
    result = Entry(Point(3,5.50),20)
    start = Text(Point(3,5.9),"Calculator")
    start.draw(yasmin)
    num = "0"
    result.setText(num)
    result.draw(yasmin)
    leia = []
    layla = []
    x=3
    y=3
    j=9
    i=0
    k=0
    z=0
    while j>=0:
        leia.append(Point(x,y))
        layla.append((Point(x+1.5,y+1)))
        btn = Rectangle(Point(x,y),Point(x+1.5,y+1))
        btn.draw(yasmin)
        num = Text(Point(x+0.75,y+0.5),str(j))
        num.draw(yasmin)
        x -= 1.5
        j -= 1
        i += 1
        k += 1
        z += 1
        if i==3:
            x = 3
            y = 2
            i = 0
        if k==6:
            x = 3
            y = 1
            k = 0
        if z==10:
            x=0
            y=0
            leia[z-1] =  (Point(x, y))
            layla[z-1] = (Point(x+3, y+1))
            btn = Rectangle(Point(x,y),Point(x+3,y+1))
            btn.draw(yasmin)
            num.undraw()
            num = Text(Point(x+1.5,y+0.5),str(j+1))
            num.draw(yasmin)
            z = 0

    ops = ["AC","+/-","%","/","x","-","+","**","="]
    j = 0
    x = 0
    y = 4
    i = 0
    while j<len(ops):
        leia.append(Point(x,y))
        layla.append(Point(x+1.5,y+1))
        btn = Rectangle(Point(x,y),Point(x+1.5,y+1))
        btn.draw(yasmin)
        num = Text(Point(x+0.75,y+0.5),str(ops[j]))
        num.draw(yasmin)
        x += 1.5
        i += 1
        j += 1
        if i==4:
            x = 4.5
            y = 3
        if i==5:
            x = 4.5
            y = 2
        if i==6:
            x = 4.5
            y = 1
        if i==7:
            x=3
            y=0
            i=0
    numa = "0"
    numb = ""
    numv = ""
    clk = True
    while clk:
        try:
            ab = yasmin.getMouse()
            if (ab.x > leia[0].x and ab.x < layla[0].x and ab.y > leia[0].y and ab.y < layla[0].y):
                if numa[-1]=="=":
                    numv = ""
                    numa += "9"
                    numv += "9"
                    numb += "9"
                    result.setText(numb)
                else:
                    numa += "9"
                    numv += "9"
                    numb += "9"
                    result.setText(numb)
            if (ab.x > leia[1].x and ab.x < layla[1].x and ab.y > leia[1].y and ab.y < layla[1].y):
                if numa[-1] == "=":
                    numv = ""
                    numa += "8"
                    numv += "8"
                    numb += "8"
                    result.setText(numb)
                else:
                    numa += "8"
                    numv += "8"
                    numb += "8"
                    result.setText(numb)
            if (ab.x > leia[2].x and ab.x < layla[2].x and ab.y > leia[2].y and ab.y < layla[2].y):
                if numa[-1] == "=":
                    numv = ""
                    numa += "7"
                    numv += "7"
                    numb += "7"
                    result.setText(numb)
                else:
                    numa += "7"
                    numv += "7"
                    numb += "7"
                    result.setText(numb)
            if (ab.x > leia[3].x and ab.x < layla[3].x and ab.y > leia[3].y and ab.y < layla[3].y):
                if numa[-1] == "=":
                    numv = ""
                    numa += "6"
                    numv += "6"
                    numb += "6"
                    result.setText(numb)
                else:
                    numa += "6"
                    numv += "6"
                    numb += "6"
                    result.setText(numb)
            if (ab.x > leia[4].x and ab.x < layla[4].x and ab.y > leia[4].y and ab.y < layla[4].y):
                if numa[-1] == "=":
                    numv = ""
                    numa += "5"
                    numv += "5"
                    numb += "5"
                    result.setText(numb)
                else:
                    numa += "5"
                    numv += "5"
                    numb += "5"
                    result.setText(numb)
            if (ab.x > leia[5].x and ab.x < layla[5].x and ab.y > leia[5].y and ab.y < layla[5].y):
                if numa[-1] == "=":
                    numv = ""
                    numa += "4"
                    numv += "4"
                    numb += "4"
                    result.setText(numb)
                else:
                    numa += "4"
                    numv += "4"
                    numb += "4"
                    result.setText(numb)
            if (ab.x > leia[6].x and ab.x < layla[6].x and ab.y > leia[6].y and ab.y < layla[6].y):
                if numa[-1] == "=":
                    numv = ""
                    numa += "3"
                    numv += "3"
                    numb += "3"
                    result.setText(numb)
                else:
                    numa += "3"
                    numv += "3"
                    numb += "3"
                    result.setText(numb)
            if (ab.x > leia[7].x and ab.x < layla[7].x and ab.y > leia[7].y and ab.y < layla[7].y):
                if numa[-1] == "=":
                    numv = ""
                    numa += "2"
                    numv += "2"
                    numb += "2"
                    result.setText(numb)
                else:
                    numa += "2"
                    numv += "2"
                    numb += "2"
                    result.setText(numb)
            if (ab.x > leia[8].x and ab.x < layla[8].x and ab.y > leia[8].y and ab.y < layla[8].y):
                if numa[-1] == "=":
                    numv = ""
                    numa += "1"
                    numv += "1"
                    numb += "1"
                    result.setText(numb)
                else:
                    numa += "1"
                    numv += "1"
                    numb += "1"
                    result.setText(numb)
            if (ab.x > leia[9].x and ab.x < layla[9].x and ab.y > leia[9].y and ab.y < layla[9].y):
                if numb == "":
                    numb = "0"
                    result.setText(numb)
                    numb = ""
                    if numa[-1] == "=":
                        numv = ""
                        numa += "0"
                        numv += "0"
                        numb += "0"
                        result.setText(numb)
                else:
                    if numa[-1] == "=":
                        numv = ""
                        numa += "0"
                        numv += "0"
                        numb += "0"
                        result.setText(numb)
                    else:
                        numa += "0"
                        numv += "0"
                        numb += "0"
                        result.setText(numb)
            if (ab.x > leia[10].x and ab.x < layla[10].x and ab.y > leia[10].y and ab.y < layla[10].y):
                numa = "0"
                numv = ""
                numb = "0"
                result.setText(numb)
                numb = ""
            if (ab.x > leia[11].x and ab.x < layla[11].x and ab.y > leia[11].y and ab.y < layla[11].y):
                try:
                    if numb=="":
                        if numa[-1] == "=":
                            numv = "-" + str(eval(numv))
                            numb = str(eval(numv))
                            result.setText(numb)
                            numb = str(eval(numv))
                        else:
                            numv = ""
                            numb = "0"
                            result.setText(numb)
                            numb = ""

                    elif numb[0] == "-":
                        result.setText(numb)
                    else:
                        numv = "-" + numv
                        numb = "-" + numb
                        result.setText(numb)
                        if "+" or "-" or "x" or "**" or "/" or "%" in numv[1:]:
                            k = 0
                            for j in numv[1:]:
                                if j=="+" or j=="-" or j=="x" or j=="**" or j=="/" or j=="%":
                                    numv = numv[1:k+2] + "-" + numv[k+2:]
                                else:
                                    k+=1
                    numa += "-"
                except SyntaxError:
                    numv = "0"
                    numb = str(eval(numv))
                    result.setText(numb)
                    numv = ""
                    numb = ""
            if (ab.x > leia[12].x and ab.x < layla[12].x and ab.y > leia[12].y and ab.y < layla[12].y):
                if "+" or "-" or "x" or "**" or "/" or "%" in numv:
                    numa += "%"
                    try:
                        if float(eval(numv)) == int(eval(numv)):
                            numb = int(eval(numv))
                            result.setText(numb)
                            numv = str(numb) + "%"
                            numb = ""
                        else:
                            numb = str(eval(numv))
                            result.setText(numb)
                            numv = str(eval(numv)) + "%"
                            numb = ""
                    except SyntaxError:
                        numv = "0"
                        numb = str(eval(numv))
                        result.setText(numb)
                        numv = ""
                        numb = ""
                else:
                    numv += "%"
                    numb = str(eval(numb))
                    result.setText(numb)
                    numb = ""
            if (ab.x > leia[13].x and ab.x < layla[13].x and ab.y > leia[13].y and ab.y < layla[13].y):
                if "+" or "-" or "x" or "**" or "/" or "%" in numv:
                    numa += "/"
                    try:
                        if float(eval(numv)) == int(eval(numv)):
                            numb = int(eval(numv))
                            result.setText(numb)
                            numv = str(numb) + "/"
                            numb = ""
                        else:
                            numb = str(eval(numv))
                            result.setText(numb)
                            numv = str(eval(numv)) + "/"
                            numb = ""
                    except SyntaxError:
                        numv = "0"
                        numb = str(eval(numv))
                        result.setText(numb)
                        numv = ""
                        numb = ""
                else:
                    numv += "/"
                    numb = str(eval(numb))
                    result.setText(numb)
                    numb = ""
            if (ab.x > leia[14].x and ab.x < layla[14].x and ab.y > leia[14].y and ab.y < layla[14].y):
                if "+" or "-" or "x" or "**" or "/" or "%" in numv:
                    numa += "*"
                    try:
                        if float(eval(numv)) == int(eval(numv)):
                            numb = int(eval(numv))
                            result.setText(numb)
                            numv = str(numb) + "*"
                            numb = ""
                        else:
                            numb = str(eval(numv))
                            result.setText(numb)
                            numv = str(eval(numv)) + "*"
                            numb = ""
                    except SyntaxError:
                        numv = "0"
                        numb = str(eval(numv))
                        result.setText(numb)
                        numv = ""
                        numb = ""
                else:
                    numv += "*"
                    numb = str(eval(numb))
                    result.setText(numb)
                    numb = ""
            if (ab.x > leia[15].x and ab.x < layla[15].x and ab.y > leia[15].y and ab.y < layla[15].y):
                if "+" or "-" or "x" or "**" or "/" or "%" in numv:
                    numa += "-"
                    try:
                        if float(eval(numv)) == int(eval(numv)):
                            numb = int(eval(numv))
                            result.setText(numb)
                            numv = str(numb) + "-"
                            numb = ""
                        else:
                            numb = str(eval(numv))
                            result.setText(numb)
                            numv = str(eval(numv)) + "-"
                            numb = ""
                    except SyntaxError:
                        numv = "0"
                        numb = str(eval(numv))
                        result.setText(numb)
                        numv = ""
                        numb = ""
                else:
                    numv += "-"
                    numb = str(eval(numb))
                    result.setText(numb)
                    numb = ""
            if (ab.x > leia[16].x and ab.x < layla[16].x and ab.y > leia[16].y and ab.y < layla[16].y):
                if "+" or "-" or "x" or "**" or "/" or "%" in numv:
                    numa += "+"
                    try:
                        if float(eval(numv)) == int(eval(numv)):
                            numb = int(eval(numv))
                            result.setText(numb)
                            numv = str(numb) + "+"
                            numb = ""
                        else:
                            numb = str(eval(numv))
                            result.setText(numb)
                            numv = str(eval(numv)) + "+"
                            numb = ""
                    except SyntaxError:
                        numv = "0"
                        numb = str(eval(numv))
                        result.setText(numb)
                        numv = ""
                        numb = ""
                else:
                    numv += "+"
                    numb = str(eval(numb))
                    result.setText(numb)
                    numb = ""
            if (ab.x > leia[17].x and ab.x < layla[17].x and ab.y > leia[17].y and ab.y < layla[17].y):
                if "+" or "-" or "x" or "**" or "/" or "%" in numv:
                    numa += "**"
                    try:
                        if float(eval(numv)) == int(eval(numv)):
                            numb = int(eval(numv))
                            result.setText(numb)
                            numv = str(numb) + "**"
                            numb = ""
                        else:
                            numb = str(eval(numv))
                            result.setText(numb)
                            numv = str(eval(numv)) + "**"
                            numb = ""
                    except SyntaxError:
                        numv = "0"
                        numb = str(eval(numv))
                        result.setText(numb)
                        numv = ""
                        numb = ""
                else:
                    numv += "**"
                    numb = str(eval(numb))
                    result.setText(numb)
                    numb = ""
            if (ab.x > leia[18].x and ab.x < layla[18].x and ab.y > leia[18].y and ab.y < layla[18].y):
                try:
                    numa += "="
                    if float(eval(numv)) == int(float(eval(numv))):
                        if "-" and "**" in numv:
                            if numa[-2]=="-":
                                if int(numv[-1])%2==0:
                                    numb = abs(int(eval(numv)))
                                    z = 1 / numb
                                    numb = str(z)
                                    numv = numb
                                    result.setText(numb)
                                    numb = ""
                                else:
                                    numb = abs(int(eval(numv)))
                                    if numv[1]=="-" and numv[0]=="-":
                                        z =  -1 / numb
                                    else:
                                        z = 1/numb
                                    numb = str(z)
                                    numv = numb
                                    result.setText(numb)
                                    numb = ""
                            else:
                                a = str(numv)
                                b = a[-1]
                                if int(b)%2==0:
                                    numb = abs(int(eval(numv)))
                                    numv = str(numb)
                                    result.setText(numb)
                                    numb = ""
                                else:
                                    numb = int(eval(numv))
                                    numv = str(numb)
                                    result.setText(numb)
                                    numb = ""
                        else:
                            numb = int(eval(numv))
                            numv = str(numb)
                            result.setText(numb)
                            numb = ""
                    else:
                        numb = str(eval(numv))
                        numv = str(eval(numv))
                        result.setText(numb)
                        numb = ""
                except SyntaxError:
                    numv = "0"
                    numb = str(eval(numv))
                    result.setText(numb)
                    numv = ""
                    numb = ""
                continue
            if (ab.x > 5.99 and ab.y > 5.98):
                yasmin.close()
                break
        except GraphicsError:
            yasmin.close()
            break

if __name__ == '__main__':
    Yasmin()
