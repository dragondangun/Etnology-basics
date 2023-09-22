abstractFile = open("Abstract.html", "r", encoding="utf8")
text_to_add = abstractFile.read()
abstractFile.close()

text_to_add = text_to_add.replace('--', '—')

citeCounter = 1
point = text_to_add.find('%cite%')
while(point != -1):
    text_to_add = text_to_add[:point] + str(citeCounter) + text_to_add[point+6:]
    point = text_to_add.find('%cite%')
    citeCounter += 1

def create_link(link_pair):
    result = '\t\t\t<ul class="Nav">'
    left = '' if link_pair[0] == '' else f'\t\t\t<li class="Nav"><a href="{link_pair[0]}.html">Назад</a></li>'
    right = '' if link_pair[1] == '' else f'\t\t\t<li class="Nav"><a href="{link_pair[1]}.html">Вперёд</a></li>'
    result += f'\t{left}\n\t{right}\n\t\t\t</ul>'
    return result

page_contents = [""]

point = 0
curr_page = 0
while True:

    p_point = text_to_add.find('<p', point)
    point = text_to_add.find('<h', point)

    if(point == -1):
        page_contents[curr_page] += text_to_add[:point]
        break

    heading = int(text_to_add[point+2])
    if((p_point != -1) & (p_point < point) & (heading < 5)):
        page_contents[curr_page] += text_to_add[:point]
        curr_page+=1
        page_contents.append('')
    else:
        page_contents[curr_page] += text_to_add[:point]

    text_to_add = text_to_add[point:]
    point = 1


title = 'Основы этнологии' # Enter title
head = '<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta charset="utf-8">\n\t\t<title>Конспект '+title+'</title>\n\t\t<link rel="stylesheet" href="style.css">\n\t</head>\n\t<body>\n\t\t<div class="MyDiv">\n'
tail = '\n\t\t</div>\n\t</body>\n</html>'

page_number = len(page_contents)
names = ['index' if i == 0 else i for i in range(0, page_number)]
left_links = ['' if i == 0 else 'index' if i == 1 else f'{i-1}' for i in range(0, page_number)]
right_links = ['' if i == page_number-1 else f'{i+1}' for i in range(0, page_number)]
links = list(zip(left_links, right_links))

for i, p in enumerate(page_contents):
    mainFile = open(f"docs/{names[i]}.html", "w", encoding="utf8")
    mainFile.write(head)
    mainFile.write(p)
    mainFile.write(create_link(links[i]))
    mainFile.write(tail)
    mainFile.close()

