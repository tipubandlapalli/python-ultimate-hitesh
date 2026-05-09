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
def generate_score_report(names, scores):
    return [f"{name} --> {score}" for name, score in zip(names, scores)]

# match case continue break loop_fallback_else 

# walrus
# (:=)

# using dictionary over match case