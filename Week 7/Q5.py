a = [2,4,[6,3,2],[3,4,5],[3,4,8],(2,),9,1]
print ((lambda lst,ele: [True for i in lst if isinstance(i,list) if ele in i ])(a,5))