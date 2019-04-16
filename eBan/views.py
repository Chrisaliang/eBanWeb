from django.shortcuts import render
from django.http import HttpResponse
from .models import Board


# Create your views here.


def home(request):
    boards = Board.objects.all()
    # boards_name = list()

    # for board in boards:
    #     boards_name.append(board.name)

    # response_html = '<br>'.join(boards_name)
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})
