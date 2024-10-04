import os
from argparse import ArgumentParser

def cmdline_args() -> dict:
    parser = ArgumentParser()
    # parser.add_argument(
    #     "-l",
    #     "--links",
    #     dest="links",
    #     help="[path] File containing liks and actions. The file should be a list of links, one per line, following the structure: url|action|comment (if action is comment). Actions can be one of the following: upvote, downvote, comment, join, leave. The file should be in the same directory as this script.",
    # )
    # parser.add_argument(
    #     "-a",
    #     "--accounts",
    #     dest="accounts",
    #     help="[path] File containing credentials for accounts to perform the actions with. The file should be a list of usernames and passwords, one per line, following the structure: username|password. The file should be in the same directory as this script.",
    # )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        help="[none] Print INFO messages to stdout",
    )
    parser.add_argument(
        "-x",
        "--xlsx",
        dest="xlsx",
        help="[path] File containing links, credentials and actions for accounts to perform the actions with. The file should be a xlsx file with one sheet that is structured with (serial_number:A1, link:B1, username:C1, pass:D1, mail:E1, mail_pass:F1, upvote:G1, downvote:H1, comment:I1). The file should be in the same directory as this script."
    )
    return vars(parser.parse_args())