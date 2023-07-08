import numpy as np
import matplotlib.pyplot as plt

##------ Generation of arbitrary points
x = np.array([np.linspace(2,20,200)]).T

a0 = 1
a1 = 0.4
noise_amp = 1  #Maximum amplitude of the noise
y =  a0 + a1*x  #Linear function

noise = noise_amp*np.random.rand(y.shape[0],y.shape[1]) #Random noise (gaussian)
y = y + noise  #Linear function with random noise

##--------- Linear regression model 
A = np.matrix([[x.shape[0],np.sum(x)],[np.sum(x),np.sum(x**2)]])
b = np.matrix([[np.sum(y)],[np.sum(x*y)]])
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
print('------------------------------------------');
print('Linear Function:');
print('a0 = '+str(a0),'\ta1 = '+str(a1))
print('')
print('Regression model:')
print('a0 = '+str(a_vals[0,0])+'\ta1 = '+str(a_vals[1,0]))
print('------------------------------------------');

##--------- Put input points in a matrix
Data = np.concatenate((x,y),axis=1)
##-- Copy the data from variable editor, paste in excel, insert a scatter plot
## there and add trendline
