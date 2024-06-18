#!/usr/bin/env python

import subprocess
import os

os.chdir("/home/seraj22200/work_pfeature/Pfeature-master/Standalone")

commands = [
    "python pfeature_bin.py -i ../../train_data_seq.csv -j AAB -o ../../train_AAB_1__.csv",
    "python pfeature_bin.py -i ../../train_data_seq.csv -j DPB -o ../../train_DPB__.csv",
    "python pfeature_bin.py -i ../../train_data_seq.csv -j PCB -o ../../train_PCB__.csv",
    "python pfeature_bin.py -i ../../train_data_seq.csv -j ALLBIN -o ../../train_ALLBIN__.csv",
    "python pfeature_comp.py -i ../../train_data_seq.csv -j DPC -o ../../train_DPC__.csv",
    "python pfeature_comp.py -i ../../train_data_seq.csv -j TPC -o ../../train_TPC__.csv",
    "python pfeature_comp.py -i ../../train_data_seq.csv -j PCP -o ../../train_PCP__.csv",
    "python pfeature_comp.py -i ../../train_data_seq.csv -j PRI -o ../../train_PRI__.csv",
    "python pfeature_comp.py -i ../../train_data_seq.csv -j ALLCOMP -o ../../train_ALLCOMP__.csv",
]

for command in commands:
    subprocess.call(["nohup"] + command.split(), stdout=open("nohup.out", "a"), stderr=open("nohup.err", "a"))