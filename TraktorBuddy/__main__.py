# SPDX-FileCopyrightText: 2022-present Didier Malenfant <coding@malenfant.net>
#
# SPDX-License-Identifier: MIT

import sys

from .TraktorBuddy import TraktorBuddy


def main():
    tktbud = None

    try:
        # -- Remove the first argument (which is the script filename)
        tktbud = TraktorBuddy(sys.argv[1:])

        if tktbud is not None:
            tktbud.main()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print('Execution interrupted by user.')
        pass

    if tktbud is not None:
        tktbud.shutdown()


if __name__ == '__main__':
    main()
