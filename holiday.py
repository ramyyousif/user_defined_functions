# Task
# Defining functions.
def plane_cost(city_flight): 
    paris_flight_cost = 547
    if city_flight == 'paris':
        city_flight = paris_flight_cost       
        return city_flight
    if city_flight == 'madrid':
        madrid_flight_cost = 418
        city_flight = madrid_flight_cost       
        return city_flight
    if city_flight == 'berlin':
        berlin_flight_cost = 475
        city_flight = berlin_flight_cost        
        return city_flight


def hotel_cost(num_nights):
    hotel_cost_per_night = 120
    return num_nights * hotel_cost_per_night


def car_rental(rental_days):
    car_daily_cost = 70
    return rental_days * car_daily_cost


def holiday_cost(city_flight, num_nights, rental_days):
    return plane_cost(city_flight) + hotel_cost(num_nights) + car_rental(rental_days)


choice = True
while choice == True:
    city_flight_location = input('Options:\nParis.\nMadrid.\nBerlin\nPlease enter one of the following cities you would like to travel to: ').lower() # Added lower so the user can type with or without capital letter.
    if city_flight_location == 'paris':         
        print(f'You have chosen: {city_flight_location.capitalize()}. ') # Capitalize to add the capital letter whilst printing.
        break    
    elif city_flight_location == 'madrid':
        print(f'You have chosen: {city_flight_location.capitalize()}. ')    
        break       
    elif city_flight_location == 'berlin':
        print(f'You have chosen: {city_flight_location.capitalize()}. ')     
        break                
    else:        
        print('You have entered an invalid city.')

while choice == True:
    num_nights_input = input('\nHow many nights are you planning on staying at the hotel? ')
    if num_nights_input.isdigit():             
        num_nights = int(num_nights_input)
        print(f'You will be staying for a total of: {num_nights_input} nights at the hotel.')        
        break        
    else:        
        print(f'You have entered \'{num_nights_input}\' which is an invalid number.')

while choice == True:
    rental_days_input = input('\nHow many days will you need to hire a car for? ')
    if rental_days_input.isdigit():             
        rental_days = int(rental_days_input)
        print(f'You will be hiring a car for the total of: {rental_days_input} days.')        
        break        
    else:        
        print(f'You have entered \'{rental_days_input}\' which is an invalid number.')

print(f'\nYou will be traveling to {city_flight_location.capitalize()} and your total flight cost including return ticket is of {plane_cost(city_flight_location)}£.')
print(f'You will be staying at the hotel for {num_nights} nights and your total hotel cost is of {hotel_cost(num_nights)}£.')
print(f'You will be hiring a car for {rental_days} days and your total car rental cost is of {car_rental(rental_days)}£.')
print(f'The total cost of your holiday including hotel stay, return flight ticket and car rental for the entire trip is of: {holiday_cost(city_flight_location, num_nights, rental_days)}£.')
