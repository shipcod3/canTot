#!/usr/bin/python3
from sploitkit import FrameworkConsole
from tinyscript import *

class MySploitConsole(FrameworkConsole):
    #TODO: set your console attributes
    sources = {'banners':"banners"}
    pass

if __name__ == '__main__':
    parser.add_argument("-d", "--dev", action="store_true", help="enable development mode")
    parser.add_argument("-r", "--rcfile", type=ts.file_exists, help="execute commands from a rcfile")
    initialize(exit_at_interrupt=False)
    c = MySploitConsole(
        "canTot",
        #TODO: configure your console settings
        dev=args.dev,
        debug=args.verbose,
    )
    c.rcfile(args.rcfile) if args.rcfile else c.start()
    
