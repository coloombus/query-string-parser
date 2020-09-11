# Copyright (c) 2020 <Riccardo Curcio>
#
# GNU GENERAL PUBLIC LICENSE
#    Version 3, 29 June 2007
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict
from querystring_parser.parser import *

import json


class parser:

    @staticmethod
    def parse(query_string, unquote=True):
        def recurse(pair, out=None, indent=0):
            if isinstance(pair, dict):
                (k, v) = pair.popitem()
                if out is None:
                    if isinstance(k, int) or k == '':
                        out = []
                    else:
                        out = OrderedDict()
                if isinstance(out, list) and (k == ''):
                    out.append(recurse(v, indent=indent+1))
                elif isinstance(out, list) and (k != ''):
                    out = dict(enumerate(out))
                    out[k] = recurse(v, out.get(k), indent=indent+1)
                elif isinstance(out, dict) and k == '':
                    numeric_indices = [k for k in out.keys() if isinstance(k, int)]
                    out[1+max(numeric_indices) if numeric_indices else 0] = recurse(v, out.get(k))
                elif isinstance(out, dict):
                    out[k] = recurse(v, out.get(k), indent=indent+1)
                else:
                    return recurse({k: v}, indent=indent+1)
                return out
            return pair

        plist = []
        if query_string == "":
            return mydict
        for element in query_string.split("&"):
            try:
                if unquote:
                    (var, val) = element.split("=")
                    var = urllib.unquote_plus(var)
                    val = urllib.unquote_plus(val)
                else:
                    (var, val) = element.split("=")
            except ValueError:
                raise MalformedQueryStringError
            plist.append(parser_helper(var, val))

        out = OrderedDict()
        for pair in plist:
            out = recurse(pair, out)
        return json.loads(json.dumps(out))
