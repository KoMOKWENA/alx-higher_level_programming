#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for item in my_list:
            if num < x:
                print(item, end=" ")
                num += 1
        print()
        return num
    try:
        print("An error occurred")
