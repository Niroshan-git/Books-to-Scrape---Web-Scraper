#Basic Website Scraping

from bs4 import BeautifulSoup
import requests
import pandas as pd

# Connect to website

current_page = 1

data = []

# print(soup.title.text)
proceed = True

while(proceed):
    print(f"Currently Scraping Page:{str(current_page)}")

    url = "https://books.toscrape.com/catalogue/page-"+ str(current_page)+".html"

    page =  requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")

    if soup.title.text == "404 Not Found":
        proceed = False
    else:

        all_books = soup.find_all("li", class_= "col-xs-6 col-sm-4 col-md-3 col-lg-3")
        # print(all_books)

        for book in all_books:
            item =  {}

            item['Title'] = book.find("img").attrs["alt"]

            item['Link'] = book.find("a").attrs["href"]

            item['Price'] =  book.find("p",  class_ = "price_color").text[2:]

            item['Stock'] = book.find("p", class_= "instock availability").text.strip()

             # Extract the rating
            star_rating_tag = book.find("p", class_="star-rating")
            rating_class = star_rating_tag.get("class")
            # The second class name represents the star rating, e.g., "Four", "Five", etc.
            rating_text = rating_class[1]
            rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
            item['Rating'] = rating_map.get(rating_text, 0)  # Convert to numerical value

             # Make a request to the detailed page to extract the category
            detailed_page_url = "https://books.toscrape.com/catalogue/" + item['Link']
            detailed_page = requests.get(detailed_page_url)
            detailed_soup = BeautifulSoup(detailed_page.text, "html.parser")

            # Extract the category from the breadcrumb navigation
            breadcrumb = detailed_soup.find("ul", class_="breadcrumb")
            category = breadcrumb.find_all("li")[2].find("a").text.strip()  # Get the text from the <a> tag inside the third <li>
            item['Category'] = category



            data.append(item)

            # # Print first 2 details for checking
            # if len(data) <= 2:
            #     print(item)


    current_page += 1 
    
# Convert the data into a DataFrame and save it as a JSON file
df = pd.DataFrame(data)
df.to_json("books.json", orient="records")
df.to_csv("books.csv")

print("Scraping complete. Data saved to books")
 