#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv

class DataManager:
    def dataManager(self,fd,data):
        fd_csv = csv.writer(fd)
        fd_csv.writerow(data)