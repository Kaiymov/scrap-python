import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from fake_useragent import UserAgent

ua = UserAgent()

file_save = 0
# WRITE NEW EXEL FILE
row = 2
book = Workbook()
sheet = book.active

with open('seconom24.txt') as file:
    urls = [url.strip() for url in file.readlines()]
    
    for url in urls:
        response = requests.get(url, headers={'User-Agent': ua.random})
        result = response.content
        soup = BeautifulSoup(result, 'lxml')

        title = soup.find('h1', itemprop='name').get_text(strip=True)
        price = soup.find('div', class_='price-block').find('span', class_='totalPrice').get_text(strip=True)
        category = soup.find('ul', class_='bread-crumbs').get_text(strip=True)
        

        sheet['A1'].value = 'URL'
        sheet['B1'].value = 'TITLE'
        sheet['C1'].value = 'CATEGORY'
        sheet['D1'].value = 'PRICE'

        sheet[row][0].value = url
        sheet[row][1].value = title
        sheet[row][2].value = category
        sheet[row][3].value = price

        file_save += 1
        print(f'loading...{file_save}')
                
        row += 1

# SAVE EXEL FILE
book.save('seconom24.xlsx')
book.close()
