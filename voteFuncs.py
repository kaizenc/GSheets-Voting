# Actual Voting Functions

def vote_3(position_name, candidates, vote_cols, spreadsheet):
	"""vote_3: Implementation of the Instant Runoff Voting Algorithm
	position_name (string): name of the position or office
	candidates (string[]): list of possible candidate choices
	vote_cols (int[]): spreadsheet columns to look at
	spreadsheet (string[][]): final votes
	"""
	# Setup
	votes = {candidates[0]:0, candidates[1]:0, candidates[2]:0}
	num_of_votes = 0

	list_of_lists = [i for i in spreadsheet if (i[1].title() not in candidates and i[vote_cols[0]]!="")]

	# Count Initial Votes
	for i in list_of_lists:
		for j, col in enumerate(vote_cols):
			if i[col] == 'First':
				votes[candidates[j]] +=1
		num_of_votes +=1

	# Print winner if majority+
	possible_winner= max(votes, key=votes.get)
	if votes[possible_winner] >= num_of_votes/2:
		winner_votes = str(votes[possible_winner])
		return f'Your new {position_name} is {possible_winner} with {winner_votes} votes (out of {num_of_votes})'

	# Remove loser
	loser = min(votes, key=votes.get)
	del votes[loser]
	ix_of_loser = 0
	for i, name in enumerate(candidates):
		if name == loser:
			ix_of_loser = vote_cols[i]
			break

	# Runoff Count
	list_of_lists = [x for x in list_of_lists if x[ix_of_loser] == 'First']
	for i in list_of_lists:
		for j, col in enumerate(vote_cols):
			if i[col] == 'Second':
				votes[candidates[j]] +=1

	# Print winner
	winner = max(votes, key=votes.get)
	winner_votes = str(votes[winner])
	return f'Your new {position_name} is {winner} with {winner_votes} votes (out of {num_of_votes})'

def vote_2(position_name, candidates, vote_col, spreadsheet):
	# Setup
	votes = {candidates[0]:0, candidates[1]:0}
	num_of_votes = 0
	col1 = vote_col[0]
	list_of_lists = [i for i in spreadsheet if (i[1].title() not in candidates and i[col1]!="")]

	# Count Initial Votes
	for i in list_of_lists:
		for key in votes:
			if i[col1] == key:
				votes[key] +=1
		num_of_votes +=1

	# Print Winner
	winner = max(votes, key=votes.get)
	winner_votes = str(votes[winner])
	return f'Your new {position_name} is {winner} with {winner_votes} votes (out of {num_of_votes})'

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
