import requests

r = requests.get("https://imgs.xkcd.com/comics/houseguests.png")
print(r.content)

with open('comic.png', 'wb') as f:
    f.write(r.content)
# print(dir(r))
# print(help(r))