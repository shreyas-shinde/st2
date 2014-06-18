import datetime

from st2common import log as logging
import st2reactor.container.utils as container_utils
import st2reactor.ruleenforcement.enforce as rules_engine

LOG = logging.getLogger('st2reactor.sensor.dispatcher')


class TriggerDispatcher(object):

    def __init__(self):
        pass

    def dispatch(self, triggers):
        """
        """
        trigger_instances = [container_utils.create_trigger_instance(
            trigger['name'],
            trigger['payload'] if 'payload' in trigger else {},
            trigger['occurrence_time'] if 'occurrence_time' in trigger else
            datetime.datetime.now())
            for trigger in triggers]
        rules_engine.handle_trigger_instances(trigger_instances)
