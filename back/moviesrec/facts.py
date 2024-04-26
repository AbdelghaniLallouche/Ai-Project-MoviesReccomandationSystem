from aima3.logic import *

movie_kb = FolKB()

#  Time : select option from [2010-2020] ==> Old , [2020-2024] ==> New , <2010 ==> Veryold
# Language English , Spanish, French, Korean, Chinese, German, Russian
# Genre: Drama, Action, Comedy, Horror,ScienceFiction,Fantasy
movie_kb.tell(expr('Language(English)'))
movie_kb.tell(expr('Type(Movie)'))
movie_kb.tell(expr('Time(Veryold)'))
movie_kb.tell(expr('Genre(Action)'))
movie_kb.tell(expr('Principalactor(CharlesBronson)'))

#rule for getting the type
movie_kb.tell(expr('Language(English)&Type(Movie)&Time(Veryold)&Genre(Action) ==>Concept(Western)'))
movie_kb.tell(expr('Language(English)&Type(Movie)&Time(Old)&Genre(Action) ==>Concept(Mafia)'))
movie_kb.tell(expr('Language(English)&Type(Movie)&Time(Veryold)&Genre(Action) ==>Concept(Mafia)'))
movie_kb.tell(expr('Language(English)&Type(Movie)&Time(Veryold)&Genre(Action) ==>Concept(Mafia)'))
movie_kb.tell(expr('Language(English)&Type(Movie)&Time(Old)&Genre(Action) ==>Concept(War)'))
movie_kb.tell(expr('Language(English)&Type(Movie)&Time(Old)&Genre(Action) ==>Concept(War)'))
movie_kb.tell(expr('Language(English)&Type(Movie)&Time(Old)&Genre(Action) ==>Concept(War)'))
movie_kb.tell(expr('Language(English)&Type(Movie)&Time(Veryold)&Genre(Action) ==>Concept(War)'))

movie_kb.tell(expr('Language(English)&Type(Movie)&Time(Veryold)&Genre(Fantasy) ==>Concept(War)'))
movie_kb.tell(expr('Language(English)&Type(Movie)&Time(Old)&Genre(Fantasy) ==>Concept(War)'))
movie_kb.tell(expr('Language(English)&Type(Movie)&Time(Old)&Genre(Fantasy) ==>Concept(Pirates)'))
movie_kb.tell(expr('Language(English)&Type(Movie)&Time(Veryold)&Genre(Fantasy) ==>Concept(Pirates)'))
movie_kb.tell(expr('Language(English)&Type(Movie)&Time(New)&Genre(Fantasy) ==>Concept(Adventure)'))


movie_kb.tell(expr('Language(Spanish)&Type(Movie)&Time(New)&Genre(Horror) ==>Concept(Enigme)'))


# get the movies
#action movies
movie_kb.tell(expr('Principalactor(CharlesBronson)&Concept(Western) ==>Movie(OnceUponaTimeintheWest)'))
movie_kb.tell(expr('Principalactor(KeanuReeves)&Concept(Mafia) ==>Movie(JohnWick)'))
movie_kb.tell(expr('Principalactor(AlPAcino)&Concept(Mafia) ==>Movie(GodFather)'))
movie_kb.tell(expr('Principalactor(MarlonBrando)&Concept(Mafia) ==>Movie(GodFather)'))
movie_kb.tell(expr('Principalactor(BradPitt)&Concept(War) ==>Movie(fury)'))
movie_kb.tell(expr('Principalactor(LoganLerman)&Concept(War) ==>Movie(fury)'))
movie_kb.tell(expr('Principalactor(BradPitt)&Concept(War) ==>Movie(IngloriousBasterds)'))
movie_kb.tell(expr('Principalactor(ChristophWaltz)&Concept(War) ==>Movie(IngloriousBasterds)'))
movie_kb.tell(expr('Principalactor(BradPitt)&Concept(War) ==>Movie(Troy)'))
#Fantasy movies
movie_kb.tell(expr('Principalactor(ElijahWood)&Concept(War) ==>Movie(LordOfTheRings)'))
movie_kb.tell(expr('Principalactor(IanMcKellen)&Concept(War) ==>Movie(LordOfTheRings)'))
movie_kb.tell(expr('Principalactor(ViggoMortensen)&Concept(War) ==>Movie(LordOfTheRings)'))
movie_kb.tell(expr('Principalactor(OrlandoBloom)&Concept(War) ==>Movie(LordOfTheRings)'))
movie_kb.tell(expr('Principalactor(OrlandoBloom)&Concept(War) ==>Movie(LordOfTheRings)'))
movie_kb.tell(expr('Principalactor(MartinFreeman)&Concept(War) ==>Movie(TheHobbit)'))
movie_kb.tell(expr('Principalactor(AndySerkis)&Concept(War) ==>Movie(TheHobbit)'))
movie_kb.tell(expr('Principalactor(JohnnyDepp)&Concept(Pirates) ==>Movie(PiratesOfTheCaribbean)'))
movie_kb.tell(expr('Principalactor(OrlandoBloom)&Concept(Pirates) ==>Movie(PiratesOfTheCaribbean)'))
movie_kb.tell(expr('Principalactor(MillieBobbyBrown)&Concept(Adventure) ==>Movie(Damsel)'))
#Horror movies
movie_kb.tell(expr('Principalactor(AriaBedmar)&Concept(Enigme) ==>Movie(HermanaMuerte)'))