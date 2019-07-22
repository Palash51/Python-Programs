from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import re

import datefinder
import datetime
from nltk.corpus import words

from airline import AllAirlines


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    # print(text)
    return text



# print(convert_pdf_to_txt('sample_ticket.pdf'))

def get_travelling_dates(string_with_dates):
	# print(string_with_dates)
	matches = datefinder.find_dates(string_with_dates)

	time_lst = []
	all_time = []
	for match in matches:
		NO_TIME = datetime.time(0) #or datetime.datetime.now().time()
		all_time.append(match)
		if  match.time() == NO_TIME:
			continue
		else:
			time_lst.append(match)
	# print(all_time)
	return time_lst
	# print(time_lst)



def get_data(file):

	full_string = convert_pdf_to_txt(file)

	if full_string.count("\n") > 1:
		word_list = full_string.split("\n")
	else:
		word_list = full_string.split()

	# import pdb
	# pdb.set_trace()

	new = [x for x in word_list if x not in '']
	# print(word_list)
	# # print(type(word_list))
	# # clean_list = [x for x in word_list if x is not None]
	# # print(' '.join(word_list).split())
	# sub = "Mr"
	# if sub in word_list:
	# 	print(sub)
	passanger_details = {
		"name": re.sub("[\(\[].*?[\)\]]", "", " ".join([x for x in new if x.__contains__('Mr')])).strip()
	}
	# print(passanger_details)
	# print(new)
	date_data = []
	for date in ['Tue', 'Wed', 'Thu', 'Fri', 'Sat','Mon', 'Sun']:
		trip_date = ([x for x in new if x.__contains__(''.join(date))])
		if trip_date:
			date_data.append(trip_date)
	
	# print(date_data)	
	# print(("".join(date_data)))

	travellig_date = get_travelling_dates(full_string)
	# print(travellig_date)

	passanger_details.update({
		"time": travellig_date
	})

	ALL_AIRLINE = ['JET AIRWAYS', 'go air', 'indigo', 'air india', 'air asia']
	# ALL_AIRLINE = AllAirlines.get_airlines()
	PNR = []
	new_list = full_string.replace(",", "\n").split("\n")
	pnr_word = [x for x in new_list if x not in '']
	Airlines = []
	# print(pnr_word)
	for i in pnr_word:
		# print(i)
		i = i.strip()
		if i.lower() not in words.words() and i.isupper() and len(i)==6 and re.match("^[a-zA-Z0-9_]*$", i):
			if i not in PNR:
				PNR.append(i)

		i = i.lower()
		if i.strip() in ALL_AIRLINE:
			Airlines.append(i)




	passanger_details.update({
		"PNR": PNR,
		"Airlines" : Airlines	
		})


	# import pdb
	# pdb.set_trace()
	
	print(passanger_details)







get_data('sample_ticket.pdf')




































###################################################################################

############
## OLD ##
###########

####################################################################################


# from tabula import read_pdf

# df = read_pdf('mmt.pdf', output_format="json")
# print(df)
# import pdb
# pdb.set_trace()

##############################################################

# import requests 

# def pdfToTable(PDFfilename, apiKey, fileExt, downloadDir):
# 	# PDFfilename = 'example.pdf'
# 	fileData = (PDFfilename, open(PDFfilename, 'rb')) #"rb" stands for "read bytes"
# 	files = {'f': fileData}
# 	# apiKey = "vhnh77dypzrf" 
# 	fileExt = "xlsx-multiple" #format/file extension of final document
# 	postUrl = "https://pdftables.com/api?key={0}&format={1}".format(apiKey, fileExt)
# 	#the .format puts value of apiKey where {0} is, etc
# 	response = requests.post(postUrl, files=files)
# 	response.raise_for_status() # ensure we notice bad responses
# 	import pdb
# 	pdb.set_trace()
# 	# downloadDir = "example.csv" #directory where you want your file downloaded to 
# 	with open(downloadDir, "wb") as f:
# 	    f.write(response.content) #write data to csv



# print(pdfToTable('sample_ticket.pdf', 'vhnh77dypzrf', '.xlsx', 'example1.xlsx'))


#############################################################################


# import pandas as pd
# import tabula
# files = "mmt.pdf"
# path = files
# df = tabula.read_pdf(path, pages = '1', multiple_tables = True)
# # print(df)
# import pdb
# pdb.set_trace()
# mydict = dict(zip(df.AIRLINE, df.value))
# print(mydict)





# import xlrd 
  
# loc = ("example.xlsx") 
  
# wb = xlrd.open_workbook(loc) 
# sheet = wb.sheet_by_index(0) 
  
# # For row 0 and column 0 
# sheet.cell_value(0, 0) 
# import pdb
# pdb.set_trace()
  
# for i in range(sheet.ncols): 
#     print(sheet.cell_value(0, i)) 



# import xlrd

# ExcelFileName= 'example.xlsx'
# workbook = xlrd.open_workbook(ExcelFileName)
# worksheet = workbook.sheet_by_name("Sheet1") # We need to read the data 
# #from the Excel sheet named "Sheet1"


# num_rows = worksheet.nrows #Number of Rows
# num_cols = worksheet.ncols #Number of Columns

# result_data =[]
# for curr_row in range(0, num_rows, 1):
# 	row_data = []
# 	for curr_col in range(0, num_cols, 1):
# 		data = worksheet.cell_value(curr_row, curr_col) # Read the data in the current cell
# 		row_data.append(data)
# 	result_data.append(row_data)

# print(result_data)





