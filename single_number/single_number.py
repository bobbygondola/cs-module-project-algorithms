'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

'''FIRST THOUGHT''' # we want to check which number only shows up once in a normally double listed array
# we can check if the index[0] == index[1] and so on maybe -- nope



def single_number(arr):
    
    singles = []
    for i in arr:                   # 1.) iterates over each item
        if i in singles:            # 3.) if its pair is in singles(meaning its not alone..)
            singles.remove(i)       # 4.) remove it
        else:
            singles.append(i)       # 2.) append to singles
    if len(singles) == 1:
        return singles[0]           # 5.) return any singles left that their pair didnt remove them.
        
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")