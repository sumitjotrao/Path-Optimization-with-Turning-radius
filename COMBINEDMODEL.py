import math as m

# Extracting node sequence
p = open("C:\Mydata\MS Thesis\My_Data.dat", 'r')

a = p.readline()
x_coord = []
y_coord = []

f = str.split(a)
#number of node points
n=int(f[0])
for a in p:
    f = str.split(a)

    x_coord.append(float(f[0]))
    y_coord.append(float(f[1]))

points = {}
for i in range(n):
    points.update({i: (x_coord[i], y_coord[i])})

#print(points)

dt=open("C:\Mydata\MS Thesis\Info_gain.dat",'r')

k1=dt.readlines()
data={}

for i in range(len(k1)):
    data.update({i:int(k1[i])})

#en is set of points of entry on a particular circle
entry=[5,6,7,8]
#ex is set of points of exit on a particular circle
exit=[1,2,3,4]


#Total Distance uper limit
D=5000

#**************Finding the inner and outer tangents********************

r=3



def outer_tangent(x1,y1,x2,y2,r):
 if (x2 - x1) == 0:
        a = 90
 else:
        a = m.degrees(m.atan((y2 - y1) / (x2 - x1)))
 if a>=0:
    theta=m.radians(a)
 else:
    theta=m.radians(180+a)


 x3=x1-r*m.sin(theta)
 y3=y1+r*m.cos(theta)

 x4=x1+r*m.sin(theta)
 y4=y1-r*m.cos(theta)

 x5=x2-r*m.sin(theta)
 y5=y2+r*m.cos(theta)

 x6=x2+r*m.sin(theta)
 y6=y2-r*m.cos(theta)
 return (x3,y3,x4,y4,x5,y5,x6,y6)

def inner_tangent(x1,y1,x2,y2,r):
 d=m.sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))
 if (x2-x1)==0:
     a=90
 else:
  a = m.degrees(m.atan((y2 - y1) / (x2 - x1)))
 if a >= 0:
     theta = m.radians(a)
 else:
     theta = m.radians(180 + a)

 if x1<=x2 and y1<=y2:
    quadrant=1
 elif x1>=x2 and y1<=y2:
    quadrant=2
 elif x1>=x2 and y1>=y2:
    quadrant=3
 else:
    quadrant=4
 alpha=m.acos(r/(d/2))
 if quadrant==1 :
  theta1=theta+alpha
  theta2=alpha-theta
 elif quadrant==3:
    theta1=theta-alpha
    theta2=m.radians(180-m.degrees(theta)-m.degrees(alpha))
 elif quadrant==4:
     theta1=m.radians(m.degrees(alpha)+180-m.degrees(theta))
     theta2=m.radians(m.degrees(alpha)-180+m.degrees(theta))
 else:
     if theta == 0:
         theta1 = m.radians(m.degrees(alpha))
         theta2 = m.radians(m.degrees(alpha))
     else:
         theta1 = m.radians(180 - m.degrees(theta) + m.degrees(alpha))
         theta2 = m.radians(m.degrees(alpha) + m.degrees(theta) - 180)
 if quadrant==1 :
    x7=x1+r*m.cos(theta1)
    y7=y1+r*m.sin(theta1)

    x8=x1+r*m.cos(theta2)
    y8=y1-r*m.sin(theta2)

    x9=x2-r*m.cos(theta2)
    y9=y2+r*m.sin(theta2)

    x10=x2-r*m.cos(theta1)
    y10=y2-r*m.sin(theta1)
 elif quadrant==4:
    x7=x1+r*m.cos(theta2)
    y7=y1+r*m.sin(theta2)

    x8=x1+r*m.cos(theta1)
    y8=y1-r*m.sin(theta1)

    x9=x2-r*m.cos(theta1)
    y9=y2+r*m.sin(theta1)

    x10=x2-r*m.cos(theta2)
    y10=y2-r*m.sin(theta2)

 elif quadrant==3:
    x7 = x1 - r * m.cos(theta1)
    y7 = y1 - r * m.sin(theta1)

    x8 = x1 + r * m.cos(theta2)
    y8 = y1 - r * m.sin(theta2)

    x9 = x2 - r * m.cos(theta2)
    y9 = y2 + r * m.sin(theta2)

    x10 = x2 + r * m.cos(theta1)
    y10 = y2 + r * m.sin(theta1)

 else:
    x7 = x1 - r * m.cos(theta1)
    y7 = y1 + r * m.sin(theta1)

    x8 = x1 - r * m.cos(theta2)
    y8 = y1 - r * m.sin(theta2)

    x9 = x2 + r * m.cos(theta2)
    y9 = y2 + r * m.sin(theta2)

    x10 = x2 + r * m.cos(theta1)
    y10 = y2 - r * m.sin(theta1)
 return (x7,y7,x8,y8,x9,y9,x10,y10)




def angle_1(x1,y1,x2,y2,x3,y3):
  a_x=x2-x3
  a_y=y2-y3
  a=m.sqrt((a_x*a_x)+(a_y*a_y))

  b_x = x3-x1
  b_y = y3-y1
  b = m.sqrt((b_x * b_x) + (b_y * b_y))

  c_x = x1-x2
  c_y = y1-y2
  c= m.sqrt((c_x * c_x) + (c_y * c_y))

  if abs(b - (a + c)) < 0.09:
      theta = 180
  elif abs(a - (b + c)) < 0.09:
      theta = 0
  else:
   theta=abs(m.degrees(m.acos(((a*a)+(c*c)-(b*b))/(2*a*c))))

  return theta

#**********Storing the inner tangent and outer tanget between pair of circle*********

pair=[]
for i in range(n):
 for j in range(n):
     if i!=j:
        pair.append((i,j))

#print(pair)
pt = {}
# pt contains tanget points in pair of circle
# pt((i,j) :(points)) all points joining tangents between cirlce i and circle j

for i in range(len(pair)):
    gr1_1=outer_tangent(points[pair[i][0]][0],points[pair[i][0]][1],points[pair[i][1]][0],points[pair[i][1]][1],r)
    gr1_2=inner_tangent(points[pair[i][0]][0],points[pair[i][0]][1],points[pair[i][1]][0],points[pair[i][1]][1],r)
    pt.update({(pair[i][0],pair[i][1]):(gr1_1,gr1_2)})

#print("pt",pt)

p={}
#
# for i in range(1,n):
#  p.update({(i,0,8):(pt[i,0][0][4],pt[i,0][0][5])})
#  p.update({(i,0,5):(pt[i,0][0][6],pt[i,0][0][7])})
#
#
#  if angle_1(p[i,0,8][0],p[i,0,8][1],points[0][0],points[0][1],pt[i,0][1][4],pt[i,0][1][5])<angle_1(p[i,0,8][0],p[i,0,8][1],points[0][0],points[0][1],pt[i,0][1][6],pt[i,0][1][7]):
#     p.update({(i,0,7):(pt[i,0][1][4],pt[i,0][1][5])})
#     p.update({(i,0,6):(pt[i,0][1][6],pt[i,0][1][7])})
#  else:
#     p.update({(i,0, 6): (pt[i,0][1][4], pt[i,0][1][5])})
#     p.update({(i,0, 7): (pt[i,0][1][6], pt[i,0][1][7])})

for i in range(n):
  for j in range(n):
    if i!=j:
     p.update({(i,j,1):(pt[i,j][0][0],pt[i,j][0][1])})
     p.update({(i,j,4):(pt[i,j][0][2],pt[i,j][0][3])})


     if angle_1(p[i,j,1][0],p[i,j,1][1],points[i][0],points[i][1],pt[i,j][1][0],pt[i,j][1][1])<angle_1(p[i,j,1][0],p[i,j,1][1],points[i][0],points[i][1],pt[i,j][1][2],pt[i,j][1][3]):

        p.update({(i,j,2):(pt[i,j][1][0],pt[i,j][1][1])})
        p.update({(i,j,3):(pt[i,j][1][2],pt[i,j][1][3])})
     else:

        p.update({(i,j, 3): (pt[i,j][1][0], pt[i,j][1][1])})
        p.update({(i,j, 2): (pt[i,j][1][2], pt[i,j][1][3])})


     p.update({(i,j,8):(pt[i,j][0][4],pt[i,j][0][5])})
     p.update({(i,j,5):(pt[i,j][0][6],pt[i,j][0][7])})

     if angle_1(p[i,j,8][0],p[i,j,8][1],points[j][0],points[j][1],pt[i,j][1][4],pt[i,j][1][5])<angle_1(p[i,j,8][0],p[i,j,8][1],points[j][0],points[j][1],pt[i,j][1][6],pt[i,j][1][7]):

        p.update({(i,j,7):(pt[i,j][1][4],pt[i,j][1][5])})
        p.update({(i,j,6):(pt[i,j][1][6],pt[i,j][1][7])})
     else:
        p.update({(i,j, 6): (pt[i, j][1][4], pt[i,j][1][5])})
        p.update({(i,j, 7): (pt[i, j][1][6], pt[i,j][1][7])})
#print("p",p)

e={1:(1,8),2:(2,6),3:(3,7),4:(4,5)}
#print("e",e)


def quadrant(x,y,x_c,y_c):
    if x>x_c and y>y_c:
        quad=1
    elif x<x_c and y>y_c:
        quad=2
    elif x<x_c and y<y_c:
        quad=3
    elif x>x_c and y<y_c:
        quad=4
    elif x>x_c and y==y_c:
        quad=1
    elif x==x_c and y>y_c:
        quad=2
    elif x<x_c and y==y_c:
        quad=3
    elif x==x_c and y<y_c:
        quad=4
    return quad

# def up_down(y1,y2,a):
#   if a=="en":
#     if y2>=y1:
#         dir="down"
#     else:
#         dir='up'
#   quad=quadrant()
#   if a=="ex":
#
#       if y2>=y1:
#           dir="up"
#       else:
#           dir='down'
#   return dir

def up_down(x1, y1, x2, y2, x_c, y_c, a):
    if a == "en":
        quad = quadrant(x2, y2, x_c, y_c)
        if y2 > y1:
            dir = "down"
        elif y2<y1:
            dir = 'up'
        elif y1==y2:
            if x1<x2:
                if quad==4:
                    dir='down'
                if quad==2:
                    dir='down'
            if x2<x1:
                if quad==2:
                    dir='up'
                if quad==4:
                    dir='up'
    if a == "ex":
        quad = quadrant(x1, y1, x_c, y_c)
        if y2 > y1:
            dir = "up"
        elif y2 < y1:
            dir = 'down'
        elif y2 == y1:
            if x2 < x1:
                if quad==2:
                  dir = 'down'
                if quad==4:
                    dir='down'
            elif x2 > x1:
                if quad==2:
                    dir='up'
                if quad==4:
                    dir='up'
    return dir

edges={}

for i in range(n):
 for j in range(n):
  for k in range(n):
   if i!=j and i!=k and j!=k:
    a_x=points[j][0]
    a_y=points[j][1]
    b_x=points[i][0]
    b_y=points[i][1]
    c_x=points[k][0]
    c_y=points[k][1]

    for l in entry:
        for q in exit:
            for b in e:
                if l==e[b][1]:
                   p1=b
                if q==e[b][0]:
                    p2=b

            x1=p[j,i,l][0]
            y1=p[j,i,l][1]
            det1=((b_x-a_x)*(y1-a_y))-((b_y-a_y)*(x1-a_x))
            x2=p[i,k,q][0]
            y2=p[i,k,q][1]
            det2 = ((c_x - b_x) * (y2 - b_y)) - ((c_y - b_y) * (x2 - b_x))

            if det1>=0 and det2>=0:
                if i in edges:
                    edges[i].append(((j,p1),(k,p2)))
                else:
                    edges.update({i:[((j,p1),(k,p2))]})

            if det1<0 and det2<0:
                if i in edges:
                    edges[i].append(((j,p1),(k,p2)))
                else:
                    edges.update({i:[((j,p1),(k,p2))]})


#print("edges",edges)


def cl_acl(i,j,k,p_en,p_ex):
    #quad1 is quadrant for entry point of circle i w.r.t. center of circle i
    quad1=quadrant(p[j,i,e[p_en][1]][0],p[j,i,e[p_en][1]][1],points[i][0],points[i][1])
    #quad2 is quadrant for exit point of circle i w.r.t. center of circle i
    quad2=quadrant(p[i,k,e[p_ex][0]][0],p[i,k,e[p_ex][0]][1],points[i][0],points[i][1])
    #dir1 is direction for entry tangent
    dir1=up_down(p[j,i,e[p_en][0]][0],p[j,i,e[p_en][0]][1],p[j,i,e[p_en][1]][0],p[j,i,e[p_en][1]][1],points[i][0],points[i][1],"en")
    #dir2 is direction for exit tangent
    dir2 = up_down(p[i, k, e[p_ex][0]][0],p[i, k, e[p_ex][0]][1], p[i,k, e[p_ex][1]][0],p[i,k, e[p_ex][1]][1],points[i][0],points[i][1],"ex")


    if quad1==1 and dir1=='up' and quad2==1 and dir2=='down':
        ang='acl'
    elif quad1==1 and dir1=='up' and quad2==2 and dir2=='up':
        ang='acl'
    elif quad1==1 and dir1=='up' and quad2==3 and dir2=='up':
        ang='acl'
    elif quad1==1 and dir1=='up' and quad2==4 and dir2=='down':
        ang='acl'
    elif quad1==2 and dir1=='down' and quad2==1 and dir2=='down':
        ang='cl'
    elif quad1==2 and dir1=='down' and quad2==2 and dir2=='up':
        ang='acl'
    elif quad1==2 and dir1=='down' and quad2==3 and dir2=='up':
        ang='acl'
    elif quad1==2 and dir1=='down' and quad2==4 and dir2=='down':
        ang='acl'
    elif quad1==3 and dir1=='down' and quad2==1 and dir2=='down':
        ang='cl'
    elif quad1==3 and dir1=='down' and quad2==2 and dir2=='up':
        ang='cl'
    elif quad1==3 and dir1=='down' and quad2==3 and dir2=='up':
        ang='acl'
    elif quad1==3 and dir1=='down' and quad2==4 and dir2=='down':
        ang='acl'
    elif quad1==4 and dir1=='up' and quad2==1 and dir2=='down':
        ang='cl'
    elif quad1==4 and dir1=='up' and quad2==2 and dir2=='up':
        ang='cl'
    elif quad1==4 and dir1=='up' and quad2==3 and dir2=='up':
        ang='cl'
    elif quad1==4 and dir1=='up' and quad2==4 and dir2=='down':
        ang='acl'
    elif quad1==1 and dir1=='down' and quad2==1 and dir2=='up':
        ang='acl'
    elif quad1==1 and dir1=='down' and quad2==2 and dir2=='down':
        ang='cl'
    elif quad1==1 and dir1=='down' and quad2==3 and dir2=='down':
        ang='cl'
    elif quad1==1 and dir1=='down' and quad2==4 and dir2=='up':
        ang='cl'
    elif quad1==2 and dir1=='up' and quad2==1 and dir2=='up':
        ang='acl'
    elif quad1==2 and dir1=='up' and quad2==2 and dir2=='down':
        ang='acl'
    elif quad1==2 and dir1=='up' and quad2==3 and dir2=='down':
        ang='cl'
    elif quad1==2 and dir1=='up' and quad2==4 and dir2=='up':
        ang='cl'
    elif quad1==3 and dir1=='up' and quad2==1 and dir2=='up':
        ang='acl'
    elif quad1==3 and dir1=='up' and quad2==2 and dir2=='down':
        ang='acl'
    elif quad1==3 and dir1=='up' and quad2==3 and dir2=='down':
        ang='acl'
    elif quad1==3 and dir1=='up' and quad2==4 and dir2=='up':
        ang='cl'
    elif quad1==4 and dir1=='down' and quad2==1 and dir2=='up':
        ang='acl'
    elif quad1==4 and dir1=='down' and quad2==2 and dir2=='down':
        ang='acl'
    elif quad1==4 and dir1=='down' and quad2==3 and dir2=='down':
        ang='acl'
    elif quad1==4 and dir1=='down' and quad2==4 and dir2=='up':
        ang='acl'
    else:
        ang='n/a'
    return ang

def angle(x,y,x_c,y_c):
    if x>=x_c and y>=y_c:
        quad=1
    elif x<=x_c and y>=y_c:
        quad=2
    elif x<=x_c and y<=y_c:
        quad=3
    elif x>=x_c and y<=y_c:
        quad=4

    if (x_c-x)==0:
        a=90
    else:
        a=m.degrees(m.atan((y-y_c)/(x-x_c)))
    #print(quad)

    #print(a)
    if quad==1:
        b=a
    elif quad==2:
        b = 180 + a
    elif a<0:
        b=360+a
    else:
        b=a+180
    return b

def arclength(x_en,y_en,x_ex,y_ex,x_c,y_c,a):
    ang1=angle(x_en,y_en,x_c,y_c)
    ang2=angle(x_ex,y_ex,x_c,y_c)
    b=abs(ang1-ang2)

    if a=='cl':
        ang=b
    elif a=='acl':
        ang=360-b
    return ang

arc={}

#arc={i:(j,en_p),(k,ex_p),cl/acl)   where en_p is entering edge and can be p1 p2,p3,p4
for i in edges:
 for j in range(len(edges[i])):
    if i in arc:
        arc[i].append(((edges[i][j][0][0], edges[i][j][0][1]), (edges[i][j][1][0],edges[i][j][1][1]),cl_acl(i,edges[i][j][0][0],edges[i][j][1][0],edges[i][j][0][1],edges[i][j][1][1])))
    else:
        arc.update({i:[((edges[i][j][0][0], edges[i][j][0][1]), (edges[i][j][1][0],edges[i][j][1][1]),cl_acl(i,edges[i][j][0][0],edges[i][j][1][0],edges[i][j][0][1],edges[i][j][1][1]))]})

#print("arc",arc)

e_type=[1,2,3,4]

arc_length={}

for i in edges:
    for j in range(len(edges[i])):
        if (i,(edges[i][j][0][0],edges[i][j][0][1]),(edges[i][j][1][0],edges[i][j][1][1]),cl_acl(i,edges[i][j][0][0],edges[i][j][1][0],edges[i][j][0][1],edges[i][j][1][1])) in arc_length:
            arc_length[i,(edges[i][j][0][0],edges[i][j][0][1]),(edges[i][j][1][0],edges[i][j][1][1]),cl_acl(i,edges[i][j][0][0],edges[i][j][1][0],edges[i][j][0][1],edges[i][j][1][1])].append(arclength(p[edges[i][j][0][0],i,e[edges[i][j][0][1]][1]][0],p[edges[i][j][0][0],i,e[edges[i][j][0][1]][1]][1],p[i,edges[i][j][1][0],e[edges[i][j][1][1]][0]][0],p[i,edges[i][j][1][0],e[edges[i][j][1][1]][0]][1],points[i][0],points[i][1],cl_acl(i,edges[i][j][0][0],edges[i][j][1][0],edges[i][j][0][1],edges[i][j][1][1])))
        else:
            arc_length.update({(i,(edges[i][j][0][0],edges[i][j][0][1]),(edges[i][j][1][0],edges[i][j][1][1]),cl_acl(i,edges[i][j][0][0],edges[i][j][1][0],edges[i][j][0][1],edges[i][j][1][1])):arclength(p[edges[i][j][0][0],i,e[edges[i][j][0][1]][1]][0],p[edges[i][j][0][0],i,e[edges[i][j][0][1]][1]][1],p[i,edges[i][j][1][0],e[edges[i][j][1][1]][0]][0],p[i,edges[i][j][1][0],e[edges[i][j][1][1]][0]][1],points[i][0],points[i][1],cl_acl(i,edges[i][j][0][0],edges[i][j][1][0],edges[i][j][0][1],edges[i][j][1][1]))})



#print(arc_length)


def tan_dist(i,j,a):

    dx=p[i,j,e[a][0]][0]-p[i,j,e[a][1]][0]
    dy=p[i,j,e[a][0]][1]-p[i,j,e[a][1]][1]

    d=m.sqrt((dx*dx)+(dy*dy))
    return d


dist={}

for i in range(n):
    for j in range(n):
        for k in e_type:
            if i!=j:
                dist.update({(i,j,k):tan_dist(i,j,k)})

#print("dist",dist)



from gurobipy import *

def combined_model():
 def subtourelim(model, where):
        if where == GRB.callback.MIPSOL:

            selected = []
            # for i in range(n):
            sol = model.cbGetSolution(model._b)
            selected = tuplelist((i, j) for i, j in model._b.keys() if sol[i, j] > 0.5)
            adjList = [[] for i in range(n)]
            for i, j in selected:
                adjList[i].append(j)
            # find the shortest cycle in the selected edge list
            components = subtour(adjList)
            print(components)
            count = 0
            if len(components) > 1:
                # add a subtour elimination constraint
                for component in components:

                    if len(component) >= 2:
                        count += 1
                if count > 1:
                    for component in components:
                        if (len(component) >= 2):
                            print('Add constraint for component: {}'.format(component))
                            m.cbLazy(
                                quicksum(b[i, j] for i in component for j in component if i != j) <= len(component) - 1)


 def subtour(adjList):
        discover = [0 for i in range(n)]
        components = []
        for i in range(n):
            component = []
            queue = []
            if discover[i] == 0:
                discover[i] = 1
                component.append(i)
                queue.append(i)
                while queue:
                    v = queue.pop(0)
                    for u in adjList[v]:
                        if discover[u] == 0:
                            discover[u] = 1
                            component.append(u)
                            queue.append(u)
                components.append(component)
        return components
 m=Model()

#x[i]=1 if circle is visited
 x={}
 for i in range(n):
     x[i]=m.addVar(vtype=GRB.BINARY,name='x'+str(i))

 b = {}
 for i in range(n):
     for j in range(n):
             b[i, j] = m.addVar(vtype=GRB.BINARY, name='b' + "_" + str(i) + "_" + str(j))

 g = {}
 for i in range(n):
     for j in range(n):
         for k in e_type:
             if i!=j:
                 g[i, j, k] = m.addVar(vtype=GRB.BINARY, name='t' + "(" + str(i) + "," + str(j) + "," + str(k) + ")")

 # y[i,j,k,p1,p2]=1 if edge p is selected to travel between circle i and circle j
 y={}
 for i in range(n):
     for j in range(n):
         for k in range(n):
             for t in e_type:
                 for q in e_type:
                     if i!=j and j!=k and i!=k:
                        y[i,j,k,t,q]=m.addVar(vtype=GRB.BINARY,name='y'+"("+str(i)+","+str(j)+","+str(k)+","+str(t)+","+str(q)+")")



#Objective Function
 z={}
 z=m.addVar(vtype=GRB.CONTINUOUS,name='z',obj=1)

 m.modelSense = GRB.MAXIMIZE
 m.update()


 m.addConstr(quicksum(x[i]*data[i] for i in range(n))==z)

 #first point to start
 m.addConstr(x[0]==1)
 #if circle is selected then it will have one link for leaving
 for i in range(n):
     m.addConstr(quicksum(b[i,j] for j in range(n) if i!=j)==x[i])

 #if circle is selected then it will have one link for entering
 for i in range(n):
     m.addConstr(quicksum(b[j,i] for j in range(n) if i!=j)==x[i])

 #distance
 m.addConstr(quicksum(g[i,j,k]*dist[i,j,k] for i in range(n) for j in range(n) for k in e_type if i!=j)+quicksum(arc_length[i,(edges[i][j][0][0],edges[i][j][0][1]),(edges[i][j][1][0],edges[i][j][1][1]),cl_acl(i,edges[i][j][0][0],edges[i][j][1][0],edges[i][j][0][1],edges[i][j][1][1])]*y[i,edges[i][j][0][0],edges[i][j][1][0],edges[i][j][0][1],edges[i][j][1][1]] for i in range(n) for j in range(len(edges[i])))<=D)
 #m.addConstr(quicksum(g[i, edges[i][j][1][0], edges[i][j][1][1]] * dist[i, edges[i][j][1][0], edges[i][j][1][1]] for i in range(n) for j in range(len(edges[i]))) <= D)

 #there should be one enetring tangent out of 4 if i selected
 for i in range(n):
     m.addConstr(quicksum(g[j,i,k] for j in range(n) for k in e_type if i!=j)==x[i])

 #there should be one exiting tangent out of 4 if i selected
 for i in range(n):
     m.addConstr(quicksum(g[i,j,k] for j in range(n) for k in e_type if i!=j) == x[i])

 #link between variable g and b
 for i in range(n):
     for j in range(n):
         if i!=j:
            m.addConstr(quicksum(g[j,i,k] for k in e_type)==b[j,i])
            m.addConstr(quicksum(g[i,j,k] for k in e_type)==b[i,j])

 #if circle i is selected then one combination from edges[i] will be selected
 # for i in range(n):
 #     m.addConstr(quicksum(y[i,j,k,t,q] for j in range(n) for k in range(n) for t in e_type for q in e_type if i!=j and j!=k and i!=k)==x[i])
 #
 # #linking variable y and t
 #
 # for i in range(n):
 #     for j in range(n):
 #         for k in range(n):
 #             for t in e_type:
 #                 for q in e_type:
 #                     if i!=j and j!=k and i!=k:
 #                        m.addConstr((g[j,i,t]+g[i,k,q]-1)<=y[i,j,k,t,q])
 #                        m.addConstr(g[j,i,t]>=y[i,j,k,t,q])
 #                        m.addConstr(g[i,k,q]>=y[i,j,k,t,q])

 for i in range(n):
     m.addConstr(quicksum(y[i,edges[i][j][0][0],edges[i][j][1][0],edges[i][j][0][1],edges[i][j][1][1]] for j in range(len(edges[i])))==x[i])

 #linking variable y and g

 for i in range(n):
     for j in range(len(edges[i])):
                        m.addConstr((g[edges[i][j][0][0],i,edges[i][j][0][1]]+g[i,edges[i][j][1][0],edges[i][j][1][1]]-1)<=y[i,edges[i][j][0][0],edges[i][j][1][0],edges[i][j][0][1],edges[i][j][1][1]])
                        m.addConstr(g[edges[i][j][0][0],i,edges[i][j][0][1]]>=y[i,edges[i][j][0][0],edges[i][j][1][0],edges[i][j][0][1],edges[i][j][1][1]])
                        m.addConstr(g[i,edges[i][j][1][0],edges[i][j][1][1]]>=y[i,edges[i][j][0][0],edges[i][j][1][0],edges[i][j][0][1],edges[i][j][1][1]])

 m._b=b
 m.params.LazyConstraints = 1
 #m.modelsense = GRB.MAXIMIZE
 m.optimize(subtourelim)

 a=[]
 b1=[]
 ent=[]
 def printsol():
     if m.status == GRB.status.OPTIMAL:
         for i in range(n):
                #print(x[i])
                if x[i].x>0.5:
                    print('x[%d]=1'%(i))

         for i in range(n):
             for j in range(n):
                 for k in range(n):
                     for t in e_type:
                         for q in e_type:
                          if i!=j and j!=k and i!=k:
                            if y[i,j,k,t,q].x>0.5:
                                print('y[%d,%d,%d,%s,%s]=1'%(i,j,k,t,q))

         for i in range(n):
             for j in range(n):
                 for k in e_type:
                     if i!=j:
                      if g[i,j,k].x>0.5:
                         print('g[%d,%d,%s]=1'%(i,j,k))
                         if k==1:
                             b1.append(((i,1),(j,8)))
                             ent.append((i,1))
                             ent.append((j,8))
                         elif k==2:
                             b1.append(((i,2),(j,6)))
                             ent.append((i,2))
                             ent.append((j,6))
                         elif k==3:
                             b1.append(((i,3),(j,7)))
                             ent.append((i,3))
                             ent.append((j,7))
                         elif k==4:
                             b1.append(((i,4),(j,5)))
                             ent.append((i,4))
                             ent.append((j,5))


         print(b1)
         print(ent)


         for i in range(n):
             for j in range(n):
                 if i!=j:
                     if b[i,j].x>0.5:
                         print('b[%d,%d]=1'%(i,j))
                         a.append((i,j))
         print(a)




 #m.optimize()
 printsol()

combined_model()


