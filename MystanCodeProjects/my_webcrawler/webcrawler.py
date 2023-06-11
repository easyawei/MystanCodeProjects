"""
File: webcrawler.py
Name: chaowei hsieh
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        tags = soup.find_all("table", {"class": "t-stripe"})

        total_male = 0
        total_female = 0

        for tag in tags:
            score = tag.tbody.text.split()    # ['1', 'Noah', '183,172', 'Emma', '194,917',...]
            score_len = len(score[0:1000])    # ['1', 'Noah', '183,172',..., 'Izabella', '16,032']

            for i in range(score_len):
                data_index = i % 5            # 0, 1, 2, 3, 4, 5

                if data_index == 2:           # e.g. Noah
                    score_new = score[i].split(',')
                    total_male += int(score_new[0]+score_new[1])

                if data_index == 4:           # e.g. Emma
                    score_new = score[i].split(',')
                    total_female += int(score_new[0]+score_new[1])

        print("Male Number: " + str(total_male))
        print("Female Number: " + str(total_female))


if __name__ == '__main__':
    main()
