import sys
import random

def main():
	if len(sys.argv) < 3:
		print "Use: <.py file> <input file> <output file>"
		sys.exit(0)

	# input file
	filein = open(sys.argv[1], 'r')
	fin = filein.read()

	# output file
	fout = open(sys.argv[2], 'w')

	# define codons
	codons = [["ATG","TTT","TTC","TTA","TTG","CTT","CTC","CTA","CTG","ATT","ATC","ATA","GTT","GTC","GTA","GTG","TCT","TCC","TCA","TCG","AGT","AGC","CCT","CCC","CCA","CCG","ACT","ACC","ACA","ACG","GCT","GCC","GCA","GCG","TAT","TAC","CAT","CAC","CAA","CAG","AAT","AAC","AAA","AAG","GAT","GAC","GAA","GAG","TGT","TGC","TGG","CGT","CGC","CGA","CGG","AGA","AGG","GGT","GGC","GGA","GGG"],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]



	# split genes by '>'
	lista1 = str.split(fin, '>')
	percentage = 0
	interface = 0
	for i in range(len(lista1)-1):
		nonsense = "false"
		percentage = 50*i/len(lista1)
		while interface < percentage:
			interface += 1
			print str(interface)+"% complete"
		newvalue = str.split(lista1[i+1], ']')


	names = []	
		#split the file's contents by '>'
	proteins = str.split(fin, '>')[1:] #the file header is discarded
	for prot in proteins:
		seq = []
		lista = str.split(prot, '\n') #split each protein 
		names.append(lista[0]) #salve the names
		#concatenate the sequences of amino acids of the protein
		for temp in lista[1:]:
			seq.append(temp[:])	
		seqfinal = ''.join(seq) 
		protName = str.split(lista[0]) #take the first name

		lista2 = list(seqfinal)
		
		

		j = 1
		while j < len(lista2)/3:
			matched = "false"
			try:
				codon = lista2[j*3] + lista2[j*3+1] + lista2[j*3+2]
			except Exception:
				print str.split(name, ' ')[0]+": fragmented codon"
				break
			for w in range(len(codons[0])):
				if matched == "false":
					if codon == codons[0][w]:
						matched = "true"
				if matched == "true":
					codons[1][w] += 1
			j+=1


	for i in range(len(lista1)-1):
		nonsense = "false"
		percentage = 50+50*i/len(lista1)
		while interface < percentage:
			interface += 1
			print str(interface)+"% complete"
		newvalue = str.split(lista1[i+1], ']')

		names = []
		sequences = []
		try:
			for element in newvalue:
				e = element.split('\n',1)
				names.append(e[0]) # genes list
				sequences.append(e[1]) #nucleotides list

				for gene_name in names:
					fout.write('>'+str(gene_name)+'ATG')

				# lista2 = list of each base in a gene
				lista2 = sequences[len(sequences)-1]
				lista2 = lista2.replace("\n", "")
				lista2 = lista2.replace("\r", "")
				lista2 = list(lista2)
		except IndexError:
			pass
		

		j = 0
		while j < len(lista2)/3:
			try:
				codon = lista2[j*3] + lista2[j*3+1] + lista2[j*3+2]
			except Exception:
				print str.split(name, ' ')[0]+": fragmented codon"
				break
			if codon != "UAA" or "UAG" or "UGA":
				itsamatch = "false"
				for w in range(len(codons[0])):
					if codon == codons[0][w]:
						teste = random.random()*codons[1][len(codons[1])-1]
						for z in range(len(codons[0])):
							if  itsamatch == "false":
								if teste <= codons[1][z]:
									fout.write(codons[0][z])
									itsamatch = "true"
							if itsamatch == "true":
								codons[1][z] -= 1
						break
			j+=1

		
main()
print "100% complete!\n"