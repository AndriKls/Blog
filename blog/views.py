from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

# Create your views here.


all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Andri",
        "date": date(2021, 7, 21),
        "title": "Matkamine mägedes",
        "exerpt": "Pole midagi võrreldavat nende vaadetega, mida mägedes matkates koged! Ja ma polnud kaugeltki valmis selleks, mis juhtus, kui ma vaadet nautisin!",
        "content": """

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quis, minus? Dolor
        numquam sunt tempore modi animi nam libero et neque quo, ut, rerum rem fugit
        explicabo quisquam asperiores. Beatae, eos?

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quis, minus? Dolor
        numquam sunt tempore modi animi nam libero et neque quo, ut, rerum rem fugit
        explicabo quisquam asperiores. Beatae, eos?

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quis, minus? Dolor
        numquam sunt tempore modi animi nam libero et neque quo, ut, rerum rem fugit
        explicabo quisquam asperiores. Beatae, eos?
        """
    },
    {
    "slug": "programmeerimine-on-lahe",
    "image": "coding.jpg",
    "author": "Andri",
    "date": date(2022, 3, 10),
    "title": "Programmeerimine on suurepärane!",
    "exerpt": "Oled kunagi veetnud tunde otsides seda ühte viga oma koodis? Jep - just see juhtus minuga eile...",
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    """
},
{
    "slug": "metsadesse-minek",
    "image": "woods.jpg",
    "author": "Andri",
    "date": date(2020, 8, 5),
    "title": "Looduse parimad hetked",
    "exerpt": "Loodus on imeline! Inspireeriv, kui palju saan ideid looduses kõndides!",
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    """
},
]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html",{
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })