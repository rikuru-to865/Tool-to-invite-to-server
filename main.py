import requests
invitecode = input("招待urlを入力")
tokens = []
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
with open("./varitify_token.txt",mode="r") as f:
    for l in f:
        tokens.append(l)
b = 0

with open("./proxys.txt",mode="r") as f:
    for i in f:
        proxyDict = { 
              "http"  : i
            }
        r = requests.post("https://discord.com/api/v8/invites/"+invitecode,proxies=proxyDict,headers={'authorization':tokens[b].replace("\n",""),'User-Agent': ua})
        print(int(r.status_code))
        b+=1
