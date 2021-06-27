import numpy as np
a=np.array([0,30,45,60,90])

# convert to radius by multiplying with pi/180

print("sine values of different angle ")
print(np.sin(a*np.pi/180))
print("cosine values for angles in array")
print(np.cos(a*np.pi/180))
print("tangent values for angles in array")
print(np.tan(a*np.pi/180))
print("value of pi")
print(np.pi)