import random as rnd
import databases

characters = {
    '1': ['Elli', ['Elli1.jpg', 'Elli2.jpg', 'Elli3.jpg']],
    '2': ['Dina', ['Dina1.png', 'Dina2.jpg', 'Dina3.jpg']],
    '3': ['Jesse', ['Jesse1.jpg', 'Jesse2.jpg', 'Jesse3.jpg']],
    '4': ['Tommy', ['Tommy1.jpg', 'Tommy2.jpg', 'Tommy3.jpg']],
    '5': ['Joel', ['Joel1.png', 'Joel2.jpg', 'Joel3.jpg']],
    '6': ['Abby', ['Abby.jpg', 'Abby1.jpeg', 'Abby2.jpg']],
    '7': ['Lev', ['Lev1.jpg', 'Lev2.jpg', 'Lev3.jpg']],
    '8': ['Yara',['Yara1.jpg', 'Yara2.jpg', 'Yara3.jpg']],
    '9': ['Mel', ['Mel1.jpg', 'Mel2.jpg', 'Mel3.png']],
    '10': ['Manny', ['Manny1.jpg', 'Manny2.jpg', 'Manny3.jpg']],
    '11': ['Bill', ['Bill1.jpg', 'Bill2.png', 'Bill3.jpg']],
    '12': ['Marlin', ['Marlin1.jpeg', 'Marlin2.jpg', 'Marlin3.jpg']]
}


phrases = ['Oh, and this is {}, let\'s try it!',
           '{} amazing character, but what about you? Let\'s check it',
           'Wow, {}! It\' be interesting 100%!',
           '{}! We\'re looking for you! Let\'s do it!',
           'Hmmm... We have {}, can you win now?)',]


def choose_caracter(user_id):
    expt = databases.get_expt(user_id)
    while True:
        person = rnd.randint(1, 12)
        if person not in expt:
            expt.append(person)
            if len(expt) == 4:
                expt.pop(0)
            break
        else:
            continue
    databases.save_expt(user_id, expt)
    return rnd.choice(characters[str(person)][1]), rnd.choice(phrases).format(characters[str(person)][0])

def expt_transmission(expt):
    transmited = [characters[str(i)][0] for i in expt]
    return transmited