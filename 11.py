

def func():
    while True:
        try:
            num = int(input().strip())
            arr = set()
            for _ in range(num):
                arr.add(input().strip())
            arr1 = list(map(int,arr))
            sorted(arr1)
            for i in range(len(arr1)):
                print(arr1[i])
        except EOFError:
            break
    # please define the python3 input here. For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().

if __name__ == "__main__":
    
    func()