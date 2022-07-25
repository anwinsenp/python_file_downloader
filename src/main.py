import sys
import getopt
import downloader
import signal

cancel_downloading = False


def handler(signum, frame):
    msg = "Ctrl+c was pressed. Do you really want to exit? y/n"
    print(msg)
    res = input()
    global cancel_downloading
    cancel_downloading = res == 'y'


signal.signal(signal.SIGINT, handler)


def main(argv):
    input_file = ''
    output_dir = ''
    global cancel_downloading

    try:
        opts, args = getopt.getopt(argv, 'hi:o:', ['ifile=', 'odir='])
    except getopt.GetoptError:
        print('main.py -i <input_file> -o <output_dir>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -i <input_file> -o <output_dir>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_dir = arg

    try:
        with open(input_file, 'r') as fp:
            line = fp.readline()
            while line and cancel_downloading == False:
                line = line.strip()
                downloader.download(line, output_dir=output_dir)
                line = fp.readline()
    except IOError as e:
        raise SystemExit(e)


if __name__ == "__main__":
    main(sys.argv[1:])
