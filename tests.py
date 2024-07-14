from collections import defaultdict


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
        for key, value in firstMap.copy().items():
            for key1, value2 in secondMap.copy().items():
                if value == value2:
                    print(f'{key}->{key1}', end=' ')
                    del secondMap[key1]
                    break
    else:
        print("NO")
    return
    

def bigSum():
    try:
        while True:
            nums = [int(item) for item in input().split()]
            print(nums[0] + nums[1])
    except EOFError:
        return
def findCard2():
    cases = 1
    try:
        while True:
            nq = input().split()
            n = int(nq[0])
            q = int(nq[1])
            origins = [int(item) for item in input().split()]
            inputs = sorted(origins)
            targets = [int(item) for item in input().split()]
            print(f"Case #{cases}:")
            for i in range(len(targets)):
                try:
                    index = inputs.index(targets[i]) + 1
                    origin = origins.index(targets[i]) + 1
                    print(f"{targets[i]} from {origin } to {index}")
                except ValueError:
                    print(f"{targets[i]} not found")
            cases+=1
    except EOFError:
        return

def initialize_blocks(n):
    return [[i] for i in range(n)]

def find_block_position(blocks, block):
    for pile in blocks:
        if block in pile:
            return pile, pile.index(block)
    return None, None

def return_to_initial(blocks, pile, index):
    # 仅将索引 index 之后的所有积木块放回初始位置
    to_return = pile[index+1:]
    for block in to_return:
        blocks[block].append(block)
    del pile[index+1:]

def move_onto(blocks, a, b):
    pile_a, index_a = find_block_position(blocks, a)
    pile_b, index_b = find_block_position(blocks, b)

    if pile_a is pile_b or a == b:
        return

    return_to_initial(blocks, pile_a, index_a)
    return_to_initial(blocks, pile_b, index_b)

    pile_b.append(pile_a.pop(index_a))

def move_over(blocks, a, b):
    pile_a, index_a = find_block_position(blocks, a)
    pile_b, _ = find_block_position(blocks, b)

    if pile_a is pile_b or a == b:
        return

    return_to_initial(blocks, pile_a, index_a)

    pile_b.append(pile_a.pop(index_a))

def stack_onto(blocks, a, b):
    pile_a, index_a = find_block_position(blocks, a)
    pile_b, index_b = find_block_position(blocks, b)

    if pile_a is pile_b or a == b:
        return

    return_to_initial(blocks, pile_b, index_b)

    pile_b.extend(pile_a[index_a:])
    del pile_a[index_a:]

def stack_over(blocks, a, b):
    pile_a, index_a = find_block_position(blocks, a)
    pile_b, _ = find_block_position(blocks, b)

    if pile_a is pile_b or a == b:
        return

    pile_b.extend(pile_a[index_a:])
    del pile_a[index_a:]

def swap_columns(blocks, a, b):
    pile_a, _ = find_block_position(blocks, a)
    pile_b, _ = find_block_position(blocks, b)

    if pile_a is pile_b or a == b:
        return

    # 交换两列
    blocks[blocks.index(pile_a)], blocks[blocks.index(pile_b)] = blocks[blocks.index(pile_b)], blocks[blocks.index(pile_a)]

def building_blocks():
    n = int(input())
    blocks = initialize_blocks(n)
    commands = list()
    while True:
        input_str = input()
        if (input_str == "q"):
            commands.append(input_str)
            break
        else:
            commands.append(input_str)
    for command in commands:
        if command == "q":
            break
        
        parts = command.split()
        
        if len(parts) != 4:
            continue
        
        action, a_str, preposition, b_str = parts
        a, b = int(a_str), int(b_str)
        
        if action == "mv":
            if preposition == "on":
                move_onto(blocks, a, b)
            elif preposition == "ov":
                move_over(blocks, a, b)
        elif action == "st":
            if preposition == "on":
                stack_onto(blocks, a, b)
            elif preposition == "ov":
                stack_over(blocks, a, b)
        elif action == "xh" and preposition == "an":
            swap_columns(blocks, a, b)
    
    for i, pile in enumerate(blocks):
        if len(pile) == 0:
            print(f"{i}:")
        else:
            print(f"{i}: {' '.join(map(str, pile))}")
import heapq
def generate_sequences(limit):
    # 使用最小堆
    heap = []
    heapq.heappush(heap, 1)
    # 使用集合防止重复
    seen = {1}
    # 预先生成前 limit 个丑数
    ugly_numbers = []
    for _ in range(limit):
        smallest = heapq.heappop(heap)
        ugly_numbers.append(smallest)
        for factor in [2, 3, 5]:
            new_ugly = smallest * factor
            if new_ugly not in seen:
                seen.add(new_ugly)
                heapq.heappush(heap, new_ugly)
    
    return ugly_numbers
def ugly_numbers():
    
    # 设定生成丑数的上限
    limit = 10000
    ugly_numbers = generate_sequences(limit)
    import sys
    input = sys.stdin.read
    data = input().split()
    
    for line in data:
        n = int(line)
        print(ugly_numbers[n - 1])

import sys
from collections import defaultdict

def find_special_words():
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    word_dict = defaultdict(list)
    first_appearance = defaultdict(str)
    
    for line in data:
        if line.strip() == "#":
            break
        words = line.split()
        for word in words:
            normalized = ''.join(sorted(word.lower()))
            word_dict[normalized].append(word)
            if normalized not in first_appearance:
                first_appearance[normalized] = word
    
    special_words_set = set()
    for normalized, originals in word_dict.items():
        originals = set(originals)
        if len(originals) > 1:
            special_words_set.add(first_appearance[normalized])
    
    special_words_list = sorted(special_words_set, key=lambda x: x)
    for word in special_words_list:
        print(word)


def format_files(filenames, width):
    # 按字典序排序文件名
    filenames.sort()
    # 计算文件名的最大长度
    max_length = max(len(name) for name in filenames)

    # 计算一行可以包含的文件名数量（列数）
    cols = (width + 2) // (max_length + 2)
    if cols == 0:
        cols = 1

    # 计算列数
    # 确保列数至少为 1
    if cols == 0:
        cols = 1

    # 计算所需的行数
    rows = (len(filenames) + cols - 1) // cols

    # 将文件名按列分布
    grid = [['' for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if i == 0:  
                if j == 0:
                    grid[0][0] = filenames[0]
                else:
                    grid[i][j] = filenames[j * rows]
            else:
                if(grid[i - 1][j] == ''):
                    continue
                index = filenames.index(grid[i - 1][j]) + 1
                if index < len(filenames):
                    grid[i][j] = filenames[index] 
            

    # 打印格式化后的文件名
    for row in grid:
        line = ""
        for i in range(cols):
            if i < cols - 1 and row[i]:
                line += f"{row[i]:<{max_length}}  "
            else:
                line += f"{row[i]:<{max_length}}"
        print(line.strip())
def formatMenu():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    i = 0

    while i < len(data):
        # n是文件数，w是宽度
        n, w = map(int, data[i].split())
        # 
        filenames = [data[j] for j in range(i+1, i+1+n)]
        i += 1 + n

        if n == 0:
            continue

        # 输出分隔符线
        print('-' * w)

        # 格式化并输出文件名
        format_files(filenames, w)

import sys
import re
from collections import defaultdict
def process_text():
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    word_count = defaultdict(int)

    for line in data:
        # 去除以's结尾的单词的's
        line = re.sub(r"\b(\w+)'s\b", r"\1", line)
        # 去除其他标点符号并将所有字符转换为小写
        line = re.sub(r"[^\w\s-]", "", line).lower()
        # 分割单词，对连字符处理
        words = re.split(r"[\s-]+", line)  # 对空格和连字符进行分割
        
        for word in words:
            if word:  # 只处理非空单词
                word_count[word] += 1

    sorted_words = sorted(
        word_count.items(),
        key=lambda x: (-x[1], x[0])
    )
    
    for word, count in sorted_words:
        print(word)

def find_magic_numbers(x, N):
    results = []
    for a in range(1, N+1):
        for b in range(a, N+1):
            for c in range(b, N+1):
                d_value = a ** x + b ** x + c ** x
                d = int(round(d_value ** (1 / x)))  # 取整数并四舍五入
                # 检查 d 是否正确，并且在范围 1 到 N 以内
                if d ** x == d_value and 1 <= d <= N:
                    results.append((a, b, c, d))
    return results
def magic_num():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    case_number = 1
    
    for line in data:
        if line.strip():
            x, N = map(int, line.split())
            results = find_magic_numbers(x, N)
            print(f"Case {case_number}:")
            if results:
                for a, b, c, d in results:
                    print(f"{a}^{x}+{b}^{x}+{c}^{x}={d}^{x}")
            else:
                print("No such numbers.")
            
            case_number += 1

def find_max_product(nums):
    n = len(nums)
    max_product = float('-inf')
    start = end = 0
    #暴力穷举
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= nums[j]
            if product > max_product:
                max_product = product
                start, end = i, j
            elif product == max_product:
                # 范围最小序列
                if (j - i) < (end - start):
                    start, end = i, j
                # 起始最小序列
                elif (j - i) == (end - start) and i < start:
                    start, end = i, j
    return max_product, start, end

def max_product():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    case_number = 1
    for line in data:
        if line.strip():
            nums = list(map(int, line.split()))
            max_product, start, end = find_max_product(nums)
            print(f"Case {case_number}: {max_product} {start}-{end}")
            case_number += 1

def main():
    max_product()
    

if __name__ == '__main__':
    main()