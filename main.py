def crisscross(a,b,c,d):
    cc = (a*b)-(c*d)
    return cc

class determnt:
    def two():
        tx1 = int(input("Enter x1: "))
        ty1 = int(input("Enter y1: "))
        ta1 = int(input("Enter x1+y1: "))
        tx2 = int(input("Enter x2: "))
        ty2 = int(input("Enter y2: "))
        ta2 = int(input("Enter x2+y2: "))
        
        d2 = (tx1*ty2)-(ty1*tx2)
        d2x = (ta1*ty2)-(ty1*ta2)
        d2y = (tx1*ta2)-(ta1*tx2)

        x2 = d2x/d2
        y2 = d2y/d2

        return x2,y2
    
    def three():
        r = []
        i = 0
        while i < 9:
            num = int(input(f"enter {i+1} index of matrix: "))
            r.append(num)
            i += 1

        rx1,ry1,rz1 = r[0],r[1],r[2]
        rx2,ry2,rz2 = r[3],r[4],r[5]
        rx3,ry3,rz3 = r[6],r[7],r[8]
        ra1 = int(input("Enter x1+y1+z1: "))
        ra2 = int(input("Enter x2+y2+z2: "))
        ra3 = int(input("Enter x3+y3+z3: "))
        
        d3cc1 = crisscross(ry2,rz3,ry3,rz2)
        d3cc2 = crisscross(rx2,rz3,rx3,rz2)
        d3cc3 = crisscross(rx2,ry3,rx3,ry2)
        d3 = (rx1 * d3cc1) - (ry1 * d3cc2) + (rz1 * d3cc3)

        d3xcc1 = crisscross(ry2,rz3,ry3,rz2)
        d3xcc2 = crisscross(ra2,rz3,ra3,rz2)
        d3xcc3 = crisscross(ra2,ry3,ra3,ry2)
        d3x = (ra1 * d3xcc1) - (ry1 * d3xcc2) + (rz1 * d3xcc3)

        d3ycc1 = crisscross(ra2,rz3,ra3,rz2)
        d3ycc2 = crisscross(rx2,rz3,rx3,rz2)
        d3ycc3 = crisscross(rx2,ra3,rx3,ra2)
        d3y = (rx1 * d3ycc1) - (ra1 * d3ycc2) + (rz1 * d3ycc3)

        d3zcc1 = crisscross(ry2,ra3,ry3,ra2)
        d3zcc2 = crisscross(rx2,ra3,rx3,ra2)
        d3zcc3 = crisscross(rx2,ry3,rx3,ry2)
        d3z = (rx1 * d3zcc1) - (ry1 * d3zcc2) + (ra1 * d3zcc3)

        x3 = d3x/d3
        y3 = d3y/d3
        z3 = d3z/d3

        return x3,y3,z3


def dimn(arg):
    match arg:
        case 2:
            a2,b2 = determnt.two()
            return print("\n x=",a2,",  y=",b2)
        case 3:
            a3,b3,c3 = determnt.three()
            return print("\n x=",a3,",  y=",b3,",  z=",c3)
        case default:
            return "Wrong entry"

dim=0
while dim != 1:
    dim = int(input("\nEnter dimensions (2 or 3)(1 to exit): "))
    if dim == 2:
        dimn(2)
        continue
    elif dim == 3:
        dimn(3)
        continue
    elif dim == 1:
        break
    else:
        print("Invalid option")
