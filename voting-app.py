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
WORKBOOK_NAME = "POH E-BOARD 2019 Voting (Responses)"

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
	
	print(names)
	print("Press any key to continue")
	temp = input()
	
	# Temporary; if you have any names you don't want to accept, enter them here
	blacklist = []

	# Final counted votes
	final_votes = [i for i in list_1 if (i[1].title() not in blacklist and i[1].title() in names)] # remove

	ec_candidates = ['Andrew Jreza', 'Justin Wu']
	ec_vote_cols = [2]
	ec_result = voteFuncs.vote_2("Event Coordinator", ec_candidates, ec_vote_cols, final_votes)

	ePR_candidates = ['Marie Guanzon', 'Andrew Jreza', 'JD Pacamarra']
	ePR_vote_cols = [3, 4, 5]
	ePR_result = voteFuncs.vote_3("External PR", ePR_candidates, ePR_vote_cols, final_votes)

	# TODO: Implement vote_4
	# iPR_candidates = ['Marie Guanzon', 'Mara Lopez', 'David Luu', 'Andy + Raymond']
	# iPR_vote_cols = [6, 7, 8, 9]
	# iPR_result = voteFuncs.vote_4("Internal PR", iPR_candidates, iPR_vote_cols, final_votes)

	vp_candidates = ['Sam Hidalgo', 'Noemie Li']
	vp_vote_cols = [10]
	vp_result = voteFuncs.vote_2("Vice President", vp_candidates, vp_vote_cols, final_votes)

	print(ec_result)
	print(ePR_result)
	print(vp_result)
