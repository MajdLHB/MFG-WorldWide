import random


class var():
    NS = 0
    T = 0

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
    "Virgil van-Dijk - Netherlands",
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
    "Yann Karamoh - Ivory-Coast",
    "Leandro Paredes - Argentina",
    "Mohammed Kudus - Ghana",
    "Andreas Pereira - Brazil",
    "Boubakary Soumare - France",
    "James Tarkowski - England",
    "Sergi Roberto - Spain",
    "Ousmane Dembele - France",
    "Serge Aurier - Ivory-Coast",
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
    "Gareth Bale - Wales",
    "Luis Suarez - Uruguay",
    "Eden Hazard - Belgium",
    "Luka Modric - Croatia",
    "Toni Kroos - Germany",
    "Sergio Ramos - Spain",
    "David Silva - Spain",
    "Thiago Silva - Brazil",
    "Javier Hernandez - Mexico",
    "Luis Figo - Portugal",
    "Andrea Pirlo - Italy",
    "Alessandro Del Piero - Italy",
    "Samuel Eto'o - Cameroon",
    "Didier Drogba - Ivory-Coast",
    "Zlatan Ibrahimovic - Sweden",
    "Arjen Robben - Netherlands",
    "Robin van Persie - Netherlands",
    "Fernando Torres - Spain",
    "Andriy Shevchenko - Ukraine",
    "Sergio Aguero - Argentina",
    "Paul Scholes - England",
    "Xavi Hernandez - Spain",
    "Iker Casillas - Spain",
    "Petr Cech - Czech Republic",
    "Francesco Totti - Italy",
    "Gianluigi Buffon - Italy",
    "Andres Iniesta - Spain",
    "Xabi Alonso - Spain",
    "Carles Puyol - Spain",
    "Fernando Torres - Spain",
    "Steven Gerrard - England",
    "Frank Lampard - England",
    "Didier Drogba - Ivory-Coast",
    "Ashley Cole - England",
    "Raul Gonzalez - Spain",
    "Thierry Henry - France",
    "Ryan Giggs - Wales",
    "Ruud van Nistelrooy - Netherlands",
    "Michael Owen - England",
    "Alessandro Nesta - Italy",
    "Paolo Maldini - Italy",
    "Alessandro Del Piero - Italy",
    "Roberto Carlos - Brazil",
    "Zinedine Zidane - France",
    "Patrick Vieira - France",
    "Thierry Henry - France",
    "Fabien Barthez - France",
    "Robert Pirès - France",
    "Dennis Bergkamp - Netherlands",
    "Edgar Davids - Netherlands",
    "Clarence Seedorf - Netherlands",
    "Jaap Stam - Netherlands",
    "Davor Suker - Croatia",
    "Robert Prosinecki - Croatia",
    "Ali Daei - Iran",
    "Hidetoshi Nakata - Japan",
    "Park Ji-sung - South Korea",
    "Hong Myung-bo - South Korea",
    "Jay-Jay Okocha - Nigeria",
    "George Weah - Liberia",
    "Hakan Şükür - Turkey",
    "Emre Belözoğlu - Turkey",
    "Raul - Spain",
    "Roberto Baggio - Italy",
    "Marco van Basten - Netherlands",
    "Karl-Heinz Rummenigge - Germany",
    "Gerd Muller - Germany",
    "Franz Beckenbauer - Germany",
    "George Best - Northern Ireland",
    "Alfredo Di Stéfano - Argentina/Spain",
    "Ferenc Puskás - Hungary/Spain",
    "Lev Yashin - Soviet Union/Russia",
    "Eusebio - Portugal",
    "George Best - Northern Ireland",
    "Michel Platini - France",
    "Johan Cruyff - Netherlands",
    "Franz Beckenbauer - Germany",
    "Diego Maradona - Argentina",
    "Pelé - Brazil",
    "Alfredo Di Stéfano - Argentina/Spain",
    "Stanley Matthews - England",
    "Ferenc Puskás - Hungary/Spain",
    "Lev Yashin - Soviet Union/Russia",
    "Eusebio - Portugal",
    "George Best - Northern Ireland",
    "Luis Suárez - Uruguay",
    "Edinson Cavani - Uruguay",
    "David de Gea - Spain",
    "Cesar Azpilicueta - Spain",
    "Marcos Alonso - Spain",
    "Iñigo Martinez - Spain",
    "Federico Bernardeschi - Italy",
    "Ciro Immobile - Italy",
    "Alessandro Florenzi - Italy",
    "Leonardo Spinazzola - Italy",
    "Manuel Locatelli - Italy",
    "Gianluigi Buffon - Italy",
    "Lorenzo Pellegrini - Italy",
    "Thiago Alcántara - Spain",
    "Marco Asensio - Spain",
    "Álvaro Morata - Spain",
    "Ferran Torres - Spain",
    "Rodri - Spain",
    "Eric García - Spain",
    "Pau Torres - Spain",
    "Ibrahim Afellay - Netherlands",
    "Ryan Babel - Netherlands",
    "Luuk de-Jong - Netherlands",
    "Georginio Wijnaldum - Netherlands",
    "Nathan Aké - Netherlands",
    "Donny van-de-Beek - Netherlands",
    "Cristian Pavón - Argentina",
    "Paulo Dybala - Argentina",
    "Giovani Lo Celso - Argentina",
    "Lucas Ocampos - Argentina",
    "Lucas Alario - Argentina",
    "Ángel Correa - Argentina",
    "Renan Lodi - Brazil",
    "Éder Militão - Brazil",
    "Lucas Paquetá - Brazil",
    "Everton - Brazil",
    "Richarlison - Brazil",
    "Gabriel Jesus - Brazil",
    "Douglas Costa - Brazil",
    "Fabinho - Brazil",
    "Felipe - Brazil",
    "Alex Telles - Brazil",
    "Allan - Brazil",
    "Trent Alexander-Arnold - England",
    "Ben Chilwell - England",
    "Phil Foden - England",
    "Jack Grealish - England",
    "Jadon Sancho - England",
    "Mason Mount - England",
    "Jordan Henderson - England",
    "Kyle Walker - England",
    "John Stones - England",
    "James Maddison - England",
    "Wilfred Ndidi - Nigeria",
    "Kelechi Iheanacho - Nigeria",
    "Ahmed Musa - Nigeria",
    "Samuel Kalu - Nigeria",
    "Moses Simon - Nigeria",
    "William Troost-Ekong - Nigeria",
    "André-Pierre Gignac - France",
    "Wissam Ben-Yedder - France",
    "Kingsley Coman - France",
    "Lucas Hernandez - France",
    "Benjamin Pavard - France",
    "Lucas Digne - France",
    "Kurt Zouma - France",
    "Corentin Tolisso - France",
    "Tanguy Ndombele - France",
    "Presnel Kimpembe - France",
    "Steven Nzonzi - France",
    "Moussa Sissoko - France",
    "Jules Koundé - France",
    "Lucas Tousart - France",
    "Stefan Savic - Montenegro",
    "Stevan Jovetic - Montenegro",
    "Fedor Smolov - Russia",
    "Aleksandr Golovin - Russia",
    "Daler Kuzyaev - Russia",
    "Aleksandr Sobolev - Russia",
    "Nicolae Stanciu - Romania",
    "Denis Alibec - Romania",
    "Ciprian Deac - Romania",
    "Valentin Costache - Romania",
    "Ianis Hagi - Romania",
    "Taulant Xhaka - Albania",
    "Rey Manaj - Albania",
    "Sokol Cikalleshi - Albania",
    "Ledian Memushaj - Albania",
    "Jens Stryger Larsen - Denmark",
    "Yussuf Poulsen - Denmark",
    "Martin Braithwaite - Denmark",
    "Kasper Dolberg - Denmark",
    "Yusuf Yazici - Turkey",
    "Zeki Celik - Turkey",
    "Mert Muldur - Turkey",
    "Orkun Kökçü - Turkey",
    "Dorukhan Toköz - Turkey",
    "Ali Yavuz Kol - Turkey",
    "Merih Demiral - Turkey",
    "Necip Uysal - Turkey",
    "Okay Yokuslu - Turkey",
    "Çaglar Söyüncü - Turkey",
    "Kenan Karaman - Turkey",
    "Hakan Çalhanoglu - Turkey",
    "Cengiz Ünder - Turkey",
    "Ozan Tufan - Turkey",
    "Yusuf Yazıcı - Turkey",
    "Niklas Süle - Germany",
    "Lukas Klostermann - Germany",
    "Leroy Sané - Germany",
    "Kai Havertz - Germany",
    "Julian Brandt - Germany",
    "Leon Goretzka - Germany",
    "Toni Kroos - Germany",
    "İlkay Gündoğan - Germany",
    "Serge Gnabry - Germany",
    "Nico Schulz - Germany",
    "Ridle Baku - Germany",
    "Niklas Stark - Germany",
    "Wahbi Khazri - Tunisia",
    "Youssef Msakni - Tunisia",
    "Aymen Abdennour - Tunisia",
    "Ferjani Sassi - Tunisia",
    "Ali Maaloul - Tunisia",
    "Saber Khalifa - Tunisia",
    "Yassine Chikhaoui - Tunisia",
    "Hamdi Harbaoui - Tunisia",
    "Hannibal Mejbri - Tunisia",
    "Mouez Hassen - Tunisia",
    "Dylan Bronn - Tunisia",
    "Ellyes Skhiri - Tunisia",
    "Naïm Sliti - Tunisia",
    "Recardo Kaka - Brazil",
    "Diego Costa - Spain",
    "Mario Gotze - Germany",
    "Javier Pastore - Argentina",
    "Andy Delort - France",
    "Sofiane Boufal - Morocco",
    "Ahmed Hegazi - Egypt",
    "Yann Karamoh - Ivory-Coast",
    "Leandro Paredes - Argentina",
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
            print(f'Your score is: {var.NS} in {var.T} tries')
            print(f'---------------------')
            Game()
        else:
            print ("incorrect Answer")
            print(f'Your score is: {var.NS} in {var.T} tries')
            print(F'correct Answer is: {Name} {name1}!')
            print(f'---------------------')
            Game()
    else:
        print("Incorrect Input")
        print(f'---------------------')
        Game()


Game()

