import gspread
import string
import sys
import voteFuncs
from oauth2client.service_account import ServiceAccountCredentials

# Use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
# Find a workbook by name and open the first sheet
# Make sure you use the right name here
WORKBOOK_NAME = "Voting Form (Responses)"

if __name__ == "__main__":
	# Open the first sheet
	sheet = client.open(WORKBOOK_NAME).sheet1

	# Extracts all values as list of lists, one list per row
	list_1 = sheet.get_all_values()
	old_names = [i[1] for i in list_1][1:]

	# Dupe/Invalid Chars Removal
	invalidChars = set(string.punctuation + string.digits)
	names = []
	for s in old_names:
		if s.title() not in names and not any(char in invalidChars for char in s):
			names.append(s.title())
	
	# Temporary; if you have any names you don't want to accept, enter them here
	blacklist = []

	# Final counted votes
	final_votes = [i for i in list_1 if (i[1].title() not in blacklist and i[1].title() in names)] # remove

	candidates_a = ["Candidate A", "Candidate B", "Candidate C"]
	vote_cols_a = [2, 3, 4]
	result_a = voteFuncs.vote_3("Position A", candidates_a, vote_cols_a, final_votes)

	candidates_b = ["Candidate D", "Candidate E"]
	vote_cols_b = [5]
	result_b = voteFuncs.vote_2("Position B", candidates_b, vote_cols_b, final_votes)

	print(result_a)
	print(result_b)
