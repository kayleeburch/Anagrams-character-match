# Don't forget to run your tests!

def is_character_match(string1, string2):
	lower_string_1 = list(string1.lower())
	lower_string_2 = list(string2.lower())
	lower_string_1.sort()
	lower_string_2.sort()
	remove_white_space_1 = [i for i in lower_string_1 if i != " "]
	remove_white_space_2 = [i for i in lower_string_2 if i != " "]
	if remove_white_space_1 == remove_white_space_2:
		return True
	else:
		return False
	
	
	# Your code here
print(is_character_match('hello', '   lle  ho') == True)
print(is_character_match('charm', 'march') == True)
print(is_character_match('zach', 'attack') == False)
print(is_character_match('CharM', 'mARcH') == True)
print(is_character_match('abcde2', 'c2abed') == True)

