import logging

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')

logger = logging.getLogger("nj-transit")
logger.setLevel(logging.DEBUG)

def greet_handler():
    logger.info("GREET ACTION CREATED")
    return True
    

def identify_handler():
    logger.info("IDENTIFY ACTION CREATED")
    return True

def close_handler():
    logger.info("CLOSE ACTION CREATED")
    return True



class ActionHandler:

    mapping = {'greet': greet_handler,
              'identify': identify_handler,
              'close': close_handler}

    def execute(self, action):
        handler = self.mapping[action]
        return handler()


def root(event_data, context):
    logging.info("Process started")
    logging.info("event received: ", event_data)

    action = event_data["action"]

    ActionHandler().execute(action)


if __name__ == "__main__":
    event = {'action': 'greet'}
    logging.info("event sent: %s", event)
    root(event_data=event, context =  None)
