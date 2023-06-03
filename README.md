# Maxima-Minima
DSAD Problem of Maxima-Minima

Problem Statement : Does Maxima Minima exist for given input function?

OVERVIEW
    1- To read the input file from the mentioned four distributions form and return minima or maxima of array.
    2- Divide the data into small subparts .
    3- Declare minima and maxima by comparing index array with (index +1) array
    4- Define maximum and minimum for recursive iteration on the subparts .
    5- Define all the four cases of strictly increasing, strictly decreasing, minima and maxima and output for each cases.
Case(i) – If array is in strictly increasing form of let say length n.

Then, the array will be divided in n parts and recursion will run comparing array index and maxima and minima as defined above.

For example:
1 2 3 4 5 6
    i) 5 will be index compared with 6 and 5 will be returned 
    ii) Then 4 and 5(result of first recursive iteration) will be compared and 4 will be returned.
    iii) Next 3 and result of above iteration will be compared.
    iv) Such process will continue till n times
Hence complexity will be in order of ‘n’ for the given four conditions of data of array.


Case(ii) – If array is in strictly decreasing form of, let say length n.

Then, the array will be divided in n parts and recursion will run comparing array index and maxima and minima as defined above.

For example:
6 5 4 3 2 1
    i) 2 will be index compared with 1 and 1 will be returned 
    ii) Then 3 and 1 (result of first recursive iteration) will be compared and 1 will be returned.
    iii) Next 4 and result of above iteration will be compared.
    iv) Such process will continue till n times
Hence complexity will be in order of ‘n’ for the given four conditions of data of array .


Case(iii) – If array is in maxima form of , let say length n.

Then , the array will be divided in n parts and recursion will run comparing array index and maxima and minima as defined above.

For example:
1 2 3 4 3 2 1
    i) 2 will be index compared with 1 and 2 will be returned 
    ii) Then 3 and 2 (result of first recursive iteration) will be compared and 3 will be returned.
    iii) Next 4 and result of above iteration (3) will be compared and 4 will return.
    iv) Next 3 and result of above iteration (4) will be compared and 4 will return.
    v) Such process will continue till n times and result will be 4 (maxima).
Hence complexity will be in order of ‘n’ for the given four conditions of data of array.


Case(iv) – If array is in minima form of, let say length n.

Then, the array will be divided in n parts and recursion will run comparing array index and maxima and minima as defined above.

For example:
4 3 2 1 2 3 4
    i) 3 will be index compared with 4 and 3 will be returned 
    ii) Then 2 and 3(result of first recursive iteration) will be compared and 2 will be returned.
    iii) Next 1 and result of above iteration (2) will be compared and 1 will return.
    iv) Next 2 and result of above iteration (1) will be compared and 1 will return.
    v) Such process will continue till n times and result will be 1 (minima).
Hence complexity will be in order of ‘n’ for the given four conditions of data of array .

 
                          COMPARISON WITH OTHER ALGORITHM

    1- Using Linear Search

In our technique we are dividing the array recursively and then searching 2 elements at once, rather than just going sequentially. So our algorithm is better in that sense. For both, the running time complexity is O(n) but ammortised analysis for divide and conquer shows O(log n) 

