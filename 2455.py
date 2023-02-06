people_nums = []
people = 0 

for _ in range(4) :
    a, b = map(int,input().split())
    people += a #타는 사람
    people -= b #내리는 사람

    people_nums.append(people) #종착역 마다의 사람 수 추가
    
print(max(people_nums))