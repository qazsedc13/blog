Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.path
['', 'C:\\Program Files\\Python35-32\\Lib\\idlelib', 'C:\\Program Files\\Python35-32\\python35.zip', 'C:\\Program Files\\Python35-32\\DLLs', 'C:\\Program Files\\Python35-32\\lib', 'C:\\Program Files\\Python35-32', 'C:\\Program Files\\Python35-32\\lib\\site-packages']
>>> dir(sys)
['__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe', '_home', '_mercurial', '_xoptions', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_coroutine_wrapper', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'set_coroutine_wrapper', 'setcheckinterval', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'version', 'version_info', 'warnoptions', 'winver']
>>> help(sys.ver)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    help(sys.ver)
AttributeError: module 'sys' has no attribute 'ver'
>>> help(sys.version)
No Python documentation found for '3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)]'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> sys.version
'3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)]'
>>> version
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    version
NameError: name 'version' is not defined
>>> from sys import *
>>> version
'3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)]'
>>> import os
>>> os.getcwd()
'C:\\Program Files\\Python35-32'
>>> os.system('ping 8.8.8.8 -t')
-1073741510
>>> 
