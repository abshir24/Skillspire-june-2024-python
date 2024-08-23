session = {}

if "counter" not in session:
    session['counter'] = 0
else: 
    session['counter'] += 1

print(session)