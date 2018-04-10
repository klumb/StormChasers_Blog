from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import top_post, response_post, Profile
from .models import tags as modelsTag
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
# from .forms import ImageForm, PostForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import top_post, response_post, image
from .models import image as dbimage
from .forms import PostForm, ImageForm, TagForm
from random import randrange
from django.contrib import messages
from .forms import *
import json
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator1
import requests as Requests
import json as Json

@login_required
def new_top_post(request):
    ImageFormSet = modelformset_factory(dbimage,
                                        form=ImageForm, extra=10)

    if request.method == 'POST':
        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=dbimage.objects.none())
        tagsForm = TagForm(request.POST)
        if postForm.is_valid() and formset.is_valid():
            title = request.POST['title']
            text = request.POST['text']
            tags = request.POST['tag']
            tags = tags.split(',')
            newTopPost = top_post(title=title,
                                  text=text,
                                  created_date=timezone.now(),
                                  published_date=timezone.now(),
                                  user_id=request.user, )
            newTopPost.author = request.user.username
            newTopPost.save()
            # Get object to save with images
            topPostInstance = get_object_or_404(top_post, post_id=newTopPost.post_id)
            for form in formset.cleaned_data:
                try:
                    image = form['image']
                    photo = dbimage(image=image, top_post_id=topPostInstance)
                    photo.save()
                except KeyError:
                    pass

            for tag in tags:
                tag = tag.strip()
                newTag = modelsTag(tag=tag, top_post_id=topPostInstance)
                newTag.save()

            return HttpResponseRedirect(reverse('blog'))
        else:
            print(tagsForm.errors)
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=dbimage.objects.none())
        tagForm = TagForm()
    return render(request, 'blog/new_post.html',
                  {'postForm': postForm, 'formset': formset, 'tagForm': TagForm})

@login_required
def getForecast(request):

    lat = request.GET['lat']
    lon = request.GET['lon']
    zip = request.GET['zip']

    success = False
    json = {}

    if lat == '' and lon == '' and zip == '':
        pass
    elif lat != '' and lon != '':
        #forecast = http://api.openweathermap.org/data/2.5/forecast?zip=68114&APPID=431a44405aef953371bcbe245588e0c7
        r = Requests.get('http://api.openweathermap.org/data/2.5/forecast?lat=' + str(lat) + '&lon=' + str(lon) + '&APPID=431a44405aef953371bcbe245588e0c7')
        if r.status_code == 200:
            success = True
            json = r.json()
    elif zip != '':
        #forecast = http://api.openweathermap.org/data/2.5/forecast?lat=41.3&lon=95.9&APPID=431a44405aef953371bcbe245588e0c7
        r = Requests.get('http://api.openweathermap.org/data/2.5/forecast?zip=' + str(zip) + '&APPID=431a44405aef953371bcbe245588e0c7')
        if r.status_code == 200:
            success = True
            json = r.json()
    else:
        pass

    #for key, value in json.items():
    #    print(str(key) + '   ' + str(value))

    # print('+1 Day')
    # print((json['list']))

    print('+1 Day 3AM')
    print((json['list'][0]))
    print('+1 Day 6AM')
    print((json['list'][1]))
    print('+1 Day 9AM')
    print((json['list'][2]))
    print('+1 Day 12PM')
    print((json['list'][3]))
    print('+1 Day 3PM')
    print((json['list'][4]))
    print('+1 Day 6PM')
    print((json['list'][5]))
    print('+1 Day 9PM')
    print((json['list'][6]))
    print()
    print()
    print('+2 Day 3AM')
    print((json['list'][7]))
    print('+2 Day 6AM')
    print((json['list'][8]))
    print('+2 Day 9AM')
    print((json['list'][9]))
    print('+2 Day 12PM')
    print((json['list'][10]))
    print('+2 Day 3PM')
    print((json['list'][11]))
    print('+2 Day 6PM')
    print((json['list'][12]))
    print('+2 Day 9PM')
    print((json['list'][13]))
    print()
    print()
    print('+3 Day 3AM')
    print((json['list'][14]))
    print('+3 Day 6AM')
    print((json['list'][15]))
    print('+3 Day 9AM')
    print((json['list'][16]))
    print('+3 Day 12PM')
    print((json['list'][17]))
    print('+3 Day 3PM')
    print((json['list'][18]))
    print('+3 Day 6PM')
    print((json['list'][19]))
    print('+3 Day 9PM')
    print((json['list'][20]))
    print()
    print()
    print('+4 Day 3AM')
    print((json['list'][21]))
    print('+4 Day 6AM')
    print((json['list'][22]))
    print('+4 Day 9AM')
    print((json['list'][23]))
    print('+4 Day 12PM')
    print((json['list'][24]))
    print('+4 Day 3PM')
    print((json['list'][25]))
    print('+4 Day 6PM')
    print((json['list'][26]))
    print('+4 Day 9PM')
    print((json['list'][27]))
    print()
    print()
    print('+5 Day 3AM')
    print((json['list'][28]))
    print('+5 Day 6AM')
    print((json['list'][29]))
    print('+5 Day 9AM')
    print((json['list'][30]))
    print('+5 Day 12PM')
    print((json['list'][31]))
    print('+5 Day 3PM')
    print((json['list'][32]))
    print('+5 Day 6PM')
    print((json['list'][33]))
    print('+5 Day 9PM')
    print((json['list'][34]))


    '''
    print('+3 Day')
    print()
    print('+4 Day')
    print()
    print('+5 Day')
    print()
    
    '''
    #j = Json.loads(json)
    #json['']
    return render(request, 'blog/dashboard.html', {'lat':lat, 'lon':lon,
                                                   'zip':zip, 'success':success})
    #return render(request, 'blog/blog.html', {'topPosts': topPosts, 'blogImages': displayImages})

@login_required
def post_deleted(request, id):
    post = top_post.objects.get(post_id=id).delete()
    return render(request, 'blog/post_deleted_after.html')

@login_required
def post_detail(request, post_id):
    topPost = get_object_or_404(top_post, post_id=post_id)
    images = image.objects.filter(top_post_id=topPost.post_id)
    isAuthor = False
    print(request.user.username)
    print(topPost.user_id.username)
    if request.user.username == topPost.user_id.username:
        isAuthor = True
    dateNow = timezone.now()
    return render(request, 'blog/post_detail.html', {'post': topPost, 'images': images,
                                                     'isAuthor': isAuthor, 'dateNow': dateNow})


@login_required
def delete_image(request, id):
    # Get the ID for the page to redirect to after deletion
    postId = image.objects.get(id=id)
    postId = postId.top_post_id.post_id
    images = image.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('post_edit', kwargs={'post_id': postId}))


@login_required
def post_edit(request, post_id):
    topPost = get_object_or_404(top_post, post_id=post_id)
    # Need to lay these out in an editable way
    images = image.objects.filter(top_post_id=topPost.post_id)
    if request.method == "POST":
        postForm = PostForm(request.POST, prefix='PostForm')
        if postForm.is_valid():
            title = request.POST['PostForm-title']
            text = request.POST['PostForm-text']
            newTopPost = top_post.objects.get(post_id=post_id)
            newTopPost.title = title
            newTopPost.text = text
            newTopPost.save()
            # newTopPost = top_post.objects.get(post_id=post_id)
            return redirect('post_detail', post_id=newTopPost.post_id)
    else:
        form = PostForm(instance=topPost, prefix='PostForm')
        # images = ImageForm()
        return render(request, 'blog/post_edit.html', {'form': form, 'images': images})


'''Uses old django girls post object
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
'''


def home(request):
    return render(request, 'blog/home.html')


@login_required
def dashboard(request):
    return render(request, 'blog/dashboard.html')


@login_required
def locations(request):
    return render(request, 'blog/locations.html')


def blog(request):
    topPosts = top_post.objects.all().order_by('-post_id')
    displayImages = []
    # Get some default image if posts don't have an image
    defaultImage = None  # image.objects.get(image='blogImages/2018/03/20/instructor.jpg')
    for post in topPosts:
        allBlogImages = image.objects.filter(top_post_id=post.post_id)
        try:
            randomImage = allBlogImages[randrange(0, len(allBlogImages))]
        except:
            randomImage = defaultImage
        displayImages.append(randomImage)
    return render(request, 'blog/blog.html', {'topPosts': topPosts, 'blogImages': displayImages})


@login_required
def blog_search(request):  # , formTags):
    if request.method == 'GET':
        # SearchForm
        newSearch = request.GET['search']
        # I should upgrade this to also split on a comma
        searchTerms = newSearch.split()
        postIds = []
        for tag in searchTerms:
            dataBaseTags = modelsTag.objects.filter(tag=tag)
            for dataBaseTag in dataBaseTags:
                post = dataBaseTag.top_post_id
                postIds.append(post.post_id)
        # #topPosts = top_post.objects.all().order_by('-post_id')
        topPosts = top_post.objects.filter(post_id__in=postIds)
        displayImages = []
        # Get some default image if posts don't have an image
        defaultImage = None
        for post in topPosts:
            allBlogImages = image.objects.filter(top_post_id=post.post_id)
            try:
                randomImage = allBlogImages[randrange(0, len(allBlogImages))]
            except:
                randomImage = defaultImage
            displayImages.append(randomImage)
        # Display search error if no posts are found
        if len(topPosts) > 0:
            return render(request, 'blog/blog.html', {'topPosts': topPosts, 'blogImages': displayImages})
        else:
            topPosts = []
            errorPost = top_post(post_id=999999999, published_date=timezone.now(), title="No Results!",
                                 text='Separate Search Terms by a Space', user_id=request.user)
            errorPost.author = 'Oh No'
            topPosts.append(errorPost)

            return render(request, 'blog/blog.html', {'topPosts': topPosts, 'blogImages': displayImages})

    else:
        topPosts = None
        displayImages = None
        return render(request, 'blog/blog.html', {'topPosts': topPosts, 'blogImages': displayImages})


@login_required
def my_profile(request):
    return render(request, 'blog/my_profile.html')


def about_us(request):
    language_translator = LanguageTranslator(
        username='90cbe197-3db2-45e1-8d4b-0a95444275f0',
        password='jxPHFLuHnTra')

    translation = language_translator.translate(
        text=['Join us in the quest to witness a tornado close and personal.We are the StormChasers.'],
        source='en',
        target='fr')

    translatedtext = json.dumps(translation, indent=2, ensure_ascii=False)

    t = json.loads(translatedtext)

    translation = t['translations'][0]['translation']

    return render(request, 'blog/about_us.html', {'translations': translation})


# def about_us1(request):
#     language_translator1 = LanguageTranslator1(
#         username='0a1ec0ad-b7d8-4b8c-a6cc-d368be0c96ac',
#         password='I6lRukwzjTo4')
#
#     translation1 = language_translator1.translate(
#         text=['Join us in the quest to witness a tornado close and personal.We are the StormChasers.'],
#         source='en',
#         target='es')
#
#     translatedtext1 = json.dumps(translation1, indent=2, ensure_ascii=False)
#
#     t1 = json.loads(translatedtext1)
#
#     translationes = t1['translations'][0]['translation']
#
#     print(translationes)
#
#     return render(request, 'blog/about_us.html', {'translationsp': translationes})

@login_required
def subscriptions(request):
    return render(request, 'blog/subscriptions.html')


@login_required
def add_comment_to_post(request, post_id):
    post = get_object_or_404(top_post, post_id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.top_post_id = post
            comment.user_id = request.user
            comment.author = request.user.username
            comment.is_approved = True
            comment.save()
            return redirect('post_detail', post_id=post.post_id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


'''Uses old django girls post object
@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'blog/post_list.html', {'posts': posts})
'''

'''Uses old django girls post object
@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
'''

'''Uses old django girls post object
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
'''


def pwd_recover(request):
    return render(request, 'blog/pwd_recover.html',
                  {'xxx': pwd_recover})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)
            return render(request, 'blog/my_profile.html', {'profile': profile, 'new_user': new_user})
        # return render(request,
        #  'blog/register_done.html',
        # {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'blog/register.html', {'user_form': user_form})


@login_required
def comment_approve(request, post_id):
    comment = get_object_or_404(response_post, post_id=post_id)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, post_id):
    comment = get_object_or_404(response_post, post_id=post_id)
    comment.text = 'COMMENT DELETED'
    comment.save()
    return redirect('post_detail', post_id=comment.top_post_id.post_id)
