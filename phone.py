import phonenumbers
from phonenumbers import carrier, geocoder, timezone

def get_phone_number_info():
    mobileNo = input("Enter Phone number with country code (+xx xxxxxxxxx): ")
    mobileNo = phonenumbers.parse(mobileNo)
    
    if phonenumbers.is_valid_number(mobileNo):
        region = timezone.time_zones_for_number(mobileNo)
        service_provider = carrier.name_for_number(mobileNo, "en")
        country = geocoder.description_for_number(mobileNo, "en")
        
        print("Phone Number belongs to region:", region)
        print("Service Provider:", service_provider)
        print("Phone number belongs to country:", country)
    else:
        print("Please enter a valid mobile number")

get_phone_number_info()
