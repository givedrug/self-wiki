#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import re

base_dir = './docs_copy/'
base_space = 0
uncheck_dir_list = ['.idea', 'src']


def changeFile(base, name):
    fullname = os.path.join(base, name)
    fr = open(fullname, 'r')
    lines = fr.readlines()
    fr.close()

    def complete(value):
        v1 = value.group(1)
        v2 = value.group(2)
        return '[' + v1 + '](https://givedrug.github.io/self-wiki/' + base.lstrip(base_dir) + '/' + v2 + ')'

    for idx, line in enumerate(lines):
        lines[idx] = re.sub(r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)', complete, line)

    lines.insert(0, '# ' + name.rstrip('.md') + '\n\n')

    fw = open(fullname, 'w')
    fw.writelines(lines)
    fw.close()


def checkAllFile(base, file, base_space):
    list = os.listdir(base)
    list.sort()
    for name in list:
        fullname = os.path.join(base, name)
        if 'assets' in name:
            continue
        if os.path.isdir(fullname) and name not in uncheck_dir_list:
            file.write(' ' * base_space + '- <font color="#42b983"><b>' + name + '</b></font>' + '\n')
            checkAllFile(fullname, file, base_space + 2)
        if os.path.isfile(fullname) and base != base_dir and name.endswith('.md'):
            file.write(' ' * base_space + '- [' + name.rstrip('.md') + '](' +
                       fullname.lstrip(base_dir).replace(' ', '%20') + ')' + '\n')
            changeFile(base, name)


def main():
    sidebar_file = open(base_dir + '_sidebar.md', 'w')
    sidebar_file.write('- [<b>README</b>](README.md)' + '\n')
    checkAllFile(base_dir, sidebar_file, base_space)
    sidebar_file.close()


if __name__ == '__main__':
    main()
