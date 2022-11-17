from bs4 import BeautifulSoup
from rest_framework.response import Response
import requests


class ScrapRestaurants:

    def chicken_republic():
        url = "https://www.chicken-republic.com/menu/"
        try:
            page = requests.get(url=url)
        except requests.exceptions.ConnectionError:
            return "Internet connection is lost"

        menu = BeautifulSoup(page.text, "html.parser")
        print(menu)
        if not menu: 
            return "no menu found"
        company_ = menu.findAll('div',class_="totalbusiness-logo-inner")
        for line in company_:
            tag = line.find('img')
            company_logo = tag.get('src')

        package_details = menu.findAll('div', class_="wpcp-slide-image")
        # print('COMPANY LOGO ===> ')
        

    
        # company_logo = company_.findChild('img')
        # if not company_logo:
        #     print("no logo found")
        # else:
        #     print(company_logo)
        #     return company_logo

        

            
        #     link_of_logo.append(tag.get('img'))
        # return link_of_music