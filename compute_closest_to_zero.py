
def compute_closest_to_zero(ts):
    if not ts:
        return 0
    else:
        min = ts[0];
        for item in ts:
            if abs(item) < abs(min):
                min = item
            else:
               if(min == -(item)):
                   min =abs(min)

    




print(compute_closest_to_zero([-5,5]))
print(compute_closest_to_zero([7,5,9,1,4]))
print(compute_closest_to_zero([-273]))
print(compute_closest_to_zero([5526]))
print(compute_closest_to_zero([-15,-7,-9,-14,-12]))
print(compute_closest_to_zero([-10,-10]))
print(compute_closest_to_zero([]))