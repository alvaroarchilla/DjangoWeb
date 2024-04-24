
from blog.models import Post
from django.db import connection
from pprint import pprint

def run():
    posts= Post.objects.all()
    print(posts)
    