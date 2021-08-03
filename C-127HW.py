from bs4 import BeautifulSoup
import requests
import time
import csv

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = requests.get(start_url)

time.sleep(10)

def scrap():
    header = ["Name", "Distance", "Mass", "Radius"]
    star_data = []

    for x in range(0,444):
       soup = BeautifulSoup(browser.page_source, "html.parser")
       for ul_tag in soup.find_all("th", attrs={"class", "stars"}):
           li_tags = ul_tag.find_all("a")
           temp_list = []
           for index, li_tag in enumerate(li_tags):
               if index == 0:
                   temp_list.append(li_tag.find_all("a")[0].contents[0])
               else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
           star_data.append(temp_list)
       browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scraper2.csv", "w") as f:
       csv_writer = csv.writer(f)
       csv_writer.writerow(header)
       csv_writer.writerow(star_data)

scrap()