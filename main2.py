from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/news")

# print(response.text)

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

links = soup.find_all(name="span", class_ = "titleline")
article_texts = []
article_links = []
for link in links:
    title = link.select("a")[0].getText()
    articleLink = link.select("a")[0].get("href")
    article_texts.append(title)
    article_links.append(articleLink)

#List comprehension -> Converting all text scores to numbers in list
article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_scores)

#Get index of maximum score link =>
index_max = max(range(len(article_scores)), key=article_scores.__getitem__)
print(f"The top news story of the day is {article_texts[index_max]}, ({article_links[index_max]}), with a score of {article_scores[index_max]}")
print(article_scores[index_max])
# titles = soup.select("td span a")


