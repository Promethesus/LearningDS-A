arr = [-1,-1,0,1,1]

def plus_minus(arr):
    positive = 0
    negative = 0
    zero = 0
    for number in arr:
        if number > 0: 
            positive += 1
        elif number < 0: 
            negative += 1
        else : 
            zero += 1

    def formatted_value(value):
        return format(value/len(arr), ".6f")
        

    
    print(formatted_value(positive))
    print(formatted_value(negative))
    print(formatted_value(zero))


plus_minus(arr)