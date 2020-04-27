'''
Протарифицировать абонента с номером 915783624 с коэффициентом k: 2руб/минута исходящие звонки, 
0руб/минута входящие, 
смс - первые 10шт бесплатно, далее 1руб/шт
'''
import csv

def payment(out_call_cost, in_call_cost, sms_cost, 
			out_call_duration, in_call_duration, sms_number):
	if sms_number > 10:
		sms_number -= 10
	bill = in_call_duration * in_call_cost + out_call_duration * out_call_cost + sms_number*sms_cost
	return bill
 
in_call_duration = 0
out_call_duration = 0
sms_number = 0
number = "915783624"

data_file = open('data.csv', 'r')
reader = csv.DictReader(data_file, delimiter=',')
for line in reader:
	if line.get('msisdn_origin') == number:
		out_call_duration += float(line.get('call_duration'))
		sms_number += int(line.get('sms_number'))

	if line.get('msisdn_dest') == number:
		in_call_duration += float(line.get('call_duration'))

print(payment(2, 0, 1, out_call_duration, in_call_duration, sms_number))

	
