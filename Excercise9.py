# def form_new_list(new_list):
#     return [str(element) for element in new_list if type(element) == int or type(element) == float]
#
# new_list = [1,2,3,4,5,6,9.8,8.2,9.9,1.3,'sumit','saurav',[1,2,'sumit']]
#
# print(form_new_list(new_list)) 

print({i:('odd' if(i%2!=0) else 'even') for i in range(1,11)})

