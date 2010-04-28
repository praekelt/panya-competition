from datetime import date, datetime, timedelta
import unittest

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from competition.models import Competition, CompetitionEntry

class ModelTestCase(unittest.TestCase):
    def test_model_methods(self):
        # create competition obj
        competition_obj = Competition(
            title='title',
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=1),
            correct_answer='answer'
        )
        competition_obj.save()
        
        # create a user obj
        user_obj = User(
            username='user',
            email='user@abcde.com'
        )
        user_obj.save()
        
        # create a competition entry obj
        competition_entry_obj = CompetitionEntry(
            competition=competition_obj,
            user=user_obj,
            answer='wrong answer'
        )
        competition_entry_obj.save()
        
        # test that the competition is displayed if the current date is within range
        self.failUnless(competition_obj.is_active())
        
        # test that the competition is inactive if the end date is less than the start date
        competition_obj.end_date = datetime.now() - timedelta(days=1)
        competition_obj.save()
        self.failIf(competition_obj.is_active())
        
        # test that the competition is inactive if the start date is greater than the current date 
        competition_obj.start_date = datetime.now() + timedelta(days=1)
        competition_obj.save()
        self.failIf(competition_obj.is_active())
        
        # test that the competition is inactive if the end date is less than the current date
        competition_obj.end_date = datetime.now() - timedelta(days=1)
        competition_obj.save()
        self.failIf(competition_obj.is_active())
        
        # test that the competition entry has answered the question correctly
        self.failIf(competition_entry_obj.correct_answer())
        