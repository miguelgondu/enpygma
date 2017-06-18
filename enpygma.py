def isOnetoOne(dict1):
    list_of_values = []
    set_of_values = set([])
    for key in dict1:
        list_of_values.append(dict1[key])
        set_of_values.add(dict1[key])
    #print(list_of_values)
    if len(list_of_values) == len(set_of_values):
        return True
    else:
        return False

Rotor_1_dict = {'a': 'e', 'b': 'k', 'c': 'm', 'd': 'f',
           'e': 'l', 'f': 'g', 'g': 'd', 'h': 'q',
           'i': 'v', 'j': 'z', 'k': 'n', 'l': 't',
           'm': 'o', 'n': 'w', 'o': 'y', 'p': 'h',
           'q': 'x', 'r': 'u', 's': 's', 't': 'p',
           'u': 'a', 'v': 'i', 'w': 'b', 'x': 'r',
           'y': 'c', 'z': 'j', ' ': ' '}

Rotor_1_dict_inverse = {v: k for k, v in Rotor_1_dict.items()}

Rotor_1_knocker = 'r'

Rotor_2_dict = {'a': 'a', 'b': 'j', 'c': 'd', 'd': 'k',
           'e': 's', 'f': 'i', 'g': 'r', 'h': 'u',
           'i': 'x', 'j': 'b', 'k': 'l', 'l': 'h',
           'm': 'w', 'n': 't', 'o': 'm', 'p': 'c',
           'q': 'q', 'r': 'g', 's': 'z', 't': 'n',
           'u': 'p', 'v': 'y', 'w': 'f', 'x': 'v',
           'y': 'o', 'z': 'e', ' ': ' '}

Rotor_2_dict_inverse = {v: k for k, v in Rotor_2_dict.items()}

Rotor_2_knocker = 'f'

Rotor_3_dict = {'a': 'b', 'b': 'd', 'c': 'f', 'd': 'h',
           'e': 'j', 'f': 'l', 'g': 'c', 'h': 'p',
           'i': 'r', 'j': 't', 'k': 'x', 'l': 'v',
           'm': 'z', 'n': 'n', 'o': 'y', 'p': 'e',
           'q': 'i', 'r': 'w', 's': 'g', 't': 'a',
           'u': 'k', 'v': 'm', 'w': 'u', 'x': 's',
           'y': 'q', 'z': 'o', ' ': ' '}

Rotor_3_dict_inverse = {v: k for k, v in Rotor_3_dict.items()}

Rotor_3_knocker = 'w'

Rotor_4_dict = {'a': 'e', 'b': 's', 'c': 'o', 'd': 'v',
           'e': 'p', 'f': 'z', 'g': 'j', 'h': 'a',
           'i': 'y', 'j': 'q', 'k': 'u', 'l': 'i',
           'm': 'r', 'n': 'h', 'o': 'x', 'p': 'l',
           'q': 'n', 'r': 'f', 's': 't', 't': 'g',
           'u': 'k', 'v': 'd', 'w': 'c', 'x': 'm',
           'y': 'w', 'z': 'b', ' ': ' '}

Rotor_4_dict_inverse = {v: k for k, v in Rotor_4_dict.items()}

Rotor_4_knocker = 'k'

Rotor_5_dict = {'a': 'v', 'b': 'z', 'c': 'b', 'd': 'r',
           'e': 'g', 'f': 'i', 'g': 't', 'h': 'y',
           'i': 'u', 'j': 'p', 'k': 's', 'l': 'd',
           'm': 'n', 'n': 'h', 'o': 'l', 'p': 'x',
           'q': 'a', 'r': 'w', 's': 'm', 't': 'j',
           'u': 'q', 'v': 'o', 'w': 'f', 'x': 'e',
           'y': 'c', 'z': 'k', ' ': ' '}

Rotor_5_dict_inverse = {v: k for k, v in Rotor_5_dict.items()}

Rotor_5_knocker = 'a'

Reflector_B_dict = {'a': 'y', 'y': 'a', 'b': 'r', 'r': 'b', 'c': 'u', 'u': 'c', 'd': 'h', 'h': 'd',
                    'e': 'q', 'q': 'e', 'f': 's', 's': 'f', 'g': 'l', 'l': 'g',
                    'i': 'p', 'p': 'i', 'j': 'x', 'x': 'j', 'k': 'n', 'n': 'k',
                    'm': 'o', 'o': 'm', 't': 'z', 'z': 't', 'v': 'w', 'w': 'v', ' ': ' '}

def getInverseDict(_dict):
    return {v: k for k, v in _dict.items()}

def getComposite(dict1, dict2):
    return {k: dict2[dict1[k]] for k in dict1}
from string import ascii_lowercase as alphabet

class rotor:
    def __init__(self, _rotor_dict, _starting_position = 'a', _knocker = 'a'):
        self.rotor_dict = _rotor_dict
        self.starting_position = _starting_position
        self.knocker = _knocker
        self.current_position = _starting_position
        self.inverse_dict = getInverseDict(self.rotor_dict)
        
    def setCurrentPosition(self, letter):
        self.current_position = letter
    
    def turn(self):
        current_index = alphabet.index(self.current_position)
        self.setCurrentPosition(alphabet[(current_index + 1)%26])
        
    def mapLetter(self, letter):
        return self.rotor_dict[letter]
    
    def reverseMapLetter(self, letter):
        return self.inverse_dict[letter]

def offseter(letter):
    ind = alphabet.index(letter)
    dictionary = {alphabet[(ind - i) % 26]: _letter for (i, _letter) in enumerate(alphabet)}
    dictionary[' '] = ' '
    return dictionary

def stringcleaner(message):
    return message.replace('\r', '').replace('\n', ' ').lower()

def enigma(message, _rotors, _starting_positions, _plugboard):
    '''
    This function encrypts/decrypts a string simulating the enigma machine whose set up is given by
        -_rotors: a tuple with a reflector and three rotor objects which correspond to the left,
                  middle and right rotors respectively.
        -_starting_positions: a tuple with three letters stating the starting positions of said rotors.
        
    To-Do:
        -Implement it in such a way that all characters that are not in the dict are mapped to themselves,
         fixing the whole punctuation (and spacing) problem.
    '''
    
    # Check whether the parameters are actually usable or not
    
    
    reflector, left_rotor, middle_rotor, right_rotor = _rotors
    
    left_rotor.setCurrentPosition(_starting_positions[0])
    middle_rotor.setCurrentPosition(_starting_positions[1])
    right_rotor.setCurrentPosition(_starting_positions[2])
    #Encrypt using a for for each letter in string. Be wary of white spaces when turning rotors.
    
    #The order is: recieve a letter, rotate right-most rotor, pass it through the plugboard,
    #pass it through the rotors, bounce it, pass it throught the rotors again, pass it through the plugboard
    #and save it.
    
    encrypted_message = ''
    for letter in message:
        #Turn the rotor mechanisms.
        right_rotor.turn()
        if right_rotor.current_position == right_rotor.knocker:
            middle_rotor.turn()
            if middle_rotor.current_position == middle_rotor.knocker:
                left_rotor.turn()

        #Encrypt.
        right_rotor_offseter = offseter(right_rotor.current_position)
        middle_rotor_offseter = offseter(middle_rotor.current_position)
        left_rotor_offseter = offseter(left_rotor.current_position)
        
        composite_of_rotors = getComposite(right_rotor_offseter, right_rotor.rotor_dict)
        composite_of_rotors = getComposite(composite_of_rotors, middle_rotor_offseter)
        composite_of_rotors = getComposite(composite_of_rotors, middle_rotor.rotor_dict)
        composite_of_rotors = getComposite(composite_of_rotors, left_rotor_offseter)
        composite_of_rotors = getComposite(composite_of_rotors, left_rotor.rotor_dict)
        
        inverse_of_rotors = getInverseDict(composite_of_rotors)
        
        encrypted_letter = _plugboard[letter]
        encrypted_letter = composite_of_rotors[encrypted_letter]
        encrypted_letter = reflector[encrypted_letter]
        encrypted_letter = inverse_of_rotors[encrypted_letter]
        encrypted_letter = _plugboard[encrypted_letter]
        
        #Add it to the message.
        encrypted_message += encrypted_letter
    
    return encrypted_message

def plugboardCompleter(plugboard):
    inverse_plugboard = {v: k for k, v in plugboard.items()}
    complete_plugboard = {}
    for letter in alphabet:
        if letter in plugboard:
            complete_plugboard[letter] = plugboard[letter]
        elif letter in inverse_plugboard:
            complete_plugboard[letter] = inverse_plugboard[letter]
        else:
            complete_plugboard[letter] = letter
    complete_plugboard[' '] = ' '
    return complete_plugboard

message = 'miguel miguel miguel miguel'
message.replace('\r', '')
Rotor_1 = rotor(Rotor_1_dict, _knocker = Rotor_1_knocker)
Rotor_2 = rotor(Rotor_2_dict, _knocker = Rotor_2_knocker)
Rotor_3 = rotor(Rotor_3_dict, _knocker = Rotor_3_knocker)
Rotor_4 = rotor(Rotor_4_dict, _knocker = Rotor_4_knocker)
Rotor_5 = rotor(Rotor_5_dict, _knocker = Rotor_5_knocker)

rotors = (Reflector_B_dict, Rotor_1, Rotor_2, Rotor_3)
starting_positions = ('b','a','a')
plugboard = {'b':'t', 'c':'u', 'f':'q', 'g':'z', 'i':'a', 'j':'o', 'n':'v', 'p':'e', 's': 'l', 'y':'m'}
plugboard = plugboardCompleter(plugboard)
# print(plugboard)
encrypted_message = enigma(message, rotors, starting_positions, plugboard)
print('Message to encrypt: ' + message)
print('Encrypted message: ' + enigma(message, rotors, starting_positions, plugboard))
print('Decrypted message: ' + enigma(encrypted_message, rotors, starting_positions, plugboard))
# decripted_message = enigma(encrypted_message, rotors, starting_positions, plugboard)
# print(message == decripted_message)


