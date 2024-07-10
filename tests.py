

def sum1():
    try:
        while True:
            nums = input().split()
            sum = 0
            for n in nums:
                sum+= int(n)
            print(sum)
    except EOFError:
        return
    
def trangle():
    result = input().split()
    char = result[0]
    edges = int(result[1])
    for i in range(1, edges + 1):
        blank = edges - i
        for _ in range(blank):
            print(" ", end='')
        star = 0
        # 每行结束的下标
        last = edges * 2 - 1 - (edges - i)
        for j in range(blank, last):
            # 最后一行
            if i == edges:
                if star % 2 == 0:
                    print(char, end='')
                else:
                    print(" ", end='')
            else:
                if star == 0  or j == last - 1:
                    print(char, end='')
                else:
                    print(" ", end='')
            star += 1
                
        print()
        
#
def maxDif():
    count = input()
    chars = input().split()   
    nums = [int(item) for item in chars]
    min_val = float('inf')
    max_val = float('-inf')
    
    for num in nums:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    max_dif = max_val - min_val
        
    print(max_dif)

def minDif():
    count = input()
    chars = input().split()   
    nums = [int(item) for item in chars]
    #先排序 O(nlongn)
    nums.sort()
    minDif = float('inf')
    for i in range(1, len(nums)):
        minDif = min(minDif, abs(nums[i] - nums[i - 1]))   
    print(minDif)
    
def minDifWithPosition():
    count = input()
    chars = input().split()   
    nums = [int(item) for item in chars]
    
    #创建一个key-value
    map = {}
    
    # 存储index
    for i in range(len(nums)):
        map[nums[i]] = i
    
    #先排序 O(nlongn)
    nums.sort()
    minDif = float('inf')
    start = 0
    end = 0
    for i in range(1, len(nums)):
        value = abs(nums[i] - nums[i - 1])
        if (value < minDif):
            start = map.get(nums[i])
            end = map.get(nums[i - 1])
            minDif = value
    print(minDif, end=' ')
    if(start > end):
        print(end + 1, end=' ')
        print(start + 1, end=' ')
    else:
        print(start + 1, end=' ')
        print(end + 1, end=' ')
    
def sumOf16():
   try:
     while True:
        chars = input().split()
        nums = [int(item, 16) for item in chars]
        sum = 0
        for num in nums:
            sum += num
        print(sum)
   except EOFError:
       return

def dateFormat():
    try:
        while True:
            dates = input().split('-')
            result = ''
            if len(dates[1]) < 2:
                result+='0'
            result += dates[1]
            result +='/'
            if len(dates[2]) < 2:
                result+='0'
            result += dates[2]
            result += '/'
            result += dates[0]
            print(result)
    except EOFError:
        return
def equivalentStrings():

    first = list(input())
    second = list(input())
    firstMap = {}
    secondMap = {}
    for i in range(len(first)):
        if not firstMap.get(first[i]):
            firstMap[first[i]] = 1
        else:
            firstMap[first[i]] += 1
    
    for i in range(len(second)):
        if not secondMap.get(second[i]):
            secondMap[second[i]] = 1
        else:
            secondMap[second[i]] += 1 
    firstCount = sorted(firstMap.values())
    secondCount = sorted(secondMap.values())
    if firstCount == secondCount:
        print("YES")
    else:
        print("NO")

def findCard():
    cases = 1
    try:
        while True:
            nq = input().split()
            n = int(nq[0])
            q = int(nq[1])
            inputs = sorted([int(item) for item in input().split()])
            targets = [int(item) for item in input().split()]
            print(f"Case #{cases}:")
            for i in range(len(targets)):
                try:
                    index = inputs.index(targets[i]) + 1
                    print(f"{targets[i]} found at {index}")
                except ValueError:
                    print(f"{targets[i]} not found")

            cases+=1
    except EOFError:
        return

def printUniqueNum():
    try:
        input()
        nums = sorted([int(item) for item in input().split()], reverse=True)
        appeared = []
        for num in nums:
            if appeared.count(num) > 0:
                continue
            else:
                appeared.append(num)
                print(num, end=' ')
        print()
    except EOFError:
        return
             
def stringsReflect():
    return
    
    
    
        

def main():
    printUniqueNum()

if __name__ == '__main__':
    main()