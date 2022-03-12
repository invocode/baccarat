import random as ra
import time
import matplotlib.pyplot as plt

balance = 15
start_balance = balance
bets = 0
progress = 0
player = 0
banker = 0
draws = 0

while progress < 4000 and balance > 1:
    draw = ra.randint(1, 8)
    numb = ra.randint(1, 2)

    if numb == 1 and draw != 8:
        progress += balance
        bets += 1
        player += 1
        print(progress)
        print(balance)
    
    elif numb == 2 and draw != 8:
        progress += balance
        balance -= balance*0.025
        bets +=1
        banker += 1
        print(progress)
        print(balance)

    elif draw == 8:
        progress += balance
        bets += 1
        draws += 1
        print(progress)
        print(balance)


    time.sleep(0.05)
print('-------------------------------------------------------------------------------------------------------------------------------------------')
print('Start balance: ', start_balance)
print('Number of bets: ', bets)
print('Balance: ', balance)
print('Player wins: ', player)
print('Banker wins: ', banker)
print('Draws: ', draws)
print('Progress: ', progress)
print('-------------------------------------------------------------------------------------------------------------------------------------------')

file_name = str(start_balance)+'.txt'
f = open(file_name, 'a+')  # open file in append mode
if progress >= 4000:
    f.write('4000: Yes, Progress: {}, Balance: {}\n'.format(progress, balance))
else:
    f.write('4000: No, Progress: {}, Balance: {}\n'.format(progress, balance))
f.close()

labels = 'Draw', 'Player', 'Banker'
sizes = [draws, player, banker]
explode = (0.1, 0, 0)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  
plt.legend(['Draws: {}'.format(draws), 'Player: {}'.format(player), 'Banker: {}'.format(banker)], loc = 'upper right')
plt.title('Baccarat')
plt.text(-1.82, 0.785, 'Start balance: {}\nNumber of bets: {}\nBalance: {}\nProgress: {}'.format(start_balance, bets, int(balance), int(progress)))
plt.show()