import xml.etree.ElementTree as ET

tree = ET.parse(r'D:\_proj\19_21_szkolenie\dane\movies.xml')
root = tree.getroot()
print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag, child.attrib)

print([elem.tag for elem in root.iter()])

for movie in root.iter('movie'):
    print(movie.attrib)

for desc in root.iter('description'):
    print(desc.text)

for movie in root.findall("./genre/decade/movie/[year='2000']"):
    print(movie.attrib)