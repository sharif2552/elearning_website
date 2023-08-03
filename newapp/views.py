from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from .models import Category, Question

# Create your views here.
def home(request):
    category = Category.objects.all()
    return render(request, 'tests.html', {'category': category})


def givetest(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    allquestions = Question.objects.filter(category=category)
    total_questions = allquestions.count()
    if request.method == 'POST':
        
        score = 0
        corrected_answer = 0
        incorrect_answer = 0
        not_answered= 0

        for question in allquestions:
            submitted_answer = request.POST.get(f'q{question.id}')
            correct_answer = question.correct_answer

            if submitted_answer == correct_answer:
                score += 1
                corrected_answer+=1
            elif submitted_answer is None:
                not_answered+=1
            
            else:
                incorrect_answer += 1

        # Calculate the percentage score
        percentage_score = (score / total_questions) * 100

        # You can pass the score or percentage_score to the template as needed
        # For example:
        return render(request, 'results.html', {
            'category': category,
            'total_questions': total_questions,
            'score': score,
            'percentage_score': percentage_score,
            'correct_answers': corrected_answer,
            'incorrect_answers': incorrect_answer,
            'not_answered' : not_answered,
        })

    return render(request, 'give_test.html', {'category': category, 'allquestions': allquestions ,'total_questions': total_questions} )

def add_question(request):
    if request.method == 'POST':
        if 'another_question' in request.POST:
            # If the "Add another question" button is clicked, save the current question data
            category_id = request.POST.get('category')
            category = Category.objects.get(pk=category_id)
            question = request.POST.get('question')
            option1 = request.POST.get('option1')
            option2 = request.POST.get('option2')
            option3 = request.POST.get('option3')
            option4 = request.POST.get('option4')
            correct_answer = request.POST.get('correct_answer')

            question_obj = Question(category=category, question=question, option1=option1, option2=option2, option3=option3, option4=option4, correct_answer=correct_answer)
            question_obj.save()

            # Redirect back to the same page to add another question
            return redirect('add_question')

        else:
            # If the "Submit" button is clicked, save the current question data and redirect to the success page
            # You can put the same logic for saving the question as above
            
            return redirect('/')  # Replace 'success_page' with the URL name of your success page or the URL path

    else:
        categories = Category.objects.all()
        return render(request, 'add_question.html', {'categories': categories})
