from django.db import models


class CharacterRoles(models.TextChoices):
    PROTAGONIST = 'PROTAGONIST', 'Protagonist'
    DEUTERAGONIST = 'DEUTERAGONIST', 'Deuteragonist'
    ANTAGONIST = 'ANTAGONIST', 'Antagonist'
    SUPPORTING = 'SUPPORTING', 'Supporting Character'
    NPC = 'NPC', 'Non-Playable Character'
    
    
class LoreType(models.TextChoices):
    MAIN_STORY = 'MAIN_STORY', 'Main Story'
    SIDE_QUEST = 'SIDE_QUEST', 'Side Quest'
    DLC = 'DLC', 'Downloadable Content'


class TimelineEventType(models.TextChoices):
    BATTLE = 'BATTLE'