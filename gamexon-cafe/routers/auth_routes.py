from fastapi import APIRouter, Body, HTTPException, Depends, responses, status
from firebase_admin import auth
import middleware.firebase as firebase
from models.user import LoginSchema, RegisterSchema

router = APIRouter()

@router.post('/register')
async def create_account(user_data:RegisterSchema):
   try:
        user = auth.create_user(
            email=user_data.email,
            password=user_data.password,
            display_name=user_data.username
        )
        return responses.JSONResponse(content={"message": "User created successfully", "user_id": user.uid
        }, status_code=201)
   except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating user: {str(e)}")

@router.post('/login')
async def login_account(user_data:LoginSchema):
    email = user_data.email
    password = user_data.password

    try:
        user = firebase.get_firebase_config().auth().sign_in_with_email_and_password(
            email = email,
            password = password
        )

        token = user['idToken']

        return responses.JSONResponse(
            content={
                "token":token
            },status_code=200
        )

    except:
        raise HTTPException(
            status_code=400,detail="Invalid Credentials"
        )

@router.post("/assign-role")
def assign_role(
    user_id: str = Body(..., embed=True),
    role: str = Body(..., embed=True),
    user: dict = Depends(firebase.get_firebase_user_from_token),
):
    firebase.check_admin_role(user)
    try:
        auth.set_custom_user_claims(user_id, {"role": role})
        return {"message": f"Role '{role}' assigned to user {user_id}"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to assign role: {str(e)}"
        )
