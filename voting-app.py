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

blacklist = [] #blacklisted names; done manually
# Arguments
if len(sys.argv) > 1:
	if sys.argv[1] == "DL":
		voteFuncs.load_names(sys.argv[2], names)
		print("Names loaded into " + sys.argv[2])
		exit()
	if sys.argv[1] == "UP-b":
		voteFuncs.get_names(sys.argv[2], blacklist)
		print("Blacklist loaded: ")
		print(blacklist)
	if sys.argv[1] == "UP-n":
		new_names = []
		voteFuncs.get_names(sys.argv[2], new_names)
		print("Names loaded: ")
		print(new_names)
		names = new_names


# Blacklisting if none provided
if len(sys.argv) < 1:
	print("The following is a list of names entered:")
	print(names)
	print("Please enter names you want to blacklist, type 'end' to end: ")
	while(1):
		var = input("Name: ")
		if var == "end":
			break
		blacklist.append(var)

	print("The following is your blacklist:")
	print(blacklist) # shows all except the empty string
	var = input("Continue? (Y/N): ")
	if var != "Y":
		print("Ending Program...")
		exit()

final_votes = [i for i in list_1 if (i[1].title() not in blacklist and i[1].title() in names)] # remove

s_candidates = ["Claudette Ramos", "Tiffany Corro", "Megan Rae Parayno"]
s_vote_cols = [2, 3, 4]
new_secretary = voteFuncs.vote_3("Secretary", s_candidates, s_vote_cols, final_votes)

i_candidates = ["Ivan Nicolas Dioso", "Gwyneth Ganigan"]
i_vote_cols = [5]
new_internal = voteFuncs.vote_2("Internal", i_candidates, i_vote_cols, final_votes)

ec_candidates = ["Noemie Li", "Johan Ortiz", "Charls Vergara"]
ec_vote_cols = [6, 7, 8]
new_ec = voteFuncs.vote_3("Event Coordinator", ec_candidates, ec_vote_cols, final_votes)

h_candidates = ["Neil Doria", "Mikee Villanueva"]
h_vote_cols = [9]
new_historian = voteFuncs.vote_2("Historian", h_candidates, h_vote_cols, final_votes)
