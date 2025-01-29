from django.shortcuts import render
from datetime import date

# Create your views here.

all_posts = [
    {
        'slug': 'learning-django',
        'title': 'django course',
        'author': 'Mohammad Ordokhani',
        'image': 'django.png',
        'date': date(2021, 4, 5),
        'short_description': "This is django course from zero to hero :)",
        'content': """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium eius fugit ipsam iure quibusdam.
            Dolorum fuga incidunt, nobis perspiciatis sequi velit vitae! Asperiores, deleniti dicta dolorem et ex harum
            inventore itaque magnam nemo nihil, nostrum placeat provident, quis reprehenderit soluta veniam veritatis?
            Ab, adipisci culpa cumque deleniti doloremque facilis magnam nihil odit omnis quam quia quis quos saepe
            suscipit voluptate
        """
    },
    {
        'slug': 'learning-python',
        'title': 'python course',
        'author': 'Mohammad Ordokhani',
        'image': 'python.png',
        'date': date(2021, 4, 3),
        'short_description': "This is python course from zero to hero :)",
        'content': """
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium eius fugit ipsam iure quibusdam.
        Dolorum fuga incidunt, nobis perspiciatis sequi velit vitae! Asperiores, deleniti dicta dolorem et ex harum
        inventore itaque magnam nemo nihil, nostrum placeat provident, quis reprehenderit soluta veniam veritatis?
        Ab, adipisci culpa cumque deleniti doloremque facilis magnam nihil odit omnis quam quia quis quos saepe
        suscipit voluptate
    """
    },
    {
        'slug': 'machine-learning',
        'title': 'ml course',
        'author': 'Mohammad Ordokhani',
        'image': 'ml.png',
        'date': date(2021, 3, 1),
        'short_description': "This is ml course from zero to hero :)",
        'content': """
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium eius fugit ipsam iure quibusdam.
        Dolorum fuga incidunt, nobis perspiciatis sequi velit vitae! Asperiores, deleniti dicta dolorem et ex harum
        inventore itaque magnam nemo nihil, nostrum placeat provident, quis reprehenderit soluta veniam veritatis?
        Ab, adipisci culpa cumque deleniti doloremque facilis magnam nihil odit omnis quam quia quis quos saepe
        suscipit voluptate
    """
    }
]


def get_date(post):
    return post['date']


def index_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_post = sorted_posts[-2:]
    return render(request, 'blog/Home.html', {
        'latest_post': latest_post
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })


def single_post(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': post
    })
