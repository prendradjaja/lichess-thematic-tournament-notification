import os
import json


def main():
    print('Loading...')

    response = os.popen(f'curl -s https://lichess.org/api/tournament').read()
    tourneys = json.loads(response)

    print()

    found = False
    for t in tourneys['started']:
        if not is_thematic(t):
            continue
        if not found:  # first found
            print('Ongoing:')
        print('-', t['fullName'])
        found = True
    if found:
        print()

    found = False
    for t in tourneys['created']:
        if not is_thematic(t):
            continue
        if not found:  # first found
            print('Upcoming:')
        print('-', t['fullName'])
        found = True

def is_thematic(t):
    return 'position' in t

main()
