import os.path
import PyPDF2
import os
import pandas as pd
import re
import textract


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import spacy
import xlsxwriter


path = '/home/palash/exadatum/ost/CaseStudy'

folder = os.fsencode(path)

filenames = []

for file in os.listdir(folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.pdf', '.doc') ):
        filenames.append(filename)

all_fe = []
all_e = []
all_contacts = []
all_skills = []
all_file_address = []
all_file_content = []

for each_file in filenames:
	file = each_file
	f = open('CaseStudy/' + file, 'r+')
	file_title = os.path.basename(f.name)
	file_name = f.name

	# no need for file extention here 
	available_extention = [".csv", ".doc", ".docx", ".eml", ".epub", ".gif", ".htm", ".html", ".jpeg", 
				".jpg", ".json", ".log", ".mp3", ".msg", ".odt", ".ogg", ".pdf", ".png", 
				".pptx", ".ps", ".psv", ".rtf", ".tff", ".tif", ".tiff", ".tsv", ".txt", ".wav", ".xls", ".xlsx"]
	extension = os.path.splitext(file_name)[1]

	if extension in available_extention:
		text = textract.process(file_name).decode("utf-8") 
		lst = text.split("\n")
		candidate_email_ids = [i for i in lst if i.__contains__("@")]

		all_email_ids = []
		if candidate_email_ids:
			for candidate in candidate_email_ids:
				if candidate.__contains__("@"):
					email_ids = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", candidate)
					if not email_ids:
						email_ids = re.findall('\S+@\S+',candidate)

					if email_ids[0] not in all_email_ids:
						all_email_ids.append(email_ids[0])
		# print(all_email_ids)

		contact_number = set(re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{10,}[0-9]', text))

		known_lang = ["c","c++", "java", "css", "linux", "java script", "vb","vb script", 
		"ajax", "aws", "db2", "python", "perl", "shell scripting", "cloud", "devops", "automation", 
		"s3", "git", "docker", "Jenkins", "kubernetes", "web & domain hosting", "mysql",
		"agile methodologies", "go", "system administration", "sql", "php", "html"] #.Net, VB .Net, VB 6.0, Java Script, VB Script, AJAX, Unix scripting

		all_technologies = []
	 

		nlp = spacy.load('en')
		
		doc = nlp(text)
		for ent in doc.ents:
			# print(ent)
			# import pdb
			# pdb.set_trace()
			if str(ent).lower() in known_lang: #or str(ent).__contains__([i for i in known_lang]):
				if str(ent) not in all_technologies:
					all_technologies.append(str(ent))
				# print("+++++++++++++++", ent)
			# if ent.label_ in ['GPE', 'LOC']:
			# 	print(ent.text, ent.start_char, ent.end_char, ent.label_)

		


		# for s in doc.sents:
		# 	if s.text.lower().__contains__("python"):
		# 		all_technologies.append(str(s.text).strip("\n"))

		file_name_email_id = ""
		for email_id in all_email_ids:
			for i in list(email_id):
				if i in list(file_title):
					file_name_email_id = file_name_email_id + i

		# print(file_name_email_id)

		file_address = os.path.dirname(os.path.abspath(__file__))
		##############################################
		file_content = text.replace("\n", " ").replace("\x0c", " ").replace("•", "").replace("    ", "").replace("|","").strip()
		cdata = {
			"file_email" : file_name_email_id,
			"email" : all_email_ids,
			"contact number" : contact_number,
			"skills" : all_technologies,
			"file_address" : file_address,
			"file_content" : file_content
		}

		all_fe.append(file_name_email_id)
		all_e.append(all_email_ids)
		all_contacts.append(contact_number)
		all_skills.append(all_technologies)
		all_file_address.append(file_address)
		all_file_content.append(file_content)
		# print(cdata)
				
		# print(contact_number, all_technologies, all_email_ids)

	else:
		print("Unknown file")


# print(all_fe)

data = [
		{'file_email': all_fe},
		{'email': all_fe},
		{'contact number': all_contacts},
		{'skills' : all_skills},
		{'file_address' : all_file_address},
		{'file_content' : all_file_content}
		]

final_df = pd.DataFrame()
for id in range(0,len(data)):
	df = pd.DataFrame.from_dict(data[id])
	final_df = pd.concat([final_df, df], axis=1)

# print(final_df)
final_df.to_excel('final_test.xlsx')










































# import os.path
# import PyPDF2

# import pandas as pd
# import re
# import textract


# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import sent_tokenize
# import spacy
# import xlsxwriter


# f = open('CaseStudy/cute.aarts.gmail@naukri.comcuteDotaarts@gmailDotcom.doc', 'r+')



# file_title = os.path.basename(f.name)


# file_name = f.name

# available_extention = [".csv", ".doc", ".docx", ".eml", ".epub", ".gif", ".htm", ".html", ".jpeg", 
# 			".jpg", ".json", ".log", ".mp3", ".msg", ".odt", ".ogg", ".pdf", ".png", 
# 			".pptx", ".ps", ".psv", ".rtf", ".tff", ".tif", ".tiff", ".tsv", ".txt", ".wav", ".xls", ".xlsx"]
# extension = os.path.splitext(file_name)[1]

# if extension in available_extention:
# 	text = textract.process(file_name).decode("utf-8") 
# 	lst = text.split("\n")
# 	candidate_email_ids = [i for i in lst if i.__contains__("@")]

# 	all_email_ids = []
# 	if candidate_email_ids:
# 		for candidate in candidate_email_ids:
# 			if candidate.__contains__("@"):
# 				email_ids = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", candidate)
# 				if not email_ids:
# 					email_ids = re.findall('\S+@\S+',candidate)

# 				if email_ids[0] not in all_email_ids:
# 					all_email_ids.append(email_ids[0])
# 	# print(all_email_ids)

# 	contact_number = set(re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{10,}[0-9]', text))

# 	known_lang = ["c","c++", "java", "css", "linux", "java script", "vb","vb script", 
# 	"ajax", "aws", "db2", "python", "perl", "shell scripting", "cloud", "devops", "automation", 
# 	"s3", "git", "docker", "Jenkins", "kubernetes", "web & domain hosting", "mysql",
# 	"agile methodologies", "go", "system administration", "sql", "php", "html"] #.Net, VB .Net, VB 6.0, Java Script, VB Script, AJAX, Unix scripting

# 	all_technologies = []
 

# 	nlp = spacy.load('en')
	
# 	doc = nlp(text)
# 	for ent in doc.ents:
		
# 		if str(ent).lower() in known_lang: #or str(ent).__contains__([i for i in known_lang]):
# 			if str(ent) not in all_technologies:
# 				all_technologies.append(str(ent))
		
	

# 	file_name_email_id = ""
# 	for email_id in all_email_ids:
# 		for i in list(email_id):
# 			if i in list(file_title):
# 				file_name_email_id = file_name_email_id + i

# 	cdata = {
# 		"file_email" : file_name_email_id,
# 		"email" : all_email_ids,
# 		"contact number" : contact_number,
# 		"skills" : all_technologies
# 	}

# 	check = text.replace("\n", " ").replace("\x0c", " ").replace("•", "").replace("    ", "").replace("|","").strip()

# 	import pdb
# 	pdb.set_trace()

# 	print(cdata)
	
# else:
# 	print("Unknown file")
















































# import re
# import textract


# import os.path



# file_name = "CaseStudy/tripathi.vineetbaba.gmail@naukri.comtripathiDotvineetbaba@gmailDotcom.pdf"

# available_extention = [".csv", ".doc", ".docx", ".eml", ".epub", ".gif", ".htm", ".html", ".jpeg", 
# 			".jpg", ".json", ".log", ".mp3", ".msg", ".odt", ".ogg", ".pdf", ".png", 
# 			".pptx", ".ps", ".psv", ".rtf", ".tff", ".tif", ".tiff", ".tsv", ".txt", ".wav", ".xls", ".xlsx"]
# extension = os.path.splitext(file_name)[1]

# if extension in available_extention:
# 	text = textract.process(file_name).decode("utf-8") 
# 	lst = text.split("\n")
# 	candidate_email_ids = [i for i in lst if i.__contains__("@")]

# 	all_email_ids = []
# 	if candidate_email_ids:
# 		for candidate in candidate_email_ids:
# 			if candidate.__contains__("@"):
# 				email_ids = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", candidate)
# 				if not email_ids:
# 					email_ids = re.findall('\S+@\S+',candidate)
# 				all_email_ids.append(email_ids[0])
# 	print(all_email_ids)

# 	contact_number = set(re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{10,}[0-9]', text))
# else:
# 	print("Unknown file")