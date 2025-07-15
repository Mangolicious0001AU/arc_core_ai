# ROUTES IDENTITY CONTEXT
from personality_core import personality_profile
from user_memory_index import user_profile
from values_ethics_manifesto import values_manifesto
from growth_diary import growth_diary
from project_lore_registry import project_registry

def route_context(user_input, project=None):
    return {
        'tone': 'raw, documentary',
        'mode': 'advocate',
        'emotional_resonance': ['righteous anger', 'hope']
    }