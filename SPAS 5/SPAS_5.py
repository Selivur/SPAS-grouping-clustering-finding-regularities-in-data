import matplotlib.pyplot as plt
cost = [43304,28000,18500,15400,12900]
year = [1 ,2, 3, 4, 5]
n=5
k=7
m_cost=sum(cost)/n
m_year=sum(year)/n
m_sq_cost=0
sum =0
x_sq_sum = 0
i=0
while i<n:
    sum=year[i]*cost[i]+sum
    x_sq_sum=year[i]*year[i]+x_sq_sum
    i=i+1

b1=(sum/n-(m_year*m_cost))/(x_sq_sum/n-m_year*m_year)
b0=m_cost-m_year*b1
p_year=[1,2,3,4,5,6,7]
y=[0]*k
i=0;
while i<k:
    y[i]=b0+i*b1
    i=i+1
fig, ax = plt.subplots()
ax.plot(p_year, y)
ax.scatter(year, cost)
ax.scatter(p_year, y)
ax.legend(["Linear regression","Data points","Linear regression points"])
plt.show()