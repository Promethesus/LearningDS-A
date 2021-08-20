arr = [7,69,2,221,8974]

def miniMaxSum(arr):
    sortedArr = sorted(arr)
    runningSmallestSum = sortedArr[0]
    runningLargestSum = runningSmallestSum
    sum = 0
    
    for i in range(len(sortedArr)):
        sum += sortedArr[i]

    if(sortedArr[i]) < runningSmallestSum:
        runningSmallestSum = sortedArr[i]

    if(sortedArr[i]) > runningLargestSum:
        runningLargestSum = sortedArr[i]

    
    print(sum - runningLargestSum, sum - runningSmallestSum)

miniMaxSum(arr)