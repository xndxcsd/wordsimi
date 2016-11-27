# !/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

import MySQLdb


class VecDispatcher:
    def __init__(self):
        self.__conn = MySQLdb.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            db='wordsimi',
            charset='utf8',
        )
        self.__cur = self.__conn.cursor()

    def getVector(self, word):
        sql = "SELECT * FROM vector WHERE f1 = '%s'" % word
        self.__cur.execute(sql)

        row = self.__cur.fetchone()
        if row is None :
            return None
        return row[1:]


if __name__ == '__main__':
    a = VecDispatcher()
    a.getVector("经济")
