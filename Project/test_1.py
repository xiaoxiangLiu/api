import requests

url = "http://zjh.demo.sjgtw.com/login"

payload = "userid=13639930154&password="
headers = {
    'accept': "application/json,text/javascript,*/*;q=0.01",
    'accept-encoding': "gzip,deflate",
    'accept-language': "zh-cn,zh;q=0.9",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    'x-requested-with': "XMLHttprequest",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'postman-token': "87a4c055-0219-7e86-885d-474a0842d11e"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.status_code)

