"""import phonenumbers
from test import number

from phonenumbers import geocoder

##below code for find country
##test.py number is used

ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

##below code for find service provider

from phonenumbers import carrier

s_num= phonenumbers.parse(number, "RO")
print(carrier.name_for_number(s_num, "en")) """

