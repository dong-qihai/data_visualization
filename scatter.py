import matplotlib.pyplot as plt 
 
x_values = list(range(1,101))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,c='blue',edgecolor='yellow',s=3) 
 
 

plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,110,0,12100])
plt.show()
