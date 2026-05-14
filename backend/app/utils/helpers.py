# backend/app/utils/helpers.py

import os


def create_folder(path):

    if not os.path.exists(path):

        os.makedirs(path)