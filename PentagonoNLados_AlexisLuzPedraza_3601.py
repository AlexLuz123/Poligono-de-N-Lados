import matplotlib.pyplot as plt

def algoritmoDDA(lados):
    if lados == 3:
        x2 = 5
        y2 = 0
        x3 = 15
        y3 = 0
        xn = x2
        yn = y2
        x4 = 10
        y4 = 10
        x = -1

        dx = abs(x3 - x2)
        dy = abs(y3 - y2)
        
        if dx > dy:
            steps = dx
        else:
            steps = dy

        xinc = dx / steps
        yinc = dy / steps

        for i in range(x, steps):
            plt.plot(round(x2), round(y2), marker=".", color="blue")
            print(x2,",",y2)
            x2 = x2 + xinc
            y2 = y2 + yinc

        
        dx = abs(x4 - xn)
        dy = abs(y4 - yn)
        
        if dx > dy:
            steps = dx
        else:
            steps = dy

        xinc = dx / steps
        yinc = dy / steps

        for i in range(x, steps):
            plt.plot(round(xn), round(yn), marker=".", color="blue")
            print(xn,",",yn)
            xn = xn + xinc
            yn = yn + yinc


        dx = abs(x4 - x3)
        dy = abs(y4 - y3)
        
        if dx > dy:
            steps = dx
        else:
            steps = dy

        xinc = dx / steps
        yinc = dy / steps

        for i in range(x, steps):
            plt.plot(round(x3), round(y3), marker=".", color="blue")
            print(x3,",",y3)
            x3 = x3 - xinc
            y3 = y3 + yinc
     
        plt.show()

    elif lados == 4:
            x1 = 5
            y1 = 5
            x2 = 10
            y2 = 0
            x3 = x2
            y3 = y1
            x4 = x1
            y4 = y2
            x5 = x1
            y5 = y2
            x = -1

            dx = abs(x2 - x5)
            dy = abs(y2 - y5)
            
            if dx > dy:
                steps = dx
            else:
                steps = dy

            xinc = dx / steps
            yinc = dy / steps

            for i in range(x, steps):
                plt.plot(round(x5), round(y5), marker=".", color="blue")
                print(x5,",",y5)
                x5 = x5 + xinc
                y5 = y5 + yinc

            
            dx = abs(x3 - x2)
            dy = abs(y3 - y2)
            
            if dx > dy:
                steps = dx
            else:
                steps = dy

            xinc = dx / steps
            yinc = dy / steps

            for i in range(x, steps):
                plt.plot(round(x2), round(y2), marker=".", color="blue")
                print(x2,",",y2)
                x2 = x2 + xinc
                y2 = y2 + yinc


            dx = abs(x1 - x4)
            dy = abs(y1 - y4)
            
            if dx > dy:
                steps = dx
            else:
                steps = dy

            xinc = dx / steps
            yinc = dy / steps

            for i in range(x, steps):
                plt.plot(round(x4), round(y4), marker=".", color="blue")
                print(x4,",",y4)
                x4 = x4 + xinc
                y4 = y4 + yinc


            dx = abs(x3 - x1)
            dy = abs(y3 - y1)
            
            if dx > dy:
                steps = dx
            else:
                steps = dy

            xinc = dx / steps
            yinc = dy / steps

            for i in range(x, steps):
                plt.plot(round(x1), round(y1), marker=".", color="blue")
                print(x1,",",y1)
                x1 = x1 + xinc
                y1 = y1 + yinc
                
            plt.show()

    else:
        print("\nEse tipo de figura no esta")

def algoritmoBresenhams(lados):
    if lados == 3:
        x2 = 5
        y2 = 0
        x3 = 15
        y3 = 0
        x4 = 10
        y4 = 10
        x = x2
        y = y2
        xn = x2
        yn = y2
        xn1 = x3
        yn1 = y3
        
        dx = abs(x3 - x2)
        dy = abs(y3 - y2)
        p = (2 * dy) - dx
        x3 = x3 + 1

        for i in range(x, x3):
            plt.plot(round(x), round(y), marker=".", color="blue")
            print(x,",",y)
            x = x + 1
            if p < 0:
                p = p + (2 * dy)
            else:
                p = p + (2 * dy) - (2 * dx)
                y = y + 1


        dx = abs(x4 - x2)
        dy = abs(y4 - y2)
        p = (2 * dy) - dx
        x4 = x4 + 1

        for i in range(xn, x4):
            plt.plot(round(xn), round(yn), marker=".", color="blue")
            print(xn,",",yn)
            xn = xn + 1
            if p < 0:
                p = p + (2 * dy)
            else:
                p = p + (2 * dy) - (2 * dx)
                yn = yn + 1


        dx = abs(x4 - x3)
        dy = abs(y4 - y3)
        p = (2 * dy) - dx
        x4 = x4 - 1

        for i in range(x4, xn1):
            plt.plot(round(xn1), round(yn1), marker=".", color="blue")
            print(xn1,",",yn1)
            xn1 = xn1 - 1
            if p < 0:
                p = p + (2 * dy)
            else:
                p = p + (2 * dy) - (2 * dx)
                yn1 = yn1 + 1
            
        plt.show()    

    elif lados == 4:
            x1 = 5
            y1 = 5
            x2 = 10
            y2 = 0
            x = x1
            y = y1
            x3 = x2
            y3 = y1
            x4 = x1
            y4 = y2
            xn = x2
            yn = y2
            xn1 = x4
            yn1 = y4

            dx = abs(x3 - x1)
            dy = abs(y3 - y1)
            p = (2 * dy) - dx
            x3 = x3 + 1

            for i in range(x, x3):
                plt.plot(round(x), round(y), marker=".", color="blue")
                print(x,",",y)
                x = x + 1
                if p < 0:
                    p = p + (2 * dy)
                else:
                    p = p + (2 * dy) - (2 * dx)
                    y = y + 1
                

            dx = abs(x2 - x4)
            dy = abs(y2 - y4)
            p = (2 * dy) - dx
            x2 = x2 + 1

            for i in range(x4, x2):
                plt.plot(round(x4), round(y4), marker=".", color="blue")
                print(x4,",",y4)
                x4 = x4 + 1
                if p < 0:
                    p = p + (2 * dy)
                else:
                    p = p + (2 * dy) - (2 * dx)
                    y4 = y4 + 1


            dx = abs(x3 - x2)
            dy = abs(y3 - y2)
            p = (2 * dy) - dx
            y3 = y3 + 1

            for i in range(yn, y3):
                plt.plot(round(xn), round(yn), marker=".", color="blue")
                print(xn,",",yn)
                if p < 0:
                    p = p + (2 * dy)
                else:
                    p = p + (2 * dy) - (2 * dx)
                    yn = yn + 1


            dx = abs(x1 - x4)
            dy = abs(y1 - y4)
            p = (2 * dy) - dx
            y1 = y1 + 1

            for i in range(yn1, y1):
                plt.plot(round(xn1), round(yn1), marker=".", color="blue")
                print(xn1,",",yn1)
                if p < 0:
                    p = p + (2 * dy)
                else:
                    p = p + (2 * dy) - (2 * dx)
                    yn1 = yn1 + 1

            plt.show()

    else:
        print("\nEse tipo de figura no esta")

if __name__ == '__main__':
    tipo = int(input("1.DDA \n2.Bresenhams \nSelecciona el algoritmo con el cual quieres trabajar: "))
    if tipo == 1:
        lados = int(input("Ingresa la cantidad de lados de la figura: "))
        algoritmoDDA(lados)
        print("\nUtilize DDA\n")
    elif tipo == 2:
        lados = int(input("Ingresa la cantidad de lados de la figura: "))
        algoritmoBresenhams(lados)
        print("\nUtilize Bresenhams\n")
    else:
        print("\nEse algoritmo no existe\n")