import time
import os
import subprocess



if __name__ == '__main__':

    f = open('a2_test_run_2_results.txt','r')
    data = f.readlines()
    f.close()
    result = {}
    list_result = []
    fullname="Linh Van Ha"
    for item in data:
        if item.startswith('+'):
            commands =item.strip()
            list_result = list_result.copy()            
            list_result.clear()  
        else:  
            list_result.append(item)
            result[commands] = list_result


    print(result['+ ./ur.py -h'])
    # c = result["+ ./ur.py -u user5 -t daily a2_test_data_2 -v"]
    cmd = 'python3.6 a2_'+student+'.py'+ '-h'
    print('Test run command',':',cmd)
    p1 = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    result_fromcmd = p1.communicate()[0].decode('utf-8').strip('\n') 
    # print(c)
    # print("")
    # print(test.split("\n"))
    # print(c == test.split("\n"))
