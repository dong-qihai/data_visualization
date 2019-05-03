import matplotlib.pyplot as plt
 
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth=1)

plt.title("Square Number",fontsize=14)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
 

plt.tick_params(axis='both',labelsize=24)
 
plt.show()



