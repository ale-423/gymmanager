from django.contrib import admin

from .models import (
    User, Equipment, Maintenance, AvailabilityDay,
    Course, Enrollment, Teaching, Payment, Feedback,
    ProgressReport, Subscription, Membership, Promotion,
    TrainingSchedule, TrainingDay, Exercise, ExerciseDetail
)

# Registrazione base
admin.site.register(User)
admin.site.register(Equipment)
admin.site.register(Maintenance)
admin.site.register(AvailabilityDay)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Teaching)
admin.site.register(Payment)
admin.site.register(Feedback)
admin.site.register(ProgressReport)
admin.site.register(Subscription)
admin.site.register(Membership)
admin.site.register(Promotion)
admin.site.register(TrainingSchedule)
admin.site.register(TrainingDay)
admin.site.register(Exercise)
admin.site.register(ExerciseDetail)