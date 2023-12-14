#!/usr/bin/env python3

import argparse

def main(args):

    time = args.time
    start = t_to_i(time)
    max = 60 * 22
    offset(start, max, args.time, args.bow)

def t_to_i(tm):
    return int(tm.split(":")[0]) * 60 + int(tm.split(":")[1])

def frmt(tm):

    a = str(tm // 60)
    b = str(tm % 60)

    return f'{a:0>2}:{b:0>2}'

def offset(curr, max, time, bow):

    additions = ''
    interest = ''
    bad_reason = ''
    found = False
    bad = False
    if bow and bow != 'done':

        req_bow_time = t_to_i(bow)
        if req_bow_time >= curr and req_bow_time <= curr + 40:

            additions += '\033[34m' + bow + ' \033[0m|'
            bow = 'done'
            found = True
        elif curr > req_bow_time:
            bow = 'done'
            found = False
            bad = True
            bad_reason = "|! Lightning won't make wallrun. !|"
    if found:

        interest = '\033[36m'

    if bad:

        interest = '\033[32m'

    color = '\033[0m'

    if curr > max:
        return

    print(f'{interest}{frmt(curr)}\033[0m -> {interest}{frmt(curr + 50)}\033[0m | {color}{additions}\033[0m{bad_reason}')
    offset(curr + 110, max, time, bow)

def bow():

    pass

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        prog='AG Timer Calculator',
        description='A thorough anti-grav timer calculator for der eisendrache.',
        epilog='Author: Caolan Cochrane (Alias: C4THR33N, cablemanager)'
    )

    parser.add_argument('time', metavar='time',
                        help='The anti-grav start-time.')
    parser.add_argument('-b', '--bow', metavar='b',
                        help='The bow grab time.')
    parser.add_argument('-p', '--plungerstart', metavar='p',
                        help='Plunger start time.')
    parser.add_argument('-P', '--plungerend', metavar='P',
                        help='Plunger hit time.')
    parser.add_argument('-l', '--lightning', metavar='l',
                        help='Lightning wallrun start time.')
    parser.add_argument('-w', '--wolf', metavar='w',
                        help='Wolf wallrun time.')
    parser.add_argument('-t', '--tp', metavar='t',
                        help='First back in time teleport time.')
    args = parser.parse_args()
    print(args)
    main(args)
