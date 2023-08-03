from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from .models import test, Question, Category

# Create your views here.
def home(request):
    category = Category.objects.all()
    test_set = test.objects.all() 

    context = {
        'category': category,
        'test': test_set
        }
    return render(request, 'tests.html',context)


def givetest(request, category_id):
    category = get_object_or_404(test, id=category_id)
    allquestions = Question.objects.filter(category=category)
    total_questions = allquestions.count()

        # Add question_number field to each question
    for idx, question in enumerate(allquestions, start=1):
        question.question_number = idx
    if request.method == 'POST':
        
        score = 0
        corrected_answer = 0
        incorrect_answer = 0
        not_answered= 0
        ques_no = 0

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
            'ques_no': ques_no,
        })

    return render(request, 'give_test.html', {'category': category, 'allquestions': allquestions ,'total_questions': total_questions} )

def add_question(request):
    if request.method == 'POST':
            # If the "Add another question" button is clicked, save the current question data
            category_id = request.POST.get('category')
            category = test.objects.get(pk=category_id)
            question = request.POST.get('question')
            option1 = request.POST.get('option1')
            option2 = request.POST.get('option2')
            option3 = request.POST.get('option3')
            option4 = request.POST.get('option4')
            correct_answer = request.POST.get('correct_answer')

            question_obj = Question(category=category, question=question, option1=option1, option2=option2, option3=option3, option4=option4, correct_answer=correct_answer)
            print(question_obj)
            question_obj.save()

            # Redirect back to the same page to add another question
            return redirect('add_question')

    else:
        categories = test.objects.all()
        return render(request, 'add_question.html', {'categories': categories})

def test_category_filter(request):
    if request.method == 'POST':
        selected_category_id = request.POST.get('selected_category')
        all_category = Category.objects.all()
        if selected_category_id:
            selected_tests = test.objects.filter(category=selected_category_id)
            # Redirect to the 'givetest' view with the selected category ID
            context = {'selected_tests': selected_tests
                       ,'all_category': all_category}
            print(str(selected_category_id))
            print(str(selected_tests))
            return render(request , 'test_category_filter.html', context)
        else:
            # If no category is selected, redirect back to the same page
            return redirect('/')

    else:
        # If it's a GET request, fetch all categories from the database
        test_set = test.objects.all()
        categories = Category.objects.all()
        
        # Fetch all tests if no category is selected or filter the tests by the selected category
        
        return render(request, 'test_category_filter.html', {'categories': categories, 'test_set': test_set})