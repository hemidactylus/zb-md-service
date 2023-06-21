import sys

from cqlsession import getCQLSession

KEYSPACE = "cassio_tutorials"
TABLE = "people"

if __name__ == '__main__':
    mode = sys.argv[1]
    #
    ses = getCQLSession(mode=mode)
    #
    for row in ses.execute(f"select * from {KEYSPACE}.{TABLE} limit 2"):
        print(row)
