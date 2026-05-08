def multiplication_table(number: int) -> list[str]:
    ans = []
    for i in range(1, 11):
        ans.append(f"{str(number)}x{str(i)}={number*i}")
    return ans

multiplication_table(2)

#enumerate 
def exp_enumerate(array: list):
    for idx, value in enumerate(array, start=1):
        print(idx, " ", value)
        
#zip
names = ["Alice", "Bob"]
scores = [85, 90]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
