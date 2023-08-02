from bs4 import BeautifulSoup
import requests
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "sheet2"

print("sheet name is renamed as: " + sheet.title)
sheet.append(['movies name','ranks','rating','years'])


try:
    source = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
    source.raise_for_status()

    soup =BeautifulSoup(source.text,"html.parser")

    movies = soup.find('tbody',class_='lister-list').find_all('tr')

    for movie in movies:
        name= movie .find('td',class_='titleColumn').a.text
        rank= movie.find('td',class_='titleColumn').get_text(strip=True).split('.')[0]
        rating=movie.find('td',class_='ratingColumn imdbRating').strong.text
        year=movie.find('td',class_='titleColumn').span.text.strip('()')

        print(name,rank,rating,year)
        sheet.append([name,rank,rating,year])
except Exception  as e:
    print(e)

wb.save('imdbdata.xlsx')