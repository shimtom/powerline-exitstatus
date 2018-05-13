# vim:fileencoding=utf-8:noet
from __future__ import (unicode_literals, division, absolute_import, print_function)
from powerline.theme import requires_segment_info


@requires_segment_info
def exit_status(pl, segment_info):
    '''Return last exit status

    Highlight groups used: ``exit_status_fail``, ``exit_status_success``
    '''
    exit_code = segment_info['args'].last_exit_code
    if not exit_code:
        return [{'contents': '\u2714 ', 'highlight_groups': ['exit_status_success']}]
    return [{'contents': '\u2715 ', 'highlight_groups': ['exit_status_fail']}]
