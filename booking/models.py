from django.db import models

# Create your models here.

class Library(models.Model):
    library_id = models.CharField(primary_key=True, max_length=4)
    library_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'library'
        
    def __str__(self):
        return self.library_id
    
        
class Level(models.Model):
    level_id = models.CharField(primary_key=True, max_length=6)
    library = models.ForeignKey('Library', models.DO_NOTHING, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'level'
        
    def __str__(self):
        return self.level_id


class Seat(models.Model):
    seat_id = models.CharField(primary_key=True, max_length=8)
    library = models.ForeignKey(Library, models.DO_NOTHING, blank=True, null=True)
    level = models.ForeignKey(Level, models.DO_NOTHING, blank=True, null=True)
    row = models.CharField(max_length=1, blank=True, null=True)
    col = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seat'
        
    def __str__(self):
        return self.seat_id



class Occupied(models.Model):
    occupied_id = models.AutoField(primary_key=True)
    matric_no = models.CharField(max_length=9, blank=True, null=True)
    library = models.ForeignKey(Library, models.DO_NOTHING, blank=True, null=True)
    level = models.ForeignKey(Level, models.DO_NOTHING, blank=True, null=True)
    seat = models.ForeignKey('Seat', models.DO_NOTHING, blank=True, null=True)
    book_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occupied'
        
    def __str__(self):
        return str(self.occupied_id)


