from utils import get_words, write_words
from reber import EmbeddedReber


def main():
    """
    Examples
    --------
    To run with default settings.

        python main.py

    To generate 100 false and true words.

        python main.py --nwords=100

    To specify the 12-letter alphabets.

        python main.py --alphabet=hdjsklbmdiuh

    To generate a list of words that are all unique.

        python main.py --distinct=True
    """

    import argparse

    parser = argparse.ArgumentParser(description='Creates a list of Reber words and incorrect Reber words.')

    parser.add_argument('--alphabet', default='BTSXSPXTVPVE', type=str,
                        help="Twelve letter alphabet to use.  The default value corresponds to the embedded Reber Gram's assignment of edge letters.")
    parser.add_argument('--nwords', default=1000, type=int,
                        help="Default number of words to generate -- n true and n false words will be created.")
    parser.add_argument('--distinct', default=False, type=bool,
                        help="True if all words should be unique. False if word list can contain repeats")
    parser.add_argument('--outfile', default='train.csv', type=str,
                        help="File path of the csv where the words and the class will be storred.")

    args = parser.parse_args()


    assert args.alphabet.__len__() == 12, "The string length for the alphabet must equal twelve."

    alphabet = list(args.alphabet)

    eb = EmbeddedReber(alphabet)
    eb.create_edges()
    true_words = get_words(eb, args.nwords, distinct=args.distinct)

    # TODO: use a generic function to enable user defined way of makin false words.
    # false words
    alphabet[4] = 'Z'
    eb = EmbeddedReber(alphabet)
    eb.create_edges()

    # make sure real words weren't accidentally introduced into the negative set.
    false_words = []
    while len(false_words) < len(true_words):
        false_words.extend([word for word in get_words(eb, args.nwords, distinct=args.distinct) if word not in true_words])
    false_words = false_words[:args.nwords]

    write_words(args.outfile, true_words=true_words, false_words=false_words)


if __name__ == '__main__':
    import sys
    sys.exit(main())