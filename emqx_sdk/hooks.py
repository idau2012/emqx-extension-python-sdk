from .states import EMQX_OK
from .types import (
    EMQX_TOPICS, EMQX_CLIENTINFO_T, EMQX_PROPS_T,
    EMQX_OPTS_T, EMQX_MESSAGE_T
)


EMQX_HOOK_DICT = {
    'on_client_connect': 'client_connect',
    'on_client_connack': 'client_connack',
    'on_client_connected': 'client_connected',
    'on_client_disconnected': 'client_disconnected',
    'on_client_authenticate': 'client_authenticate',
    'on_client_check_acl': 'client_check_acl',
    'on_client_subscribe': 'client_subscribe',
    'on_client_unsubscribe': 'client_unsubscribe',
    'on_session_created': 'session_created',
    'on_session_subscribed': 'session_subscribed',
    'on_session_unsubscribed': 'session_unsubscribed',
    'on_session_resumed': 'session_resumed',
    'on_session_discarded': 'session_discarded',
    'on_session_takeovered': 'session_takeovered',
    'on_session_terminated': 'session_terminated',
    'on_message_publish': 'message_publish',
    'on_message_delivered': 'message_delivered',
    'on_message_acked': 'message_acked',
    'on_message_dropped': 'message_dropped'
}


class EmqxHookSdk:
    def __init__(self, hook_module: str):
        self.hook_module = hook_module

    def on_start(self, topics: EMQX_TOPICS = None):
        hooks_spec = []
        topics = topics if topics else []
        hook_filename, hook_instance = self.hook_module.split('.')
        for key, value in self.__class__.__dict__.items():
            if not EMQX_HOOK_DICT.get(key):
                continue
            # todo @gw topics?
            action = EMQX_HOOK_DICT[key]
            action_func = f'{hook_instance}.{key}'
            hook_spec = (action, hook_filename, action_func, topics)
            hooks_spec.append(hook_spec)
        return EMQX_OK, (hooks_spec, ())

    # Clients
    def on_client_connect(self,
                          conninfo: EMQX_CLIENTINFO_T = None,
                          props: dict = None,
                          state: tuple = None):
        ...

    def on_client_connack(self,
                          conninfo: EMQX_CLIENTINFO_T,
                          props: dict,
                          state: tuple):
        ...

    def on_client_connected(self, clientinfo: EMQX_CLIENTINFO_T, state: tuple):
        ...

    def on_client_disconnected(self,
                               clientinfo: EMQX_CLIENTINFO_T,
                               reason: str,
                               state: tuple):
        ...

    @staticmethod
    def on_client_authenticate(clientinfo: EMQX_CLIENTINFO_T,
                               authresult: bool,
                               state: tuple) -> bool:
        ...

    def on_client_check_acl(self,
                            clientinfo: EMQX_CLIENTINFO_T,
                            pubsub: str,
                            topic: str,
                            result: bool,
                            state: tuple) -> bool:
        ...

    def on_client_subscribe(self,
                            clientinfo: EMQX_CLIENTINFO_T,
                            props: EMQX_PROPS_T,
                            topics: set,
                            state: tuple):
        ...

    def on_client_unsubscribe(self,
                              clientinfo: EMQX_CLIENTINFO_T,
                              props: EMQX_PROPS_T,
                              topics: set,
                              state: tuple):
        ...

    # Sessions
    def on_session_created(self, clientinfo: EMQX_CLIENTINFO_T, state: tuple):
        ...

    def on_session_subscribed(self,
                              clientinfo: EMQX_CLIENTINFO_T,
                              topic: str,
                              opts: EMQX_OPTS_T,
                              state: tuple):
        ...

    def on_session_unsubscribed(self,
                                clientinfo: EMQX_CLIENTINFO_T,
                                topic: str,
                                state: tuple):
        ...

    def on_session_resumed(self, clientinfo: EMQX_CLIENTINFO_T, state: tuple):
        ...

    def on_session_discarded(self, clientinfo: EMQX_CLIENTINFO_T, state: tuple):
        ...

    def on_session_takeovered(self, clientinfo: EMQX_CLIENTINFO_T, state: tuple):
        ...

    def on_session_terminated(self,
                              clientinfo: EMQX_CLIENTINFO_T,
                              reason: str,
                              state: tuple):
        ...

    # Messages
    def on_message_publish(self, message: EMQX_MESSAGE_T, state: tuple):
        ...

    def on_message_delivered(self,
                             clientinfo: EMQX_CLIENTINFO_T,
                             message: EMQX_MESSAGE_T,
                             state: tuple):
        ...

    def on_message_acked(self,
                         clientinfo: EMQX_CLIENTINFO_T,
                         message: EMQX_MESSAGE_T,
                         state: tuple):
        ...

    def on_message_dropped(self,
                           message: EMQX_MESSAGE_T,
                           reason: str,
                           state: tuple):
        ...

    def parse(self):
        ...
