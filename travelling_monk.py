def calculate_distance(list, time):
    time_travelled = 0.0
    distance_travelled = 0.0
    for segment in list:
        segment_distance = segment[0]
        segment_time = segment[1]
        if segment_time+time_travelled>=time:
            temp_time = time - time_travelled
            return distance_travelled + temp_time*(segment_distance/segment_time)
        else:
            distance_travelled += segment_distance
            time_travelled += segment_time
    return distance_travelled

a, d = list(map(int,input().strip().split(' ')))
ascent = []
descent = []
total_distance = 0.0
for i in range(a):
    distance, time = list(map(int,input().strip().split(' ')))
    ascent.append([distance,time])
    total_distance += distance
    
for i in range(d):
    segment, time = list(map(int,input().strip().split(' ')))
    descent.append([segment,time])

lo = 0.0
hi = 500000.0
while lo < hi:
    midpoint = lo + (hi - lo) / 2
    
    ascent_distance = calculate_distance(ascent, midpoint)
    descent_distance = calculate_distance(descent, midpoint)

    if ascent_distance - (total_distance-descent_distance)>=0:
        hi = midpoint 
        if hi-lo<=10e-5:
            break

    else:
        lo = midpoint + 10e-5
print(hi)



