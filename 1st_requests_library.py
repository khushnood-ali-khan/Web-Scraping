import requests          #import requests library.

url = "https://www.quora.com/"      #assign link to url

pr = requests.get(url)              #make a requests to url which have website link.

print(pr.status_code)               #print if the requests is successful. if the ouput is between (200 to 299) then its sucessful.

print(pr.text)              #to get or print the html code of the website.