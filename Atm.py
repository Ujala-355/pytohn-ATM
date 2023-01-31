print('welcome to bankworld')
print('swip ur card here')
language=input('choose your language')
total_balance=5000
if language=='english' and 'hindi':
	account=input('choose your account')
	if account=='saving' and 'FRCM':
		pin=int(input('enter a pin'))
		if pin==1999:
			print('choose youre trasection','1.balance_enquary','2.withdraw_money','3.deposit_money')
			transection=input('transection')
			if transection=='1':
				print('balance:',total_balance)
			elif transection=='2':
				withdraw_money=int(input('enter a withdraw_money'))
				if withdraw_money<total_balance:
				# total_balance==5000
					balance=total_balance-withdraw_money
					print(balance)
				else:
					print("ypu have not enough money")
			elif transection=='3':
				deposit_money=int(input('enter a deposit_money'))	
				print('deposit_money',deposit_money+total_balance)
			else:
				print("quit")
		else:
			print("incorrect pin")
	else:
			print('choose correct account')
else:
	print('choose corrct lang')
 