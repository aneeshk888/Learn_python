# Travel Weather Planner

# Variables
distance_mi = 10          # number (miles to travel)
is_raining = True         # boolean (True if raining, False otherwise)
has_bike = True           # boolean (True if user has a bike)
has_car = True            # boolean (True if user has a car)
has_ride_share_app = True # boolean (True if user has a ride-share app)

# Conditional logic
if not distance_mi:  # falsy check (0 or None)
    print(False)

elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)

elif distance_mi > 1 and distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)

elif distance_mi > 6:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
