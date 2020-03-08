def read_file(filename):
	lines=[]
	with open(filename, 'r', encoding= 'utf-8') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	newlines = []
	person = None
	for line in lines:
		if line == 'Joyce':
			person = 'Joyce'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			newlines.append(person + ': ' + line)
	return newlines

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()