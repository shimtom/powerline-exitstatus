# vim:fileencoding=utf-8:noet
from __future__ import (unicode_literals, division, absolute_import, print_function)

from powerline.theme import requires_segment_info


@requires_segment_info
def exit_status(pl, segment_info, only_failed=False, success_contents="\u2714 ", fail_contents="\u2715 "):
    '''Return last exit status

    :param bool only_failed:
        If False (default) shows exit status always. Otherwise shows only
        fail status and does't show success status.

    :param str success_contents:
        A format string to produce the text on success. Default value "✔ "

    :param str fail_contents:
        A format string to produce the text on failure. Default value "✕ ".
        Use "{} " to get the status code itself.

    Highlight groups used: ``exit_status_fail``, ``exit_status_success``
    '''
    exit_code = segment_info['args'].last_exit_code
    if not exit_code:
        if only_failed:
            return None
        return [{'contents': success_contents.format(exit_code), 'highlight_groups': ['exit_status_success']}]
    return [{'contents': fail_contents.format(exit_code), 'highlight_groups': ['exit_status_fail']}]
