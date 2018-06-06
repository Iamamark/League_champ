import cassiopeia as cass
cass.set_riot_api_key("RGAPI-34c1598d-d227-4396-9847-1bd4da688492")
cass.set_default_region('NA')
champions = cass.get_champions()

champ_dict = {}

for champ in champions: 
	champ_dict[champ.name.lower()] = champ

def contains_champ(comment):
	lst = comment.lower().split()
	for word in lst:
		if word in champ_dict:
			return True
	return False

def champ_list(comment):
	lst = comment.lower().split()
	result = []
	for word in lst:
		if word in champ_dict:
			result.append(word)
	return result

def champ_spells(champion_name):
	champ = champ_dict[champion_name]
	passive = champ.passive
	spells = champ.spells
	q = spells[0]
	w = spells[1]
	e = spells[2]
	r = spells[3]

	def stringify_list(lst):
		return [str(x) for x in lst]

	q_costs = stringify_list(q.costs) 
	w_costs = stringify_list(w.costs) 
	e_costs = stringify_list(e.costs) 
	r_costs = stringify_list(r.costs) 
	q_cd = stringify_list(q.cooldowns) 
	w_cd = stringify_list(w.cooldowns) 
	e_cd = stringify_list(e.cooldowns) 
	r_cd = stringify_list(r.cooldowns) 

	text = ''' Passive : {0} - {1}
		   Q : {2}	Cost: {3}	Cooldown: {4}
		   {5}
		   W : {6}	Cost: {7}	Cooldown: {8}
		   {9}
		   E : {10}	Cost: {11}	Cooldown: {12}
		   {13}
		   R : {14}	Cost: {15}	Cooldown: {16}
		   {17} 
	'''.format(passive.name, passive.description,
				q.name, '/'.join(q_costs), '/'.join(q_cd), q.description,
				w.name, '/'.join(w_costs), '/'.join(w_cd), w.description,
				e.name, '/'.join(e_costs), '/'.join(e_cd), e.description,
				r.name, '/'.join(r_costs), '/'.join(r_cd), r.description
		)
	return text

def test_champ_spells():
        print(champ_spells('ashe'))

if __name__ == '__main__':
        test_champ_spells()
