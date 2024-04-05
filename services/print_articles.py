def print_articles(articles) -> str:
    text_for_print = ""
    count = 1
    for article in articles:
        text_for_print += str(count) + ") " + article[1] + "\n"
        count += 1

    return text_for_print
