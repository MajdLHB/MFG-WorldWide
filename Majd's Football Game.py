import random


class var():
    NS = 0

var()
def Game():
    list1 = football_players = [
    "Lionel Messi - Argentina",
    "Cristiano Ronaldo - Portugal",
    "Kylian Mbappe - France",
    "Neymar Jr - Brazil",
    "Erling Haaland - Norway",
    "Robert Lewandowski - Poland",
    "Karim Benzema - France",
    "Mohamed Salah - Egypt",
    "Kevin De-Bruyne - Belgium",
    "Luka Modric - Croatia",
    "Sergio Ramos - Spain",
    "Virgil van Dijk - Netherlands",
    "Jan Oblak - Slovenia",
    "Joshua Kimmich - Germany",
    "Harry Kane - England",
    "Sadio Mane - Senegal",
    "Bruno Fernandes - Portugal",
    "Carlos Casemiro - Brazil",
    "N'Golo Kante - France",
    "Thomas Muller - Germany",
    "Son Heung-min - South Korea",
    "Frenkie de-Jong - Netherlands",
    "Antoine Griezmann - France",
    "Joao Cancelo - Portugal",
    "Trent Alexander-Arnold - England",
    "Gianluigi Donnarumma - Italy",
    "Romelu Lukaku - Belgium",
    "Marquinhos Correa - Brazil",
    "Jadon Sancho - England",
    "Riyad Mahrez - Algeria",
    "Lautaro Martinez - Argentina",
    "Kai Havertz - Germany",
    "Thiago Alcantara - Spain",
    "Joaquin Correa - Argentina",
    "Nicolas Tagliafico - Argentina",
    "Youssef En-Nesyri - Morocco",
    "Lorenzo Insigne - Italy",
    "Edin Dzeko - Bosnia and Herzegovina",
    "Sergej Milinkovic-Savic - Serbia",
    "Andre Onana - Cameroon",
    "Kalidou Koulibaly - Senegal",
    "Pedri Lopez - Spain",
    "Eduardo Camavinga - France",
    "Hakim Ziyech - Morocco",
    "Federico Chiesa - Italy",
    "Dani Olmo - Spain",
    "Houssem Aouar - France",
    "Declan Rice - England",
    "Memphis Depay - Netherlands",
    "Thibaut Courtois - Belgium",
    "Jude Bellingham - England",
    "Federico Valverde - Uruguay",
    "Angel Di-Maria - Argentina",
    "Wojciech Szczesny - Poland",
    "Gerard Pique - Spain",
    "Raheem Sterling - England",
    "Dries Mertens - Belgium",
    "Ivan Rakitic - Croatia",
    "Matthijs De-Ligt - Netherlands",
    "Luis Alberto - Spain",
    "Wilfred Ndidi - Nigeria",
    "Raphael Varane - France",
    "Timo Werner - Germany",
    "Federico Bernardeschi - Italy",
    "Leonardo Bonucci - Italy",
    "Hakan Calhanoglu - Turkey",
    "Gareth Bale - Wales",
    "David Alaba - Austria",
    "Dani Ceballos - Spain",
    "Jules Kounde - France",
    "Achraf Hakimi - Morocco",
    "Alessio Romagnoli - Italy",
    "Domenico Berardi - Italy",
    "Nicolo Barella - Italy",
    "Andreas Christensen - Denmark",
    "Declan Rice - England",
    "Serge Gnabry - Germany",
    "Eduardo Vargas - Chile",
    "Diego Costa - Spain",
    "Mario Gotze - Germany",
    "Javier Pastore - Argentina",
    "Andy Delort - France",
    "Sofiane Boufal - Morocco",
    "Ahmed Hegazi - Egypt",
    "Yann Karamoh - Ivory Coast",
    "Leandro Paredes - Argentina",
    "Mohammed Kudus - Ghana",
    "Andreas Pereira - Brazil",
    "Boubakary Soumare - France",
    "James Tarkowski - England",
    "Sergi Roberto - Spain",
    "Ousmane Dembele - France",
    "Serge Aurier - Ivory Coast",
    "Kurt Zouma - France",
    "Yves Bissouma - Mali",
    "Odsonne Edouard - France",
    "Bukayo Saka - England",
    "Mason Mount - England",
    "Nikola Milenkovic - Serbia",
    "Joaquin Correa - Argentina",
    "Andrea Belotti - Italy",
    "Andre Carrillo - Peru",
    "Martin Odegaard - Norway",
    "Daniel James - Wales",
    "Emil Forsberg - Sweden",
    "Josip Brekalo - Croatia",
    "Mikel Oyarzabal - Spain",
    "Giovanni Di-Lorenzo - Italy",
    "Matteo Pessina - Italy",
    "Ricardo Rodriguez - Switzerland",
    "Ramy Bensebaini - Algeria",
    "Dimitri Payet - France",
    "Ciro Immobile - Italy",
    "Granit Xhaka - Switzerland",
    "Tomas Soucek - Czech Republic",
    "Kasper Schmeichel - Denmark",
    "Milan Skriniar - Slovakia",
    "Lukas Hradecky - Finland",
    "Gylfi Sigurdsson - Iceland",
    "Vladimir Coufal - Czech Republic",
    "Wout Weghorst - Netherlands",
    "Yann Sommer - Switzerland",
    "Jose Gimenez - Uruguay",
    "Denis Zakaria - Switzerland",
    "Christian Pulisic - USA",
    "Eden Hazard - Belgium",
    "Nicolas Tagliafico - Argentina",
    "Manuel Akanji - Switzerland",
    "Corentin Tolisso - France",
    "Nicolo Zaniolo - Italy",
    "Alvaro Morata - Spain",
    "Ferran Torres - Spain",
    "Diago Aspas - Spain",
    "Mason Mount - England",
    "Joaquin Correa - Argentina",
    ]

    P1 = random.choice(list1)
    PN = P1.split()
    Name = PN[0]
    name1= PN[1]
    CN = PN[3]
    print(f'from {CN}')
    print(f'Player Name: {Name}')
    Answer = input("Enter Player Family Name: ")
    

    if (type(Answer == str)):
        if ((Answer) == name1):
            print("Correct")
            var.NS = var.NS + 1
            print(f'Your score is: {var.NS}')
            print(f'---------------------')
            Game()
        else:
            print ("incorrect Answer")
            print(f'Your score is: {var.NS}')
            print(F'correct Answer is: {Name} {name1}!')
            print(f'---------------------')
            Game()
    else:
        print("Incorrect Input")
        print(f'---------------------')
        Game()


Game()

