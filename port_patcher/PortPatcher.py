from distutils.version import LooseVersion, StrictVersion
from FreeBSDPortParser import FreeBSDPortParser
import argparse
import grako

def write_elements(file, elems):
    for elem in elems:
        if isinstance(elem, grako.ast.AST):
            write_elements(file, elem.values())
        elif isinstance(elem, grako.contexts.Closure):
            write_elements(file, elem)
        elif isinstance(elem, list):
            write_elements(file, elem)
        else:
            print elem,
            file.write(elem)

class PortPatcher(object):
    def __init__(self):
        pass

    def patch(self, makefile, version):
        makefile_text = None
        with open(makefile) as f:
            makefile_text = f.read()

        makefile_parser = FreeBSDPortParser(comments_re='', eol_comments='')
        makefile = makefile_parser.parse(makefile_text, rule_name='MAKEFILE')

        # check if it is a minor update
        new_version = LooseVersion(version)

        version_ast_list = filter(lambda x:x[0] == 'PORTVERSION', makefile)

        assert len(version_ast_list) == 1, 'Only one PORTVERSION is allowed in Makefile'

        version_ast = version_ast_list[0]
        old_version = LooseVersion(version_ast[-1][0])

        print 'Old version', old_version
        print 'New version', new_version

        minor_update = old_version < new_version

        print 'Is minor update?', minor_update

        if not minor_update:
            return

        # make backup of a makefile

        # update version in parsed ast
        version_ast[-1][0] = version

        # save makefile
        new_makefile = open('Makefile.new', 'w')

        for ast in makefile:
            write_elements(new_makefile, ast)

        new_makefile.close()

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
