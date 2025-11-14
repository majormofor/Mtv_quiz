from django.shortcuts import render
from .models import UserInfo, Question
from django.utils import timezone

def quiz_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        # prevent duplicate phone numbers
        if UserInfo.objects.filter(phone_number=phone).exists():
            questions = Question.objects.all()[:10]
            return render(request, 'quiz/quiz.html', {
                'error': 'Phone number already used. Try another number.',
                'questions': questions,
                'name': name,
                'phone': phone
            })

        # collect answers and calculate score
        questions = Question.objects.all()[:10]
        score = 0
        for q in questions:
            selected = request.POST.get(str(q.id))  # each input name = question id
            if selected and selected.upper() == q.correct_answer.upper():
                score += 10

        # save user info with submission time
        UserInfo.objects.create(
            name=name,
            phone_number=phone,
            score=score,
            submitted_at=timezone.now()
        )

        # leaderboard: sort by score DESC, then submission time ASC
        leaderboard = UserInfo.objects.order_by('-score', 'submitted_at')[:10]

        return render(request, 'quiz/result.html', {
            'name': name,
            'score': score,
            'leaderboard': leaderboard
        })

    else:
        # first load, show form
        questions = Question.objects.all()[:10]
        return render(request, 'quiz/quiz.html', {'questions': questions})
