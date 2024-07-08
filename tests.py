

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
    
     
        

def main():
    minDif()

if __name__ == '__main__':
    main()