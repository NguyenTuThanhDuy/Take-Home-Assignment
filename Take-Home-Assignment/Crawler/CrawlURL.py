from googlesearch import search
import re
def crawlURLBaseOnTopBranch():
    query = "macbook pro 2020 m1 16gb 256gb"
    links = {}
    top_branch = ['gearvn','didongviet','thegioididong','fptshop','cellphones']
    #write query search on google and get URL , parse to get top branches URL
    for i in search(query,tld='co.in',num=10,stop=10,pause=2):
        s = i.replace('www.','')
        start = s.find("https://") + len("https://")
        if(s.find(".com") != -1):
            end = s.find(".com")
        else:
            end = s.find(".vn")
        if(s[start:end] in top_branch):
            links.update({s[start:end]:i})
    return links
