from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://br.linkedin.com/jobs/junior-python-vagas?keywords=Junior%20Python&location=Brasil&locationId=&geoId=106057199&f_TPR=r86400&position=1&pageNum=0').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_="base-search-card__info")
for job in jobs:
    try:
        published_date = job.find('time', class_= "job-search-card__listdate--new").text.strip()
        job_title = job.find('h3', class_="base-search-card__title").text.strip()
        company_name = job.find('a', class_="hidden-nested-link").text.strip()
        company_url = job.find('a', class_="hidden-nested-link").get('href')
    except AttributeError as erro:
        pass
    print(f'''-> Job title: {job_title}
-> Company name: {company_name}
-> Published date: {published_date}
-> Company URL: {company_url}''')

    print()