#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

from os.path import splitext

def convert(input):
    with open(input, 'r') as i:
        name, ext = splitext(input)
        stream = i.read()
        lines = stream.split('\n')
        with open('{0}.js'.format(name), 'w') as o:
            o.write('export default [\n')
            for line in lines:
                o.write('  \'{0}\',\n'.format(line.replace('\'', '\\\'')))
            o.write(']\n')

if __name__ == '__main__':
    convert(argv[1])
