"""Command-line program for generating an Excel spreadsheet for a given ADF calculation result."""
import argparse
import pyorbb


def create_subparser(parent_parser: argparse.ArgumentParser):
    desc = "Read orbital information from an ADF calculation and write them to an Excel file."
    subparser = parent_parser.add_parser('excel', help=desc, description=desc)
    subparser.add_argument("-o", "--output", 
                           type=str, 
                           help="Set the output Excel file to write to.", 
                           default=None)
    subparser.add_argument("rkf",
                           type=str,
                           help="The path to the `adf.rkf` file to summarize in an Excel file.")


def main(args: argparse.Namespace):
    orbs = pyorbb.Orbitals(args.rkf)
    out = args.output
    if out is None:
        out = args.rkf + '.xlsx'
    orbs.write_excel(out)
