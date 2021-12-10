#给一个数组，不断对数组两端求和，最后得到长度为二的数组返回


def sum_two(input_array):
    # Write your code here
    length = len(input_array)
    res = []
    left = 0
    right = length - 1
    while len(input_array) > 2:
        left = 0
        right = len(input_array) - 1
        while left < right:
            total = input_array[left] + input_array[right]
            input_array[left] = total
            input_array.pop()
            left += 1
            right -= 1

    return input_array
input_array = [1,2,5,8,10,6]
ss = sum_two(input_array)
print(ss)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip()) #strip()删除末尾空格

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')