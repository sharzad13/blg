from django.shortcuts import render

def post_list(requests):
    return render (requests,'blog/post_list.html',{})