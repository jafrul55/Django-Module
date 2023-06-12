from django.shortcuts import render

# Create your views here.


# def contact(request):
#     return render(request, './first_app/index.html', context={'author': 'Phitron',
#                                                               'age': 19, 'marks': 89})

# -----------------------------------------------------------
# def contact(request):
#     return render(request, './first_app/index.html', {'courses': [
#         {
#             'id': 1,
#             'course': 'C',
#             'teacher': 'Rahim'
#         },
#         {
#             'id': 2,
#             'course': 'C++',
#             'teacher': 'Korim'

#         },
#         {
#             'id': 3,
#             'course': 'Python',
#             'teacher': 'Fahim'

#         },

#     ]})

# ----------------------------------------------
def contact(request):
    return render(request, './first_app/index.html', {"name": "I am Rahim",

                  "marks": 86, "lst": [24, 3, 10, 5], "blog": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi perferendis molestias maxime assumenda, culpa mollitia quas reprehenderit"})
