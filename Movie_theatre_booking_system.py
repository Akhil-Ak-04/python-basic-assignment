theatre_capacity = 350
total_bookings = 0
total_rejections = 0
total_tickets = 0

while theatre_capacity > 0:
    no_of_tickets = int(input('How many tickets do you need ? - '))
    if no_of_tickets == 0:
        break

    if not (0 < no_of_tickets <= 15):
        print('You can only buy up to 15 tickets')
        continue

    if no_of_tickets > theatre_capacity:
        print(f'You can only buy up to {theatre_capacity} tickets. Remaining seats: {theatre_capacity}')
        continue

    ages = input('Enter ages for each separated by a comma - ')
    ages_list = list(map(int, ages.split(',')))
    if no_of_tickets != len(ages_list):
        print('Number of tickets and ages do not match')
        continue

    if all(age >= 12 for age in ages_list):
        theatre_capacity -= no_of_tickets
        total_tickets += no_of_tickets
        total_bookings += 1
        print(f'BOOKING CONFIRMED - {no_of_tickets} tickets')
    else:
        total_rejections += 1
        print('''BOOKING REJECTED - Age restriction
Age must be above 12 for all members''')

    if theatre_capacity == 0:
        print('Theatre is now full.')
        break

print(f'Final Report: Total Bookings: {total_bookings}, Total Tickets Sold: {total_tickets}, Rejected Bookings: {total_rejections}, Remaining Seats: {theatre_capacity}')
