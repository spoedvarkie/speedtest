# creates the speed test instance and performs the run(s)
from speedtest import Speedtest
from datetime import datetime
import Calls as call
import time

# List for storing values during run
# To be saved after every runs, residuals saved after run ends
# Residual runs -> runs over 100 interval before next interval
listValues = list()

# Counter to user prompt loop
counter = 0

# Loop counter for amount of runs - Prompt to user
count = 1

# Average vars
avgDuration = 0
avgPing = 0
avgUp = 0
avgDown = 0

# Total vars
totalDuration = 0
totalPing = 0
totalUp = 0
totalDown = 0
totalSent = 0
totalReceived = 0

# object initialisation
st = Speedtest()

# User prompt loop to get amount of runs
userInput = input('Amount of runs?\n')
while not call.check_user_input(userInput) and counter < 3:
    counter += 1
    print("input failed attempt ", counter, "(3)", sep='')
    userInput = input('Reruns?(int)')

# Convert user input to int
reruns = int(userInput)

# Check for residual runs
residualToWrite = False
if count % 100 > 0:
    residualToWrite = True

# Run begins loop
print("--------------RUN START--------------")
while count <= reruns:
    # Get stating time and trigger upload and download
    startTime = time.time()
    st.get_best_server()
    st.upload(threads=5, pre_allocate=False)
    st.download(threads=5)
    endTime = time.time()

    # Current run values
    currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    currentDuration = endTime - startTime
    currentPing = st.results.ping
    currentUpload = round(st.results.upload / 1000000, 2)
    currentDownload = round(st.results.download / 1000000, 2)
    print("-------------Current------------")
    print("Time : ", currentTime, sep='')
    print("Run : ", count, sep='')
    if currentDuration < 60:
        print("Duration : ", round(currentDuration, 2), "(s)", sep='')
    else:
        print("Duration : ", round(currentDuration, 2), "(min)", sep='')
    print("Ping : ", currentPing, " ms", sep='')
    print("Upload Speed : ", currentUpload, " Mbps", sep='')
    print("Download Speed : ", currentDownload, " Mbps", sep='')

    # Total run values
    totalDuration += (endTime - startTime)
    totalUp += st.results.upload
    totalDown += st.results.download
    totalPing += st.results.ping
    totalSent += st.results.bytes_sent
    totalReceived += st.results.bytes_received
    print("-------------Total-------------")
    # Total duration of runs
    if totalDuration <= 60:
        print("Runtime : ", round(totalDuration, 2), " (s)", sep='')
    elif (totalDuration > 60) and (totalDuration <= 3600):
        print("Runtime : ", round(totalDuration / 60, 2), " (min)", sep='')
    elif totalDuration > 3600:
        print("Runtime : ", round(totalDuration / 3600, 2), " (h)", sep='')

    # Total sent/upload
    if round(totalSent / 1000000, 2) <= 100:
        print("Sent : ", round(totalSent / 1000000, 2), " Kb", sep='')
    elif (round(totalSent / 1000000, 2) > 100) and (round(totalSent / 1000000, 2) <= 1000):
        print("Sent : ", round(totalSent / 1000000, 2), " Mb", sep='')
    elif round(totalSent / 1000000, 2) > 1000:
        print("Sent : ", round(totalSent / 1000000000, 2), " Gb", sep='')

    # Total received/download
    if round(totalReceived / 1000000, 2) <= 100:
        print("Received : ", round(totalReceived / 1000000, 2), " Kb", sep='')
    elif (round(totalReceived / 1000000, 2) > 100) and (round(totalReceived / 1000000, 2) <= 1000):
        print("Received : ", round(totalReceived / 1000000, 2), " Mb", sep='')
    elif round(totalReceived / 1000000, 2) > 1000:
        print("Received : ", round(totalReceived / 1000000000, 2), " Gb", sep='')

    # Averages
    avgDuration = totalDuration / count
    avgPing = totalPing / count
    avgUp = totalUp / count
    avgDown = totalDown / count
    print("------------Average------------")
    if avgDuration < 60:
        print("Duration : ", round(avgDuration, 2), " (s)", sep='')
    else:
        print("Duration : ", round(avgDuration, 2), " (min)", sep='')
    print("Ping : ", round(avgPing, 2), " ms", sep='')
    print("Upload Speed : ", round(avgUp / 1000000, 2), " Mbps", sep='')
    print("Download Speed : ", round(avgDown / 1000000, 2), " Mbps", sep='')
    print("-----------End run ", count, "-----------", sep='')
    if count < 100:
        listValues.append((currentTime, count, currentDuration, currentPing, currentUpload, currentDownload,
                           totalDuration, totalSent, totalReceived, avgDuration, avgPing,
                           avgUp, avgDown))
    else:
        call.write_results(listValues)
        listValues.clear()
        listValues.append((currentTime, count, currentDuration, currentPing, currentUpload, currentDownload,
                           totalDuration, totalSent, totalReceived, avgDuration, avgPing,
                           avgUp, avgDown))
    count += 1

if residualToWrite:
    call.write_results(listValues)

print("---------------RUN END---------------")
print("=============================\nSpeedtest Completed\n=============================")
