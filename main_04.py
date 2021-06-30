import csv
import re
import os

nodecount = 9

options_read_dir = '/Users/junho/Downloads/parsing/data/'
options_read_filename = 'sys.20210401.log'
options_write_dir = '/Users/junho/Downloads/parsing/'

vari_write_filename_sdw = "write_filename_sdw"
vari_write_filename_sdw1 = options_read_filename + "_rewrite_" + "sdw" + "_"


def make_table():
    
for i in range (1, nodecount + 1):
    globals()['sdw{}'.format(i)] = "sdw" + str((i))

for j in range(1, nodecount + 1):
    globals()['sdw{}'.format(j) + '_outfile'] = open(options_write_dir + globals()['sdw{}'.format(j)] + '_outfile', 'w')
    globals()['sdw{}'.format(j) + '_outfile_deli'] = open(options_write_dir + globals()['sdw{}'.format(j)] + '_outfile_01_deli', 'w')

for file_name in os.listdir(options_read_dir):
    if "sys." in file_name:
        source_file = open(options_read_dir + file_name, "r")
        print(source_file)
        for data in source_file:
            for k in range(1, nodecount + 1):
                if globals()['sdw{}'.format(k)] in data:
                    x = []
                    x = (data.split('|'))
                    field_1st       = x[0].split()
                    field_name      = field_1st[0]

                    field_2nd       = x[1].split()
                    field_date      = field_2nd[0]
                    field_time      = field_2nd[1]

                    field_3rd       = x[2].split()
                    field_cpu_usr   = (field_3rd[0])
                    field_cpu_sys   = (field_3rd[1])
                    field_cpu_idle  = (field_3rd[2])
                    field_cpu_wai   = (field_3rd[3])
                    field_cpu_hiq   = (field_3rd[4])
                    field_cpu_siq   = (field_3rd[5])

                    field_4th       = x[3].split()
                    field_dsk_read  = field_4th[0]
                    field_dsk_writ  = field_4th[1]

                    field_5th = x[4].split()
                    field_net_recv  = field_5th[0]
                    field_net_send  = field_5th[1]

                    field_6th = x[5].split()
                    field_memory_used   = field_6th[0]
                    field_memory_buff   = field_6th[1]
                    field_memory_cach   = field_6th[2]
                    field_memory_free   = field_6th[3]






                    #y = str(x[0]) + ',' + str(x[1]) + ',' + str(x[2]) + ',' + str(x[3]) + ',' + str(x[4]) + ',' + str(x[5])
                    #print(y)

                    # globals()['sdw{}'.format(j) + '_outfile'] = open(options_write_dir + globals()['sdw{}'.format(j)] + '_outfile', 'w')
                    # globals()['sdw{}'.format(k) + '_outfile'].write(str(x))
                    # globals()['sdw{}'.format(j) + '_outfile'].close




# fields = ('date', 'time', 'cpu_usr', 'cpu_sys', 'cpu_idle', 'cpu_wait' , 'cpu_hiq', 'cpu_siq',
#           'disk_read', 'disk_write', 'net_send', 'net_reveive',
#           'memory_used', 'memory_buff' , 'memory_cache' , 'memory_free')
