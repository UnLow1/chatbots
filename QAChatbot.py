import requests
import string
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup


def execute_query(query, result_page_index=0):
    fallback = 'Sorry, I cannot think of a reply for that.'

    # Google Search query results as a Python List of URLs
    search_result_list = list(search(query, tld="co.in", num=10, stop=3, pause=1))

    page = requests.get(search_result_list[result_page_index])
    tree = html.fromstring(page.content)
    soup = BeautifulSoup(page.content, features="lxml")

    article_text = ''
    article = soup.findAll('p')
    for element in article:
        article_text += element.text
    article_text = article_text.replace('\n', '')
    first_sentence = article_text.split('.')[0]
    first_sentence = first_sentence.split('?')[0]

    chars_without_whitespace = first_sentence.translate(
        {ord(c): None for c in string.whitespace}
    )

    if len(chars_without_whitespace) > 0:
        result = first_sentence
    else:
        result = fallback
    return result


if __name__ == "__main__":
    query = 'how old is samuel l jackson'
    result = execute_query(query)
    print(result)
