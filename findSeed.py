import os
from random import seed
import sys
import requests
import json
import time
from multiprocessing import Process
import subprocess
import signal

def osop(op):
    filelist=os.listdir('fsg_seeds')
    txtfile=[]
    for files in filelist:
        if files[-4:]=='.txt':
            txtfile.append(int(files[:-4]))
    if op:
        return max(txtfile)
    else:
        return min(txtfile)

def seedbankop(seed):
    f = open("fsg_seeds\\{}.txt".format(osop(1)+1), 'w')
    f.write(seed)
    f.close()
    f = open("fsg_attemps.txt", 'w')
    f.write(str(osop(1)+1))
    f.close()

def display_seed(verif_data, seed):
    if (seed == ""):
        print("Seed Timed Out\n")
    else:
        print(f"Seed Found({verif_data['iso']}): {seed}")
        seedbankop(seed)
        print(f"Temp Token: {verif_data}\n")

def run_seed(filter):
    resp = requests.get(f"https://fsg2.bili2er0.workers.dev/?filter={filter}")
    res_json = resp.json()
    sseed = res_json.get("struct")
    sclass = res_json.get("class")
    randbiome = res_json.get("randbiome")
    pref = res_json.get("pref")  # village and/or shipwreck preference
    cmd = requests.get(f'https://fsg.bili2er0.workers.dev/proxy2?class={sclass}&pref={pref}&randbiome={randbiome}&struct={sseed}')
    seed = cmd.text
    display_seed(res_json, seed)

def start_run():
    print("FindSeed has started...\n")
    with open('settings.json') as filter_json:
        read_json = json.load(filter_json)
        filter = read_json["filter"]
        num_processes = read_json["thread_count"]
    processes = []
    for i in range(num_processes):
        processes.append(Process(target=run_seed, args=(filter,)))
        processes[-1].start()

def count():
    filelist=os.listdir('fsg_seeds')
    txtfile=[]
    for files in filelist:
        if files[-4:]=='.txt':
            txtfile.append(int(files[:-4]))
    if len(txtfile) <= 1:
        start_run()
        return True
    else: return False

def seed_scl():
    seed=""
    if (not os.path.exists("seed.txt")) and os.path.exists("fsg_seeds\\{}.txt".format(osop(0))):
        f = open("fsg_seeds\\{}.txt".format(osop(0)), 'r')
        seed = f.read()
        print(seed)
        f.close()
        f = open("seed.txt", 'w')
        f.write(seed)
        f.close()
        if not count():
            os.remove("fsg_seeds\\{}.txt".format(osop(0)))

if __name__ == '__main__':
    timecount=0
    while(True):
        if timecount%30==0:
            count()
        seed_scl()
        time.sleep(2)
        timecount+=1
        

