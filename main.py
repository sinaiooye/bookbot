import sys
from stats import get_count_characters,sort_on,convert_dict_to_list,get_num_words

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents=f.read()
	return file_contents

def main():
	if len(sys.argv)!=2:
		print ("Usage: python3 main.py <path_to_book>")
		sys.exit (1)
	filepath=sys.argv[1]

	print ("============ BOOKBOT ============")
	print (f"Analyzing book found at books/{filepath}.txt...")
	book_text = get_book_text(filepath)
	char_counts=get_count_characters(book_text)
	num_words=get_num_words(book_text)
	print ('----------- Word Count ----------')
	print (f"Found {num_words} total words")

	unsort_list=convert_dict_to_list(char_counts)
	unsort_list.sort(reverse=True,key=sort_on)
	print ('--------- Character Count -------')
	for item in unsort_list:
		if item["char"].isalpha():
			print (f"{item["char"]}: {item["num"]}")

	print ('============= END ===============')

if __name__ == "__main__":
	main()
