from tribus.common.cmd import Command

class BuildPackage(Command):
	
    subcommand_name = 'buildpackage'
    subcommand_help = 'Helps build a package'
    subcommand_args = {
	    'version': [['-v', '--version'], {
	        'action': 'store_true',
	        'dest': 'print_version',
	        'default': False
	    }],
	    # 'help': [['-h', '--help', '--ayuda'], {
	    #     'action': 'store_true',
	    #     'dest': 'print_help',
	    #     'default': False
	    # }],
	    'usage': [['-u', '--usage', '--uso'], {
	        'action': 'store_true',
	        'dest': 'print_usage',
	        'default': False
	    }],
	}

    def __init__(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def run(self, *args, **kwargs):
        print self.subcommand_name
