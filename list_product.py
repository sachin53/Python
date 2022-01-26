num_list=[4,2,5,1]
list_length=len(num_list)
for i in range(0,list_length):
    #print(i)
    hold_original=num_list[i]
    num_list[i]=1
    product=1
    for j in range(0,list_length):
        product=product*num_list[j]
    print("Product for index ",str(i),"= ",str(product))
    num_list[i]=hold_original

