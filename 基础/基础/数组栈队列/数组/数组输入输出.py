if __name__ == '__main__':




    ranked = list(map(int, input().rstrip().split()))  #保存为list

    player_count = int(input().strip()) #输入单个数字

    player = list(map(int, input().rstrip().split())) 

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))   #将restul 每行输出一个
    fptr.write('\n')