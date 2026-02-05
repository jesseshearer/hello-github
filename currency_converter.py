pesos = int(input(' How many pesos do you have? '))
soles = int(input(' How many soles do you have? '))
reais = int(input(' How many reais do you have? '))

# Convert to USD 
pesosAmerican = pesos * 0.00027
solesAmerican = soles * 0.3
reaisAmerican = reais * 0.19
totalAmerican = round(pesosAmerican + solesAmerican + reaisAmerican, 2)

# Print results

print(pesos,'Columbian pesos converts to', round(pesosAmerican, 2),'USD')
print(soles,'Peruvian soles converts to', round(solesAmerican, 2), 'USD')
print(reais,'Brazilian reais converts to', round(reaisAmerican, 2), 'USD')
print ('You have ', totalAmerican,)
