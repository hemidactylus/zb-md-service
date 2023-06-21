import sys

from cqlsession import getCQLSession


if __name__ == '__main__':
    mode = sys.argv[1]
    #
    ses = getCQLSession(mode=mode)
    #
    for row in ses.execute('select * from cassio_tutorials.people limit 2'):
        print(row)
