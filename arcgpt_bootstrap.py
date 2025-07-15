# BOOTSTRAP FILE
from context_router import route_context
from response_composer import compose_response
from emotional_engine import emotion_chip_switch

# Demo Entry
if __name__ == '__main__':
    user_input = input('You: ')
    trigger = input('Command: ')
    result = emotion_chip_switch(trigger, user_input, project='wormlock')
    print('\nARC_CORE_Ai:', result['reply'])