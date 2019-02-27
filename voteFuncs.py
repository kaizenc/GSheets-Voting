# Actual Voting Functions

def vote_3(position_name, candidates, vote_cols, spreadsheet):
	"""vote_3: Implementation of the Instant Runoff Voting Algorithm
	position_name (string): name of the position or office
	candidates (string[]): list of possible candidate choices
	vote_cols (int[]): spreadsheet columns to look at
	spreadsheet (string[][]): final votes
	"""
	# Setup
	winner = ["Your new", position_name, "is:", "", "with", "", "votes (out of", ""]
	votes = {candidates[0]:0, candidates[1]:0, candidates[2]:0}
	num_of_votes = 0
	col1 = vote_cols[0]
	col2 = vote_cols[1]

	list_of_lists = [i for i in spreadsheet if (i[1].title() not in candidates and i[col1]!="")]

	# Count Initial Votes
	for i in list_of_lists:
		for key in votes:
			if i[col1] == key:
				votes[key] +=1
		num_of_votes +=1

	winner[-1] = str(num_of_votes)+")"

	# Print winner if majority+
	possible_max = max(votes, key=votes.get)
	if votes[possible_max] >= num_of_votes/2:
		winner[3] = possible_max
		winner[5] = str(votes[possible_max])
		return winner

	# Remove loser
	loser = min(votes, key=votes.get)
	del votes[loser]

	# Runoff Count
	for i in list_of_lists:
		for key in votes:
			if i[col1] == loser and i[col2] == key:
				votes[key] +=1

	# Print winner
	winner[3] = max(votes, key=votes.get)
	winner[5] = str(votes[winner[3]])
	return winner

def vote_2(position_name, candidates, vote_col, spreadsheet):
	# Setup
	winner = ["Your new", position_name, "is:", "", "with", "", "votes (out of", ""]
	votes = {candidates[0]:0, candidates[1]:0}
	num_of_votes = 0
	col1 = vote_col[0]
	list_of_lists = [i for i in spreadsheet if (i[2].title() not in candidates and i[col1]!="")]

	# Count Initial Votes
	for i in list_of_lists:
		for key in votes:
			if i[col1] == key:
				votes[key] +=1
		num_of_votes +=1

	winner[-1] = str(num_of_votes)+")"

	# Print Winner
	winner[3] = max(votes, key=votes.get)
	winner[5] = str(votes[winner[3]])
	return winner

def load_names(filename, names):
	fh = open(filename, "w")
	for name in names:
		fh.write(name + " \n")
	fh.close()

def get_names(filename, blacklist):
	fh = open(filename, "r")
	for line in fh:
		blacklist.append(line[:-1])
	fh.close()
