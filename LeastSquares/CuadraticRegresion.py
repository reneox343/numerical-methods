import numpy as np
import matplotlib.pyplot as plt

##------ Generation of arbitrary points
x = np.array([0,0.41888,0.83776,1.2566,1.6755,2.0944,2.5133]).T
print(x)
a0 = 1
a1 = 0.4
a2 = 0.2
noise_amp = 1  #Maximum amplitude of the noise
y = a0 + a1*x + a2*(x**2)   #Cuadratic function
noise = 0 # noise_amp*np.random.rand(y.shape[0],y.shape[1]) #Random noise (gaussian)
y = y + noise  #Linear function with random noise

##--------- Linear regression model 
A = np.matrix([[x.shape[0],np.sum(x),np.sum(x**2)],[np.sum(x),np.sum(x**2),np.sum(x**3)],[np.sum(x**2),np.sum(x**3),np.sum(x**4)]])
b = np.matrix([[np.sum(y)],[np.sum(x*y)],[np.sum((x**2)*y)]])
a_vals = np.linalg.inv(A)*b
y_model = a_vals[1,0]*x+a_vals[0,0]

##--------- Plot input data and model
plt.clf()
plt.subplot(2,2,1)
plt.plot(x,y,marker='.',ms=8,mfc=(1,0,0),mec=(1,0,0),ls='')
plt.plot(x,y_model,color=[0,0,0],ls='-',lw=2)
plt.xlabel('x',fontsize=14,fontweight='bold')
plt.ylabel('y',fontsize=14,fontweight='bold')
plt.xticks(plt.xticks()[0],fontsize=12,fontweight='bold')
plt.yticks(plt.yticks()[0],fontsize=12,fontweight='bold')
plt.grid(True)

##--------- Display resulst in command window
print('------------------------------------------')
print('Function:');
print('a0 = '+str(a0),'\ta1 = '+str(a1),'\ta2 = '+str(a2))
print('')
print('Cuadratic regression model:')
print('a0 = '+str(a_vals[0,0])+'\ta1 = '+str(a_vals[1,0])+'\ta2 = '+str(a_vals[2,0]))
print('------------------------------------------')

##--------- Put input points in a matrix
Data = np.concatenate((x,y),axis=1)
##-- Copy the data from variable editor, paste in excel, insert a scatter plot
## there and add trendline
