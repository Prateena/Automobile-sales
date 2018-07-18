import csv,sys,os

sys.path.append("/home/daenerys/Desktop/Automobile/Automobile_sales")

os.environ['DJANGO_SETTINGS_MODULE'] = 'Automobile_sales.settings'

import django

django.setup()

from myapp.models import post_save

finaldata = csv.reader(open('/home/daenerys/Desktop/Automobile/finaldata.csv'), delimiter = ",")

for row in finaldata:
	if row[0] != 'vehicle_type':
		post = post_save()
		post.vehicle_type = row[0]
		post.brand = row[1]
		post.model_no = row[2]
		post.engine_power = row[3]
		post.price = row[4]
		post.description = row[5]
		post.image = row[6]
		post.user_id = row[7]
		post.save()
