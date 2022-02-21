def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f :
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines, person1, person2):
	person1_word_count = 0
	person1_sticker_count = 0
	person1_image_count = 0
	person1_miss_count = 0
	person2_word_count = 0
	person2_sticker_count = 0
	person2_image_count = 0
	person2_miss_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		chat = s[2:]
		if name == person1:	
			for m in chat:
				if m == '貼圖':
					person1_sticker_count += 1
				elif m == '圖片':
					person1_image_count += 1
				elif m == '未接來電':
					person1_miss_count += 1
				else:
					person1_word_count += len(m)
		elif name == person2:
			for m in chat:
				if m == '貼圖':
					person2_sticker_count += 1
				elif m == '圖片':
					person2_image_count += 1
				elif m == '未接來電':
					person2_miss_count += 1
				else:
					person2_word_count += len(m)
			

	sentens1 = person1 + '共' + str(person1_word_count) + '個字，' + str(person1_sticker_count) + '個貼圖，' + str(person1_image_count) + '個圖片，有' + str(person1_miss_count) + '個未接來電。\n'
	sentens2 = person2 + '共' + str(person2_word_count) + '個字，' + str(person2_sticker_count) + '個貼圖，' + str(person2_image_count) + '個圖片，有' + str(person2_miss_count) + '個未接來電。'
	return sentens1, sentens2


def main():
	lines = read_file('對話紀錄相關檔案/對話紀錄2/[LINE]Mr.梁川.txt')
	person1_word_count, person2_word_count = convert(lines,'Mr.梁川', 'Poppy')
	print(person1_word_count, person2_word_count )

main()

