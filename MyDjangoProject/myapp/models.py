"""
Module: Traffic Volume Data Model
Author: Lei Luo
Description: Defines the data model for storing traffic volume information in the database.
"""

from django.db import models


class TrafficVolume(models.Model):
    """
    A Django model representing a traffic volume record.

    Attributes:
        section_id (int): Unique identifier for a section of the road.
        highway (int): Identifier for the highway on which the section is located.
        section (int): Numeric identifier of the road section.
        section_length (float): Length of the road section in kilometers.
        section_description (str): Description of the road section.
        date (str): Date of the data entry.
        description (str): Additional details about the traffic volume data.
        group (str): Group classification for the section.
        type (str): Type of road or traffic.
        county (str): County in which the section is located.
        ptrucks (str): Percentage of trucks in the traffic mix.
        adt (int): Average Daily Traffic count.
        aadt (int): Adjusted Annual Average Daily Traffic count.
        direction (str): Traffic direction.
        pct85 (str): 85th percentile speed.
        priority_points (str): Points assigned based on traffic priority considerations.
    """

    section_id = models.IntegerField(db_column='SECTION_ID', primary_key=True)
    highway = models.IntegerField(db_column='HIGHWAY', default=0)
    section = models.IntegerField(db_column='SECTION', default=0)
    section_length = models.FloatField(db_column='SECTION_LENGTH', default=0.0)
    section_description = models.TextField(
        db_column='SECTION_DESCRIPTION', default='')
    date = models.TextField(db_column='Date')
    description = models.TextField(db_column='DESCRIPTION', default='')
    group = models.TextField(db_column='GROUP', default='')
    type = models.TextField(db_column='TYPE', default='')
    county = models.TextField(db_column='COUNTY', default='')
    ptrucks = models.TextField(db_column='PTRUCKS', default='')
    adt = models.IntegerField(db_column='ADT', default=0)
    aadt = models.IntegerField(db_column='AADT', default=0)
    direction = models.TextField(db_column='DIRECTION', default='')
    pct85 = models.TextField(db_column='85PCT', default='')
    priority_points = models.TextField(db_column='PRIORITY_POINTS', default='')

    class Meta:
        db_table = 'traffic_volumes'
        verbose_name_plural = "Traffic Volumes"
