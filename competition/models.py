from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from content.models import ModelBase

class Competition(ModelBase):
    content = RichTextField()
    start_date = models.DateField(
        blank=True, 
        null=True, 
        help_text='Date the competition starts.'
    )
    end_date = models.DateField(
        blank=True, 
        null=True, 
        help_text='Date the competition ends.'
    )
    question = models.CharField(
        blank=True, 
        null=True, 
        max_length=255,
        help_text='Short competition question',
    )
    '''
    question_blurb = RichTextField(
        blank=True, 
        null=True, 
        help_text='Descriptive text elaborating on the question.'
    )
    '''
    correct_answer = models.CharField(
        max_length=255,
        blank=True, 
        null=True, 
        help_text='Answer used to determine winning entries.'
    )
    '''
    rules = RichTextField(
        blank=True, 
        null=True, 
        help_text='Rules specific to this competition.',
    )
    '''
    
    def is_active(self):
        '''
        Assert that the listing in active according to start/end dates.
        '''
        now = datetime.now()
        active = True
        
        if self.start_date and self.end_date:
            active = self.end_date >= self.start_date
        if self.start_date and active:
            actice = self.start_date <= now
        if self.end_date and active:
            active = self.end_date >= now
            
        return active
    
    def __unicode__(self):
        return self.title
    
class CompetitionEntry(models.Model):
    competition = models.ForeignKey(
        Competition,
        related_name='competition_entries'
    )
    user = models.ForeignKey(
        User,
        related_name='competition_entries_users'
    )
    answer = models.CharField(max_length=255)
    winner = models.BooleanField(
        help_text='Mark this competition entry as a winning entry.'
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Competition Entry'
        verbose_name_plural = 'Competition Entries'
        
    def correct_answer(self):
        if self.answer and self.competition.correct_answer:
            return self.answer.lower() == self.competition.correct_answer.lower()
        return False

    def __unicode__(self):
        return "%s answered %s" % (self.user.username, self.answer)
