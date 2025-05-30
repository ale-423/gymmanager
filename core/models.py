from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    userName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    birthDate = models.DateField()
    gender = models.CharField(max_length=10)
    phoneNumber = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    specialization = models.CharField(max_length=100, blank=True, null=True)


class Maintenance(models.Model):
    maintenanceDate = models.DateField()
    maintenanceCost = models.DecimalField(max_digits=8, decimal_places=2)


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    state = models.CharField(max_length=50)
    administrator = models.ForeignKey(User, on_delete=models.CASCADE)


class Servicing(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE)


class AvailabilityDay(models.Model):
    dayOfWeek = models.IntegerField()  # 0 = Monday, 6 = Sunday
    startTime = models.TimeField()
    finishTime = models.TimeField()


class Availability(models.Model):
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    availabilityDay = models.ForeignKey(AvailabilityDay, on_delete=models.CASCADE)


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    maxParticipants = models.IntegerField()
    startDate = models.DateField()
    finishDate = models.DateField()


class Teaching(models.Model):
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


class TrainingSchedule(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    creationDate = models.DateField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_schedules')
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trainer_schedules')


class TrainingDay(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    trainingSchedule = models.ForeignKey(TrainingSchedule, on_delete=models.CASCADE)


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class ExerciseDetail(models.Model):
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.FloatField()
    restTime = models.DurationField()
    trainingDay = models.ForeignKey(TrainingDay, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)


class Membership(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in days")


class Promotion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    discountRate = models.FloatField()
    startDate = models.DateField()
    expirationDate = models.DateField()


class Subscription(models.Model):
    startDate = models.DateField()
    expirationDate = models.DateField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.SET_NULL, blank=True, null=True)


class ProgressReport(models.Model):
    date = models.DateField()
    description = models.TextField()
    weight = models.FloatField()
    bodyFatPercent = models.FloatField()
    muscleMass = models.FloatField()
    bmi = models.FloatField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


class Feedback(models.Model):
    date = models.DateField()
    rating = models.IntegerField()
    comment = models.TextField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


class Payment(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    type = models.CharField(max_length=50)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)