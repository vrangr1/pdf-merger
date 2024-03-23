import argparse
import os
from pypdf import PdfWriter

def parse_args(args=None):
    parser=argparse.ArgumentParser(description="A very simple PDF Merger")
    parser.add_argument('--dir',type=str,required=True,\
                        help="will merge every pdf present in this directory")
    parser.add_argument('--outfile',type=str,required=False,default="result.pdf",\
                        help='path where the output pdf file should be created alongwith the name. default: "./results.pdf"')
    return parser.parse_args()

def pdf_merger(dir_path:str, outfile:str) -> None:
    dir_path = os.path.abspath(dir_path)
    assert(os.path.isdir(dir_path))
    files = os.listdir(dir_path)
    files = sorted(files)
    merger = PdfWriter()
    for file in files:
        if os.path.splitext(file)[1] != ".pdf":
            continue
        file_path = os.path.join(dir_path,file)
        merger.append(file_path)
    merger.write(outfile)
    merger.close()

if __name__ == '__main__':
    args = parse_args()
    pdf_merger(args.dir, args.outfile)