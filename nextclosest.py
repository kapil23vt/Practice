def nextClosestTime(time):
    isV = lambda t: t[:2] < '24' and t[3:] < '60'
    can = sorted(set(time))[:-1]
    for i in (4, 3, 1, 0):
        for n in can[can.index(time[i])+1:]:
            ntime = (time[:i] + n).ljust(5, can[0])
            if isV(ntime):
                return ntime[:2] + ':' + ntime[3:]
            else:
                break
    return can[0]*2 + ':' + can[0]*2


print(nextClosestTime('11:00'))