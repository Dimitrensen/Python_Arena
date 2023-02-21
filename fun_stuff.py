

# given an arr [6,7,98,4,32,6,475,56,86,9,4,4,53,4,346,7,5,5,8,7,79,9,79,9,3]
# print how many number 4 does the arr includes
# remove the 9 largest numbers in the arr
# and the 3 smallest
# add numbers to the array starting from 1 10 time with step 2 and each number should be =>
# multiplied by 2 before added to the array  ex 1x2 2x2 3x2 etc
# insert the number 3 the second spot in the array and 5 to the spot before the last
# replace the 7th number with 111
# remove items from the array till only 2 are left
# return the original array and the modified one

arr=[6,7,98,4,32,6,475,56,86,9,4,4,53,4,346,7,5,5,8,7,79,9,79,9,3]
original_arr=arr.copy()
number_fours= arr.count(4) # int
print("Your list has",number_fours,"bananas") # srt + int, str + str
arr.sort()
print(arr)

new_arr=arr[:-9]
print(new_arr)
new_arr=new_arr[3:]
print(new_arr)


for i in range(1,10,2):
    new_arr.append(i*2)

print(new_arr)


new_arr.insert(1,3)
new_arr.insert(-1,5)
print(new_arr)

new_arr[6]=111
print(new_arr)

new_arr=new_arr[:2]
print(new_arr)

print(new_arr)
print(original_arr)
# return the original array and the modified one concatenated
concat=new_arr + original_arr
print(concat)