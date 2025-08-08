def get_count_characters(text):
	char_dict={}
	for char in text:
		lower_char=char.lower()
		if lower_char in char_dict:
			char_dict[lower_char]+=1
		else:
			char_dict[lower_char]=1
	return char_dict
def sort_on(item):
	return item["num"]

def convert_dict_to_list(count_characers):
	sort_list=[]
	for char , count in count_characers.items():
		new_dict={"char":char,"num":count }
		sort_list.append(new_dict)
	return sort_list

def get_num_words(text):
	words=text.split()
	return len(words)

