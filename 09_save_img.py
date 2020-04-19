import requests

response = requests.get('https://i0.hdslb.com/bfs/archive/399b2db27c83bfb2d1e8b6668fb9e21e787bd207.gif')

with open('./data/a.gif','wb') as f:
    f.write(response.content)