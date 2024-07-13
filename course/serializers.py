from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from course.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):

     class Meta:
         model = Course
         fields = '__all__'

class CourseDetailSerializer(serializers.ModelSerializer):
     count_lessons_in_course = SerializerMethodField()

     def get_course_lessons(self, course):
         all_lessons = Lesson.objects.filter(course=course.id)
         return [(lesson.title, lesson.lesson_description, lesson.link) for lesson in
                 all_lessons]

     def get_count_lessons_in_course(self, course):
         return Course.objects.filter(lesson=course.lesson).count()

     class Meta:
         model = Course
         fields = ("name", "description", "count_lessons_in_course",)

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'