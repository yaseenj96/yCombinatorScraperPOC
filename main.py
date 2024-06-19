from bs4 import BeautifulSoup





with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser') #lxml is another parser
print(soup.title) #Title Tag
print(soup.title.name) #Name of Title tag (title)
# print(soup.prettify)

all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
    # print(tag.getText()) #print Text
    # print(tag.get("href")) #print link within

#Find by ID
heading = soup.find(name = "h1", id = "name")
print(heading)

#Find by Class
h3_heading = soup.find_all(name="h3", class_="heading")
print(h3_heading)

#Find by ID
name = soup.select_one(selector="#name")
print(name)

##Find by selector (select all headings)
headings = soup.select(".heading")
print(headings)