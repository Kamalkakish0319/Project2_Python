import matplotlib.pyplot as plt 

x = [7, 12, 17 , 9, 10]
  
y = [11, 8, 7, 2, 3]
  
# Function to plot
plt.plot(x,y)
# function to show the plot
plt.show()

#barchart
plt.bar(x,y) 
plt.show()

#histogram
plt.hist(y)
plt.show()

#scatterplot
plt.scatter(x, y)
plt.show()