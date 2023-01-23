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
#2 repo_dict = repo_dicts[0]
#print("\nKeys:", len(repo_dict))
#for key in sorted(repo_dict.keys()):
 #   print(key)

#print("\nSelected information about first repository:")
#print('Name:', repo_dict['name'])
#print('Owner:',repo_dict['owner']['login'])
#print('Stars:' ,repo_dict['stargazers_count'])
#print('Repository:', repo_dict['html_url'])
#print('Created:',  repo_dict['created_at'])
#print('Updated:', repo_dict['updated_at'])
#print('Decription:', repo_dict['description'])
print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])
    
