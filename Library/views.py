from django.db.models.fields import DateField
from django.shortcuts import render
from django.contrib import messages
from .models import User, Book, BookRecord
from django.http import HttpResponseRedirect
from django.db.models import Q


def LogIn(request):

    if "CreateAccount" in request.POST:
        return HttpResponseRedirect("/Library/signup/")

    elif "Log In" in request.POST:

        EMAIL = request.POST.get("Email address")
        PASSWORD = request.POST.get("PasswordInput")

        if EMAIL == "" and PASSWORD == "":
            messages.warning(request, "Check the correct DataInput,Try Again")
            return HttpResponseRedirect("/Library/login/")

        elif User.objects.filter(Email=EMAIL, Password=PASSWORD).exists():
            return HttpResponseRedirect("/Library/HomePage/")

        else:
            messages.warning(request, "Not correct of Email or Password ,Try Again")
            return HttpResponseRedirect("/Library/login/")

    return render(request, "Login.html")


def SignUp(request):

    if "SignUp" in request.POST:

        username = request.POST.get("USERNAME")
        email = request.POST.get("EMAIL")
        password = request.POST.get("PASSWORD")
        phone = request.POST.get("PHONE")

        if username == "" or email == "" or password == "" or phone == "":

            messages.warning(request, "Please Fill all the data input")

            return render(request, "Signup.html")

        data = User(UserName=username, Email=email, Password=password, Phone=phone)
        data.save()
        return HttpResponseRedirect("/Library/login/")

    elif "Back" in request.POST:
        return HttpResponseRedirect("/Library/login/")

    return render(request, "Signup.html")


def LogOut(request):
    return HttpResponseRedirect("/Library/login/")


def UserHomePage(request):
    return render(request, "HomePage.html")


def EditUserInfo(request):

    if "EDIT" in request.POST:

        current_email = request.POST.get("currentemail")

        if current_email == "":
            messages.warning(request, "Please Fill all the data input")
            return render(request, "Setting.html")

        if not (User.objects.filter(Email=current_email).exists()):
            messages.warning(request, "NotCorrect Email ,TryAgain")
            return render(request, "Setting.html")

        user_obj = User.objects.get(Email=current_email)
        username = request.POST.get("newUserName")
        email = request.POST.get("newEmail")
        password = request.POST.get("newPassword")
        phone = request.POST.get("newPhone")

        if username == "" or email == "" or password == "" or phone == "":
            messages.warning(request, "Please Fill all the data input")
            return render(request, "Setting.html")

        user_obj.Email = email
        user_obj.UserName = username
        user_obj.Password = password
        user_obj.Phone = phone
        user_obj.save()
        messages.success(request, "Success Update")

    return render(request, "Setting.html")


def Books(request):
    return render(
        request,
        "Books.html",
        {"bookdisplay": Book.objects.all().filter(Available=True)},
    )


def BorrowBook(request):

    if "confirm" in request.POST:
        email = request.POST.get("email")
        title = request.POST.get("title")
        took_on = request.POST.get("takeOn")
        returned_on = request.POST.get("returnOn")

        if User.objects.filter(Email=email).count() == 0:
            messages.warning(request, "Please enter an correct email")
            return render(request, "BorrowBook.html")

        elif Book.objects.filter(Tittle=title).count() == 0:
            messages.warning(request, "Please enter an existing book title")
            return render(request, "BorrowBook.html")

        data = BookRecord(
            book_title=title, user_email=email, Took_On=took_on, Return_On=returned_on
        )
        data.save()

        Book.objects.filter(Tittle=title).update(Available=False)
        messages.success(request, "Success BorrowBook")

    return render(request, "BorrowBook.html")


def BookSearch(request):
    if "confirm1" in request.POST:

        search = request.POST.get("searchbytext")
        if Book.objects.filter(Q(Author=search) | Q(Tittle=search)).exists():
            BOOK = Book.objects.all().filter(Q(Author=search) | Q(Tittle=search))
            return render(request, "SearchBook.html", {"Books": BOOK})

        else:
            messages.warning(request, "Not correct search input")
            return render(request, "SearchBook.html")

    elif "confirm2" in request.POST:
        search = request.POST.get("searchbydate")

        if search == "":
            messages.warning(request, "Please Enter coorect date")
            return render(request, "SearchBook.html")

        elif Book.objects.filter(PublicationYear=search).exists():
            BOOK = Book.objects.all().filter(PublicationYear=search)
            return render(request, "SearchBook.html", {"Books": BOOK})

        else:
            messages.warning(request, "Not correct search Date input")
            return render(request, "SearchBook.html")

    return render(request, "SearchBook.html")
