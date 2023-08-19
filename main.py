import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

"""
    The above code defines several functions that extract specific information from a BeautifulSoup
    object representing a job listing.
    
    :param soup: The parameter "soup" is a BeautifulSoup object that represents the HTML of a webpage.
    It is used to navigate and extract information from the HTML structure of the webpage
    :return: The functions are returning different information extracted from the provided BeautifulSoup
    object (soup). The information being returned includes the job title, location, posted time, level,
    requirements, posted by, availability, and description of the job.
"""


def get_title(soup):
    
    try:
        # Outer Tag Object
        title = soup.find("h3", attrs={"class":'no-margin-top-'})
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

def get_location(soup):
    try:
        # Outer Tag Object
        title = soup.find("li", attrs={"class":'margin-right-10'})
        
        # Inner NavigatableString Object
        title_value = title.find_all("span")[1].text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

def get_posted_time(soup):
    try:
        # Outer Tag Object
        title = soup.find("li", attrs={"class":'tooltips margin-right-10'})
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

def get_level(soup):
    try:
        # Outer Tag Object
        title = soup.find_all("li", attrs={"class":'tooltips margin-right-10'})[1]
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

def get_requires(soup):
    try:
        # Outer Tag Object
        title = soup.find_all("li", attrs={"class":'tooltips margin-right-10'})[2]
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

def get_posted_by(soup):
    try:
        # Outer Tag Object
        title = soup.find_all("li", attrs={"class":'tooltips margin-right-10'})[3]
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

def get_availablity(soup):
    try:
        # Outer Tag Object
        title = soup.find_all("li", attrs={"class":'tooltips margin-right-10'})[6]
        title2 = soup.find_all("li", attrs={"class":'tooltips margin-right-10'})[7]
        title3 = soup.find_all("li", attrs={"class":'tooltips margin-right-10'})[8]
        # Inner NavigatableString Object
        title_value = title.text
        title_value2 = title2.text
        title_value3 = title3.text

        res = title_value + title_value2 + title_value3

        # Title as a string value
        title_string = res.strip()

    except AttributeError:
        title_string = ""

    return title_string

def get_description(soup):
    try:
        # Outer Tag Object
        title = soup.find("p", attrs={"class":'job-description'})
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string


"""
The code you provided is a Python script that scrapes job listings from the website
"https://www.teacheron.com/tutor-jobs" and saves the extracted information into a CSV file named
"data.csv".
"""


if __name__ == '__main__':
    url = "https://www.teacheron.com/tutor-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    links_list = []
    links = soup.find_all('h3', attrs={'class': 'no-margin-top'})

    d = {"Title": [], "Location": [], "Posted":[], "Level": [], "Requires":[], "Posted by":[],"Availablity":[], "Description":[]}

    # for getting link and store it in list
    for link in links:
        a = link.find('a')
        temp = a.attrs["href"]
        links_list.append(temp)

    # treverse all the webpages in list
    for link in links:
        # print(link)
        a = link.find('a')
        temp = a.attrs["href"]
        # print(temp)

        new_webpage = requests.get(temp)
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

        d['Title'].append(get_title(new_soup))
        d['Location'].append(get_location(new_soup))
        d['Posted'].append(get_posted_time(new_soup))
        d['Level'].append(get_level(new_soup))
        d['Requires'].append(get_requires(new_soup))
        d['Posted by'].append(get_posted_by(new_soup))
        d['Availablity'].append(get_availablity(new_soup))
        d['Description'].append(get_description(new_soup))

    df = pd.DataFrame.from_dict(d)
    df['Title'].replace('', np.nan, inplace=True)
    df = df.dropna(subset=['Title'])
    df.to_csv("data.csv", header=True, index=False)




    # for testing purposes

    # new_webpage = requests.get("https://www.teacheron.com/teacher-job/4goD")
    # new_soup = BeautifulSoup(new_webpage.content, "html.parser")

    # print(get_description(new_soup))