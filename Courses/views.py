from datetime import datetime
from django.shortcuts import render, redirect
from .models import Course, Question, Award

# Gets All Courses and displays them to the user, or filters the courses by the user's search, which then displays the filtered courses
def view_courses(request):
    if not request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        search = request.POST["search"]
        filtered_courses = Course.objects.filter(title__icontains=search)
        return render(request, "courses/view_courses.html", {"courses": filtered_courses, "search_message": f"{filtered_courses.count()} results found for {search}"})
    else:
        all_courses = Course.objects.all().order_by("title")
        return render(request, "courses/view_courses.html", {"courses": all_courses, "search_message": f"{all_courses.count()} results"})


# Gets the selected course and inputs it into the webpage, which is the overview of the course
def course_overview(request, id):
    if not request.user.is_authenticated:
        return redirect("index")

    course = Course.objects.all().get(course_id=id)
    return render(request, "courses/overview_course.html", {"course": course})


# Gets the selected course and inputs it into the webpage, which is the content of the course
def course_content(request, id):
    if not request.user.is_authenticated:
        return redirect("index")

    course = Course.objects.all().get(course_id=id)
    return render(request, "courses/content_course.html", {"course": course})


# Gets the selected course, and all questions related to the course, and the user has to answer the questions
def course_questions(request, id):
    if not request.user.is_authenticated:
        return redirect("index")

    course = Course.objects.all().get(course_id=id)
    all_questions = Question.objects.all().filter(course_id=id)
    if request.method == "POST":
        total_marks = 0
        user_marks = 0
        for question in all_questions:
            total_marks += 1
            try:
                if question.answer == request.POST[question.question]:
                    user_marks += 1
            except:
                continue
        user_award = calculate_award(request, course, user_marks, total_marks)
        return render(request,"courses/end_course.html", {"award": user_award})
    else:
        return render(request, "courses/assessment_course.html", {"course": course, "questions": all_questions})


# After the questions have been answered, the award is calculated and saved to the database
def calculate_award(request, course, user_marks, total_marks):
    percentage = user_marks / total_marks * 100
    
    if 90 <= percentage <= 100:
        trophy = "gold"
    elif 70 <= percentage < 90:
        trophy = "silver"
    elif 50 <= percentage < 70:
        trophy = "bronze"
    else:
        trophy = "none"
    award = Award.objects.create(
        course_id = course,
        user_id = request.user,
        trophy = trophy,
        user_marks = user_marks,
        total_marks = total_marks,
        percentage = percentage,
        completion_date = datetime.now(),
    )
    return award