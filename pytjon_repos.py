import requests

#执行API调用并且储存响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

#将API响应储存在一个变量中
response_dict = r.json()

print("Total repositories:",response_dict['total_count'])

repo_dicts = response_dict['items']
print("Repositories returned:",len(repo_dicts))

#研究第一个仓库
repo_dict = repo_dicts[0]

