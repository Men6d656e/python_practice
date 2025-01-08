

day = int(input("Enter day number: "))

# # using if-elif
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Invalid day number")

# using match-case
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from mongoengine import DoesNotExist

from models.user import User
from schemas.user import UserDB

router = APIRouter(prefix="/login", tags=["login"])


@router.post("")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        user = User.objects.get(email=form_data.username)
    except DoesNotExist:
        return {"error": "User not found"}
    if not user.check_password(form_data.password):
        return {"error": "Invalid password"}
    return UserDB.from_mongo(user)
