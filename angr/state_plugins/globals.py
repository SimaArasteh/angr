
import logging

from .plugin import SimStatePlugin

l = logging.getLogger('angr.state_plugins.globals')


class SimStateGlobals(SimStatePlugin):
    def __init__(self, backer=None):
        super(SimStateGlobals, self).__init__()
        self._backer = backer if backer is not None else {}

    def set_state(self, state, **kwargs):
        pass

    def merge(self, others, merge_conditions, common_ancestor=None):

        for other in others:
            for k in other.keys():
                if k not in self:
                    self[k] = other[k]

        return True

    def widen(self, others):
        l.warning("Widening is unimplemented for globals")
        return False

    def __getitem__(self, k):
        return self._backer[k]

    def __setitem__(self, k, v):
        self._backer[k] = v

    def __delitem__(self, k):
        del self._backer[k]

    def __contains__(self, k):
        return k in self._backer

    def keys(self):
        return self._backer.keys()

    def values(self):
        return self._backer.values()

    def items(self):
        return self._backer.items()

    def get(self, k, alt=None):
        return self._backer.get(k, alt)

    def copy(self):
        return SimStateGlobals(dict(self._backer))

SimStatePlugin.register_default('globals', SimStateGlobals)
