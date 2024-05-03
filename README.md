if the system doesn't generate any movies it means that no combination found you have to add some extra combinations to facts.py 
for example 
kb_movie.tell(expr('Movie(x) & Comedy(x) & Old(x) & Spanis(x) => Funny(x)'))
kb_movie.tell(expr('Funny(x) & Favactor('Ghani') => "Moviename"'))
