from django.shortcuts import render
from data_processing.models import DataEntry
from django.db.models import Count


def data_list(request):
    # Get all entries ordered by timestamp (most recent first)
    entries = DataEntry.objects.all().order_by('-timestamp')

    # Calculate grade counts
    grade_counts = {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0
    }

    grade_distribution = DataEntry.objects.values('grade').annotate(count=Count('grade'))
    for grade in grade_distribution:
        grade_counts[grade['grade']] = grade['count']

    context = {
        'entries': entries,
        'total_count': entries.count(),
        'grade_counts': grade_counts,
    }

    return render(request, 'data_processing/data_list.html', context)