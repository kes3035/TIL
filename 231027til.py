import numpy as np

def f(x):
    output = np.sin(x)*np.cos(2*x)  # 원하는 함수 적기 ex) sin(x)*cos(2x)
    return output

def forward_difference(x, h):
    output = (f(x+h) - f(x))/h
    return output

def backward_difference(x, h):
    output = (f(x) - f(x-h))/h
    return output

def center_difference(x, h):
    output = (f(x+h) - f(x-h))/(2*h)
    return output

answer_of_fordiff = forward_difference(5, 0.1)
answer_of_bacdiff = backward_difference(5, 0.1)
answer_of_cendiff = center_difference(5, 0.1)

exact_value = np.cos(5)*np.cos(2*5) - np.sin(5)*2*np.sin(2*5)
error_of_for = abs((exact_value-answer_of_fordiff)/exact_value)*100
error_of_back = abs((exact_value-answer_of_bacdiff)/exact_value)*100
error_of_cen = abs((exact_value-answer_of_cendiff)/exact_value)*100


print(f"전진차분식값 = {answer_of_fordiff}")
print(f"    실제값 = {exact_value}")
print(f"    오차율 ={error_of_for:0.1f}%")
print("")
print("")
print("")
print(f"후진차분식값 = {answer_of_bacdiff}")
print(f"    실제값 = {exact_value}")
print(f"    오차율 ={error_of_back:0.1f}%")
print("")
print("")
print("")
print(f"중간차분식값 = {answer_of_cendiff}")
print(f"    실제값 = {exact_value}")
print(f"    오차율 ={error_of_cen:0.1f}%")




#  f == 미분하려고 하는 함수
#  x == x의 값 
#  method == 미분할 방법 
#    'central'  중간차분 (기본값)
#    'forward'  전진차분
#    'backward' 후진차분
 
def numerical_differentiation(f, x, method='central'):
  h = 0.1  # 최대한 작은 값 ex)1e-4
  
  if method == 'central':
    result = (f(x + h) - f(x - h)) / (2 * h)
  elif method == 'forward':
    result = (f(x + h) - f(x)) / h
  elif method == 'backward':
    result = (f(x) - f(x - h)) / h
  else:
    raise ValueError("Method must be either 'central', 'forward', or 'backward'")
  return result

answer_of_fordiff = numerical_differentiation(f,5, method="forward")
answer_of_bacdiff = numerical_differentiation(f,5, method="backward")
answer_of_cendiff = numerical_differentiation(f,5)

error_of_for = abs((exact_value-answer_of_fordiff)/exact_value)*100
error_of_back = abs((exact_value-answer_of_bacdiff)/exact_value)*100
error_of_cen = abs((exact_value-answer_of_cendiff)/exact_value)*100

print("----------------------------------------------")

print(f"전진차분식값 = {answer_of_fordiff}")
print(f"    실제값 = {exact_value}")
print(f"    오차율 ={error_of_for:0.1f}%")
print("")
print("")
print("")
print(f"후진차분식값 = {answer_of_bacdiff}")
print(f"    실제값 = {exact_value}")
print(f"    오차율 ={error_of_back:0.1f}%")
print("")
print("")
print("")
print(f"중간차분식값 = {answer_of_cendiff}")
print(f"    실제값 = {exact_value}")
print(f"    오차율 ={error_of_cen:0.1f}%")
