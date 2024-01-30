import requests
from bs4 import BeautifulSoup
website_url = "https://infopark.in/companies/job-search"
keywords=["php","python"]
output_file =open("job.txt","w")
res=requests.get(website_url,verify=False) 
soup = BeautifulSoup(res.text,'lxml')
jobs=soup.find_all("div",{"class":"row company-list joblist"})
for job in jobs:
    title_element = job.find("a")
    title = title_element.text
    link = title_element["href"]
    company = job.find("div",{"class":"jobs-comp-name"})
    com=company.text
    last_date = job.find("div",{"class":"job-date"})
    last=last_date.text 
    if any( word.lower() in title.lower() for word in keywords):
        print(title,link,com,last)
        output_file.write(title + "." + com + ":" + last + ":" + link + "\n\n")

