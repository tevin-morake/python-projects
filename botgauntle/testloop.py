#!/usr/bin/python



def main():
    presidents = [{"Name": "Mark"}, {"Name": "Jerry"}, {"Name": "Joey"}]
    for i in range(len(presidents)) :
        print("President {}: {}".format(i + 1, presidents[i]["Name"]))
    pass
main()