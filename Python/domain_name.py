import re
def domain_name(url):
    print(re.search(r"http(?:s|):\/\/(?:www\.|)(.*)\.", url).group(1))
    return re.search(r"http(?:s|):\/\/(?:www\.|)(.*)\.", url).group(1)
domain_name("http://github.com/carbonfive/raygun")