from html.parser import HTMLParser

class MyHTMLParser(HTMLParser): #creates a new class called MyHTMLParser and inherits attributes from HTMLParser, but changes the functions listed below
    def handle_starttag(self, tag, attrs): #extracts any start tags
        print(f'Start : {tag}')
        for attr_name, attr_value in attrs: # this tells the code to extract the attribute name and value
            print(f'-> {attr_name} > {attr_value if attr_value is not None else "None"}')
    def handle_endtag(self, tag): #extracts any end tags
        print(f'End   : {tag}')
    def handle_startendtag(self, tag, attrs): #extracts any empty tags
        print(f'Empty : {tag}')
        for attr_name, attr_value in attrs:
            print(f'-> {attr_name} > {attr_value if attr_value is not None else "None"}')

parser = MyHTMLParser() #parser is a variable name that then allows you to call methods like .feed()
lines = []

n = int(input())
for _ in range(n):
    line = input()
    lines.append(line)

parser.feed("\n".join(lines))