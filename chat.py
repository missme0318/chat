def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f :
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines, person1, person2):
	chat = []
	for line in lines:
		if person1 == line:
			person = line
			continue
		elif person2 == line:
			person = line
			continue
		chat.append(str(person + ': ' + line))
	return chat

def output_file(filename,convertor):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in convertor:
			f.write(line + '\n')




lines = read_file('對話紀錄相關檔案/對話紀錄1/input.txt')
convertor = convert(lines, 'Allen', 'Tom')
output_file('對話紀錄1/output1.txt', convertor)
