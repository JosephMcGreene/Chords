notes = ["C", "D", "E", "F", "G", "A", "B"]

def key_tonic():
	tonic = input("What key is the music in? ")
	
	if not notes.__contains__(tonic.upper()):
		tonic = input("What key is the music in (A-G please)? ")
	
	return tonic.upper()

def key_accidental():
	accidental = input("sharp (#), flat (b), or natural (nat)? ")

	if accidental != "#" and accidental != "b" and accidental != "nat":
		accidental = input('"#", "b", or "nat": ')

	return accidental


def key_quality():
	quality = input("Major or minor? ")

	if quality != "Major" and quality != "minor":
		quality = input('"Major" or "minor"? ')

	return quality

print(f"The key of the music is {key_tonic()}{key_accidental()} {key_quality()}")