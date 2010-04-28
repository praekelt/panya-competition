Django Competition:
===================
**Django competition app.**


Dependancies:
=============
django-content
    git@github.com:praekelt/django-content.git


Models:
=======

Competition:
------------
class models.Competition
    
Competition model extends content.models.ModelBase. Add a competition to the CMS with start and end dates, question and correct answer.
Linked via foreign key to entries to the competion object.

API Reference:
~~~~~~~~~~~~~~

FIELDS
******
start_date
    Date field to specify the date the competition should start being displayed.
end_date
    Date field to specify the date the competition should stop being displayed.
question
    Char field for a short question specific to the competition which should be answered correctly to qualify as a winner.
question_blurb
    Richtext field for elelaborating on the short question field.
correct_answer
    Char field specifing the correct answer to the competition question.
rules
    Richtext field with rules specific to the competition.
extends django-content fields
    See django-content README

METHODS
*******
is_active::
    Competition.is_active()
Returns whether the competition should be displayed. Determined by by the start and end dates.

MANAGERS
********
None

CompetitionOption:
------------------
class models.CompetitionOption
    
Competition question answer options. List of possible answers to the question posed by the competition object.
Linked to a competition via foreign key.

API Reference:
~~~~~~~~~~~~~~

FIELDS
******
competition
    Foreign key to the competition object.
title
    The title/answer option to the competition question
extends django-content fields
    See django-content README

METHODS
*******
None

MANAGERS
********
None

CompetitionEntry:
-----------------
class models.CompetitionEntry
    
Competition entries, requires that the user is authenticated to enter. Linked via foreign key to a specific competition.

API Reference:
~~~~~~~~~~~~~~

FIELDS
******
competition
    Foreign key to the competition object.
user
    Foreign key to the currently authenticated user.
answer
    Char field with the competition entrants answer.
winner
    Boolena field specifing if this is a winning competition entry
timestamp
    Datetime field with the date and time the entry was completed
extends django-content fields
    See django-content README

METHODS
*******
correct_answer::
    CompetitionEntry.correct_answer()
Method to filter entries that have given the correct answer to the competition.

MANAGERS
********
None


Tag Reference
=============

Inclusion Tags
--------------
None

Template Tags
-------------
None
