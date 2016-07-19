import sys
import time
import datetime
DEBUG_LEVEL = 1
WARN_LEVEL = 2
INFO_LEVEL = 3
ERROR_LEVEL = 4


def info(msg, level, module_name = None, function_name= None, log_file=None):
    if level > INFO_LEVEL:
        return 
    if not log_file:
        print >> sys.stderr, '\033[1;32;40m',  #green  
        print >> sys.stderr, "\b[INFO]",
        if module_name and function_name:
            print >> sys.stderr, '\033[1;33;40m',   #yellow
            print >> sys.stderr, "\b[%s.%s]" % (module_name, function_name),
        print >> sys.stderr, '\033[0m',
        print >> sys.stderr, '\b[' + msg + '] ' + str(datetime.datetime.fromtimestamp(time.time()))
    else:
        with open(log_file, 'a') as log_file_obj:
            print >> log_file_obj, '[INFO]', 
            if module_name and function_name:
                print >> log_file_obj, "[%s.%s]" % (module_name, function_name),
            print >> log_file_obj, '[' + msg + '] ' + str(datetime.datetime.fromtimestamp(time.time()))
             

def warn(msg, level, module_name=None, function_name=None, log_file=None):
    if level > WARN_LEVEL:
        return
    if not log_file:
        print >> sys.stderr, '\033[1;35;40m', #pink 
        print >> sys.stderr, "\b[WARNING]",   
        if module_name and function_name:
            print >> sys.stderr, '\033[1;33;40m',   #yellow
            print >> sys.stderr, "\b[%s.%s]" % (module_name, function_name),
        print >> sys.stderr, '\033[0m',
        print >> sys.stderr, '\b[' + msg + '] ' + str(datetime.datetime.fromtimestamp(time.time()))
    else:
        with open(log_file, 'a') as log_file_obj:
            print >> log_file_obj, '[WARNING]',
            if module_name and function_name:
                print >> log_file_obj, "[%s.%s]" % (module_name, function_name),
            print >> log_file_obj, '[' + msg + '] ' + str(datetime.datetime.fromtimestamp(time.time()))
            
def error(msg, level, module_name=None, function_name=None, log_file=None): 
    if level > ERROR_LEVEL:
        return 
    if not log_file:
        print >> sys.stderr, '\033[1;31;40m',  #red 
        print >> sys.stderr, "\b[ERROR]",
        if module_name and function_name:
            print >> sys.stderr, '\033[1;33;40m',   #yellow
            print >> sys.stderr, "\b[%s.%s]" % (module_name, function_name),
        print >> sys.stderr, '\033[0m', 
        print >> sys.stderr, '\b[' + msg + '] ' + str(datetime.datetime.fromtimestamp(time.time()))
    else:
        with open(log_file, 'a') as log_file_obj:
            print >> log_file_obj, "[ERROR]",
            if module_name and function_name:
                print >> log_file_obj, "[%s.%s]" % (module_name, function_name),
            print >> log_file_obj, '[' + msg + '] ' + str(datetime.datetime.fromtimestamp(time.time()))
            
def debug(msg, level, module_name = None, function_name = None, log_file=None): 
    if level > DEBUG_LEVEL:
        return
    if not log_file:
        print >> sys.stderr, '\033[1;36;40m',  #cyan 
        print >> sys.stderr, "\b[DEBUG]",
        if module_name and function_name:
            print >> sys.stderr, '\033[1;33;40m',   #yellow
            print >> sys.stderr, "\b[%s.%s]" % (module_name, function_name),
        print >> sys.stderr, '\033[0m', 
        print >> sys.stderr, '\b[' + msg + ']'
    else: 
        with open(log_file, 'a') as log_file_obj:
            print >> log_file_obj, "[DEBUG]",
            if module_name and function_name:
                print >> log_file_obj, "[%s.%s]" % (module_name, function_name),
            print >> log_file_obj, '[' + msg + ']'

if __name__ == '__main__':
    
    LEVEL = 1 
    info('try something new', LEVEL, log_file='test.log')
    warn('try something new', LEVEL, log_file='test.log')
    error('try something new', LEVEL, log_file = 'test.log')
    debug('try something new', LEVEL, log_file = 'test.log')
