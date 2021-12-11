import phonenumbers
import opencage
from number import num
from phonenumbers import geocoder

key = '3448543785744288bdb3e956b6e7a18e'

sannumber = phonenumbers.parse(num)
yourlocation = geocoder.description_for_number(sannumber, "en")
print(yourlocation)

