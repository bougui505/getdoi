#!/usr/bin/env python3
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2021-01-21 09:52:56 (UTC+0100)

from crossref.restful import Works


if __name__ == '__main__':
    import argparse
    # argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True, exit_on_error=True)
    parser = argparse.ArgumentParser(description='')
    # parser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
    parser.add_argument('-s', '--search', type=str, required=True, help="Query bibliographic information, useful for citation look up. Includes titles, authors, ISSNs and publication years")
    args = parser.parse_args()

    works = Works()
    w = works.query(bibliographic=args.search)
    for item in w:
        title = item['title'][0]
        doi = item['DOI']
        print(f"title: {title}")
        print(f"doi: {doi}")
