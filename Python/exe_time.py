# -*- coding: utf-8 -*-

from datetime import datetime

def exe_time(func):
    def new_func(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        print('-'*42)
        print("Start program at: {}".format(start_time))
        print("End program at  : {}".format(end_time))
        print("Total running time: {}".format(end_time - start_time))
        print('-'*42)
        return result

    return new_func

@exe_time
def main():
    for i in range(int(1e9)):
        pass

if __name__ == '__main__':
    main()
