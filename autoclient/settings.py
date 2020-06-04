import sys, os, time

PLUGINS_PATH_DICT = {
    'disk':'lib.plugins.disk.DiskPlugin',
    'network':'lib.plugins.network.NetworkPlugin',
    'memory':'lib.plugins.memory.MemoryPlugin',
}