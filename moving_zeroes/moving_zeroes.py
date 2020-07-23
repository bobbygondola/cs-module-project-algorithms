'''
Input: a List of integers
Returns: a List of integers


Write a function that takes an array of integers and moves each non-zero integer to the left side of the array,
then returns the altered array. The order of the non-zero integers does not matter in the mutated array.

'''

# first thought, we can break it down into one integer pieces and sort all the == 0 to a left pointer
# second thought, we append 0s to the back of a new arr, and append the others to the front

def moving_zeroes(arr):
    for i in arr:
        if i == 0:
            arr.remove(i)
            arr.append(i)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")