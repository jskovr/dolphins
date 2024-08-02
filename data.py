import os, re, string, random
from urllib.request import urlopen

url_boy = 'https://www.prokerala.com/kids/baby-names/boy/page-1.html'
url_girl = 'http://www.prokerala.com/kids/baby-names/girl/page-1.html'
boy_names = 'boy_names.dat'
girl_names = "girl_names.dat"
genders = [(url_boy, boy_names), (url_girl, girl_names)]
name_set = set()
maximum = 150

for x in genders:

	for page in range(0, maximum+1):

		url = x[0][:51] + f"{page}" + '.html' 
		infile = urlopen(url)
		html_txt = str(infile.read())
		infile.close()

		pattern = "data-name=" # The name comes right after pattern
		for match in re.finditer(pattern, html_txt):
			str_ = html_txt[match.start()-10 : match.end()+10]
			m = re.search("[A-Z][a-z]*", str_)
			try:
				name_set.add(m.group())
			except AttributeError as e:
				pass
		print(f"{x[1]}: {page} out of {maximum} pages")

	name_set = list(name_set)
	name_set.sort()
	with open(x[1], 'w') as file:
		for name in name_set:
			file.write(f"{name}\n") # write each name to a .dat file
			# file.write(f"{name} {''.join(random.choices(string.ascii_uppercase, k=10)) }\n")
			file.write(f"{name} II\n")
			file.write(f"{name} III\n")
			file.write(f"{name} IV\n")
			file.write(f"{name} V\n")
			file.write(f"{name} VI\n")
			file.write(f"{name} VIII\n")
			file.write(f"{name} IX\n")
			file.write(f"{name} X\n")
			file.write(f"{name} XI\n")
	name_set = set()
print("Finished!")