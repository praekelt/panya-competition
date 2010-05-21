import random
from datetime import date, timedelta

from django.conf import settings

from generate import IMAGES
from generate.json_loader import load_json

COMPETITION_COUNT = 10

def generate():
    objects = []
    
    # create event, venue and location objects
    for i in range(1, COMPETITION_COUNT + 1):
        start_date = date.today() + timedelta(days=random.randint(1, 30))
        end_date = start_date + timedelta(days=random.randint(1, 60))
        objects.append({
            "model": "competition.Competition",
            "fields": {
                "title": "Competition %s Title" % i,
                "description": "Competition %s description with some added text to verify truncates where needed." % i,
                "content": "Competition %s Content" % i,
                "state": "published",
                "image": random.sample(IMAGES, 1)[0],
                "start_date": str(start_date),
                "end_date": str(end_date),
                "question": "Competition %s question?" % i,
                "question_blurb": "Competition %s question blurb." % i,
                "correct_answer": "Competition %s answer." % i,
                "rules": "Competition %s rules." % i,
                "sites": {
                    "model": "sites.Site",
                    "fields": { 
                        "name": "example.com",
                    }
                },
            },
        })
    
    load_json(objects)
