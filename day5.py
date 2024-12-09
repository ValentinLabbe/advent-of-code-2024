file = open('day5.txt', 'r')
# file = open('sample.txt', 'r')
lines = file.read()
file.close()

rules_section, pages_section = lines.split('\n\n')

def getPages():
    return [pages.split(',') for pages in pages_section.split()]

def getRulesDict():
    rules_dict = {}
    for rules in rules_section.split():
        rule = rules.split('|')
        rules_dict.setdefault(rule[0], set()).add(rule[1])
    return rules_dict

def sortPages(pages, rules):
    for i in range(1, len(pages)):
        for j in range(len(pages) - 1):
            if pages[j + 1] in rules.get(pages[j], []):
                temp_page = pages[j]
                pages[j] = pages[j + 1]
                pages[j + 1] = temp_page
    return pages[::-1]

def getMiddlePage(pages):
    return int(pages[len(pages) / 2])

def main():
    rules = getRulesDict()
    correctly_sorted_pages_total = 0
    wrongly_sorted_pages_total = 0

    for pages in getPages():
        sorted_pages = sortPages(list(pages), rules) 
        if pages == sorted_pages:
            correctly_sorted_pages_total += getMiddlePage(sorted_pages)
        else:
            wrongly_sorted_pages_total += getMiddlePage(sorted_pages)

    return (correctly_sorted_pages_total, wrongly_sorted_pages_total)

print(main())