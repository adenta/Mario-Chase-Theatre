import chase, numpy

#Inputs
trials = 500
marioAI = 3
toadAI = 3
#End Inputs

#Scorekeeping variables
stats = []
toad_win_count = 0
times= []

#Trialrunner
for i in range(trials):
    try:
        res = chase.trial(4,150,0,marioAI,toadAI)
    except:
        res = [False, 150]
    times.append(res[1])
    if res[0]:
        toad_win_count +=1

#Results
print "Mario AI", marioAI
print "Toad AI", toadAI
print trials, "Trials:"
print "Mean Game Time:", numpy.mean(times)
print "Toad Win %",  (float(toad_win_count)/float(trials))*100
