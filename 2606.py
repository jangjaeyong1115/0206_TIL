n = int(input()) # 컴퓨터 개수
m = int(input()) # 연결된 선 개수

graph = [[] for _ in range(n+1)] 
visited = [False] * (n)


for _ in range(m):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2) 
    graph[v2].append(v1) 


def dfs(v): 
    stack = [v] 
    visited[v] = True 
    while stack:
        num = stack.pop() 
       
        for i in graph[num]: 
            if not visited[i]:
                visited[i] = True 
                stack.append(i)
dfs(1) 
print(sum(visited)-1)