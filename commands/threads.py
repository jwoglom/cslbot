# Copyright (C) 2013-2015 Samuel Damashek, Peter Foley, James Forcier, Srijay Kasturi, Reed Koser, Christopher Reffett, and Fox Wilson
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import threading
import re
from helpers.command import Command


@Command('threads')
def cmd(send, msg, args):
    """Enumerate threads.
    Syntax: !threads
    """
    for x in sorted(threading.enumerate(), key=lambda k: k.name):
        if re.match('Thread-\d+$', x.name):
            # Handle the main server thread (permanently listed as _worker)
            if x._target.__name__ == '_worker':
                send("%s running server thread" % x.name)
            # Handle the multiprocessing pool worker threads (they don't have names beyond Thread-x)
            elif x._target.__module__ == 'multiprocessing.pool':
                send("%s running multiprocessing pool worker thread" % x.name)
        # Handle everything else including MainThread and deferred threads
        else:
            send(x.name)
