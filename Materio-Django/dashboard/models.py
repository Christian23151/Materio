from django.db import models

class CourseTable(models.Model):
    Course = models.CharField(max_length=45, primary_key=True)
    College = models.CharField(max_length=45)

    def __str__(self):
        return self.Course

class StudentTable(models.Model):
    StudentID = models.CharField(max_length=45, primary_key=True)
    Student_Name = models.CharField(max_length=45)
    Course = models.ForeignKey(CourseTable, on_delete=models.CASCADE, db_column='Course')

    def __str__(self):
        return self.Student_Name

class SubjectTable(models.Model):
    SubjCode = models.CharField(max_length=45, primary_key=True)
    SubjDescription = models.CharField(max_length=45)
    Units = models.IntegerField()

    def __str__(self):
        return self.SubjDescription

class EnrollTable(models.Model):
    StudentID = models.ForeignKey(StudentTable, on_delete=models.CASCADE, db_column='StudentID')
    SubjCode = models.ForeignKey(SubjectTable, on_delete=models.CASCADE, db_column='SubjCode')

    class Meta:
        unique_together = (('StudentID', 'SubjCode'),)

class ContactTable(models.Model):
    Contactid = models.CharField(max_length=45, primary_key=True)
    StudentID = models.ForeignKey(StudentTable, on_delete=models.CASCADE, db_column='StudentID')
    ContactNumber = models.CharField(max_length=45)
