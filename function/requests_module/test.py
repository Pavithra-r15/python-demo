import requests
url= url="https://www.weather-forecast.com/"
def scrape_website(url):
    response = requests.get(url)
    data=response.text
    #print(data)
    with open("default.html", 'w', encoding='utf-8') as file:
            file.write(data)

scrape_website(url)