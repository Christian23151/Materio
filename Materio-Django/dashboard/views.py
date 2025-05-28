from django.shortcuts import render
from .models import StudentTable, CourseTable, SubjectTable, EnrollTable, ContactTable
from django.db.models import Count, Sum

def dashboard_stats(request):
    total_students = StudentTable.objects.count()
    total_courses = CourseTable.objects.count()
    total_subjects = SubjectTable.objects.count()
    most_enrolled_subject = EnrollTable.objects.values('SubjCode').annotate(total=Count('SubjCode')).order_by('-total').first()
    total_units_per_student = EnrollTable.objects.values('StudentID').annotate(total_units=Sum('SubjCode__Units'))

    return render(request, 'dashboard/stats.html', {
        'total_students': total_students,
        'total_courses': total_courses,
        'total_subjects': total_subjects,
        'most_enrolled_subject': most_enrolled_subject,
        'total_units_per_student': total_units_per_student,
    })
