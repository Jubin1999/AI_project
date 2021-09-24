import phonenumbers
from phonenumbers import carrier, gecoder, timezone

phone_num = input("+917002380627")
phone_num = phonenumbers.parse(phone_num)

print("Time Zone-", timezone.time_zone_for_number(phone_num))

print("Carrier Name-", carrier.name_for_number(phone_num, "en"))

print("Region-", gecoder.description_for_number(phone_num, "en"))

print("Valid phone number-", phonenumbers.is_valid_number(phone_num))

