notes = ["C", "D", "E", "F", "G", "A", "B"]

def key_tonic():
	tonic = input("What Key is the music in? ")
	
	if not notes.__contains__(tonic.upper()):
		tonic = input("What Key is the music in? ")
	
	return tonic.upper()


def key_quality():
	quality = input("Major or minor? ")

	if quality != "Major" and quality != "minor":
		quality = input("Major or minor? ")

	return quality

print(f"The key of the music is {key_tonic()} {key_quality()}")