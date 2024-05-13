def domain_name(url):
    damn = url.replace('http://','').replace('https://','').replace('www.','')
    return damn.split('.')[0]




print(domain_name("http://google.com"), "google")
print(domain_name("http://google.co.jp"), "google")
print(domain_name("https://123.net"), "123")
print(domain_name("https://hyphen-site.org"), "hyphen-site")
print(domain_name("http://codewars.com"), "codewars")
print(domain_name("www.xakep.ru"), "xakep")
print(domain_name("https://youtube.com"), "youtube")
print(domain_name("http://www.codewars.com/kata/"), "codewars")
print(domain_name("icann.org"), "icann")