import numpy as np

# 0D Tensors
ZeroDTensor= np.array(2);

print(ZeroDTensor)
print("No of dimension : ",ZeroDTensor.ndim)



#1D Tensors

OneDTensor = np.array([1,2,3,4,5])


print(OneDTensor)
print("No of dimension : ",OneDTensor.ndim)


#2d Tensors


twoDTensor = np.array([[1,2],[4,5]])


print(twoDTensor)
print("No of dimension : ",twoDTensor.ndim)


#3dTensors
threeDTensor = np.array([[[1,2],[4,5]],[[6,7],[6,8]]])


print(threeDTensor)
print("No of dimension : ",threeDTensor.ndim)




#4dTensors
fourDTensor = np.array([[[[1,2],[4,5]],[[6,7],[6,8]],[[1,2],[4,5]],[[6,7],[6,8]]]])


print(fourDTensor)
print("No of dimension : ",fourDTensor.ndim)