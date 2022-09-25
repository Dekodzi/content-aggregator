import requests
from bs4 import BeautifulSoup

class Website:
    page = None
    identification_text = None
    markups = None
    titles = list()
    links = list()

    def __init__(self, url, name, markups):
        self.page = requests.get(url)
        self.identification_text = name
        self.markups = markups
        self.__parse_page()
    
    def __parse_page(self):
        soup = BeautifulSoup(self.page.content, "html.parser")
        headings = soup.find_all(self.markups[0], class_=self.identification_text[0])
        for i in range(0, 4):
            current_heading = headings[i]
            main_title = current_heading.find(self.markups[1], class_=self.identification_text[1]).text.strip()
            link = current_heading.find('a').get("href")
            self.titles.append(main_title)
            self.links.append(link)
    
    def get_titles(self):
        return self.titles
    
    def get_links(self):
        return self.links

temp_list = ["cb-meta cb-article-meta meta", "title cb-post-title"]
temp_list_2 = ["div", "h2"]
european_coffee_trip = Website("https://europeancoffeetrip.com/magazine/", temp_list , temp_list_2)

temp_list = ["research-listing-wrapper", "h2-listing-title"]
temp_list_2 = ["div", "h2"]
coffee_and_health = Website("https://www.coffeeandhealth.org/research", temp_list , temp_list_2)

temp_list = ["col-sm-8", ""]
temp_list_2 = ["div", "h1"]
daily_coffee_news = Website("https://dailycoffeenews.com/", temp_list , temp_list_2)

temp_list = ["elementor-post__text", "elementor-post__title"]
temp_list_2 = ["div", "h3"]
the_way_to_coffee = Website("https://www.thewaytocoffee.com/", temp_list , temp_list_2)

websites = [european_coffee_trip, coffee_and_health, daily_coffee_news, the_way_to_coffee]
