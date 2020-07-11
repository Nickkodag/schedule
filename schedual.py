import schedule
import time





def job():
    print("code")

def reading():
    print("what you reading mow(input())")    

def play():
    print("let me play")    

 
schedule.every(1).seconds.do(job)
schedule.every(2).seconds.do(reading)
schedule.every().day.at("04:30").do(play)


while True:
    schedule.run_pending()
    time.sleep(1)