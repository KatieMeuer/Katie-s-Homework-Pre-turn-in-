#Katie Meuer, Stock Transaction Program, 1/19/2023
#Display money he spent for stock
#Display 1st commision
#Display sell price
#Display 2nd commission
#Display amount of money left over

#Amount Jow paid for stock
Amount1 = 2000 * 40.00

#Commission1
Commission1 = Amount1 * 0.03

Joe_Paid = Amount1 + Commission1

#Amount Sold
Amount_Sold = 42.75 * 2000

#Commission2
Commission2 = 0.03 * Amount_Sold

#Joe Received
Joe_Received = Amount_Sold - Commission2

#Amound Joe had left 
Amount_Left = Joe_Received - Joe_Paid

print(f'Joe paid {Amount1} for his stock.')
print(f'Joe paid his broker {Commission1:,.2f} for his help in buying the stock.')
print(f'Joe sold his stock for {Amount_Sold}.')
print(f'Joe paid his broker {Commission2:,.2f} for his help in selling the stock.')
print(f'Joe had {Amount_Left} when all of his transactions were complete')