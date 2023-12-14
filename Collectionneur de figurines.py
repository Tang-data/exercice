# NE PAS TOUCHER
exemplaires = [50000,50000,500,50000,2000,100,2000,2000,2000,2000,50000,50,2000,2000,50000,2000,2000,2000,50000,2000,500,2000,2000,50000,50000,50000,2000,2000,50000,2000,2000,50000,2000,50000,2000,2000,50000,2000,50000,50000,2000]
cotes = [0.8,0.8,2,0.8,0.8,8,1,1,0.8,0.6,0.6,15,1,0.6,0.6,0.8,0.6,1.2,1,0.8,1.2,0.6,1.2,1.2,0.6,0.8,1,0.6,0.8,0.8,0.8,1.2,0.8,0.8,0.8,0.6,0.8,0.6,1.2,0.6,0.6]
# NE PAS TOUCHER


valeur_achat = []

for i in exemplaires :
    if i < 2000 :
        valeur_achat.append(30)
    else :
        valeur_achat.append(15)

valeur_revente = [a * b for a, b in zip(valeur_achat, cotes)]

bonus_malus = [a-b for a, b in zip(valeur_revente, valeur_achat)]
print(bonus_malus)
print(valeur_achat)
print(valeur_revente)
reponse = sum(bonus_malus)
print(reponse)
