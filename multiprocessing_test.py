#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import pandas as pd
import multiprocessing
import os

import numpy as np
import pandas as pd
import joblib


def method(df_path):
    print("starting method")
    df = pd.read_pickle(df_path)
    print("pickle loaded")
    df.copy()
    print("exit method")


def main():
    df = pd.read_pickle("df")
    df.copy()

    print("Starting pool")
    pool = multiprocessing.Pool(1)
    pool.map(method, ['df' for _ in range(10)])


if __name__ == "__main__":
    main()

