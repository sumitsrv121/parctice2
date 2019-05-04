student={
    'Ankit':{'score':90,'age':24},
    'Akash':{'score':100,'age':24},
    'Aniket':{'score':80,'age':24}
}
print(max(student,key=lambda item:student[item]['score']))