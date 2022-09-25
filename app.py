from flask import Flask, render_template
import scraper as scrp

app = Flask(__name__)

@app.route('/')
def generate():
    titles = get_headings()
    links = get_urls()
    return render_template("index.html", lato_font="http://fonts.googleapis.com/css?family=Lato&subset=latin,latin-ext", dmsans_font="https://fonts.googleapis.com/css2?family=DM+Sans", titles=titles, links=links)


def get_headings():
    headings = list()
    temp = list()
    temp.append(scrp.european_coffee_trip.get_titles())
    temp.append(scrp.coffee_and_health.get_titles())
    temp.append(scrp.daily_coffee_news.get_titles())
    temp.append(scrp.the_way_to_coffee.get_titles())
    for sublist in temp:
        for elem in sublist:
            headings.append(elem)
    return headings


def get_urls():
    links = list()
    temp = list()
    temp.append(scrp.european_coffee_trip.get_links())
    temp.append(scrp.coffee_and_health.get_links())
    temp.append(scrp.daily_coffee_news.get_links())
    temp.append(scrp.the_way_to_coffee.get_links())
    for sublist in temp:
        for elem in sublist:
            links.append(elem)
    return links
