from enpygma_body import enigma, all_rotors, reflector_B

Rotor_1, Rotor_2, Rotor_3, Rotor_4, Rotor_5 = all_rotors 

def test_simple_cyphering():
	message = 'miguel'
	rotors = (reflector_B, Rotor_1, Rotor_2, Rotor_3)
	plugboard = {'b':'t', 'c':'u', 'f':'q', 'g':'z',
				 'i':'a', 'j':'o', 'n':'v', 'p':'e',
				 's': 'l', 'y':'m'}
	encrypted_message = enigma(message, rotors, ('a', 'a', 'a'),
					plugboard)
	decrypted_message = enigma(encrypted_message, rotors,
					('a', 'a', 'a'), plugboard)
	assert message == decrypted_message
