from FreeBSDPortParser import FreeBSDPortParser
import argparse
import semantic_version

class PortPatcher(object):
    def __init__(self):
        pass

    def patch(self, makefile, version):
        makefile_text = None
        with open(makefile) as f:
            makefile_text = f.read()

        makefile_parser = FreeBSDPortParser(makefile_text)

        # check if it is a minor update
        new_version = semantic_version.Version(version)

        # make backup of a makefile
        # update version in parsed ast
        # save makefile

def main():
    argparser = argparse.ArgumentParser(description='FreeBSD Port Patcher')
    argparser.add_argument('-M', '--makefile', dest='makefile', required=True, help='port\'s makefile')
    argparser.add_argument('-V', '--version', dest='version', required=True, help='new version')
    argparser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False)

    args = argparser.parse_args()

    port_patcher = PortPatcher()
    port_patcher.patch(args.makefile, args.version)

if __name__ == '__main__':
    main()
