from fastapi import APIRouter, Depends, Request, Path
from fastapi.templating import Jinja2Templates
from motor.motor_asyncio import AsyncIOMotorCollection

# Ensure you are importing the controller functions correctly
from controller.contact_controllers import (
    home_page, 
    update_contact_page, 
    update_contact_redirect, 
    show_contact_page, 
    delete_contact_redirect, 
    add_contact_page,
    add_contact_redirect as add_contact_redirect_controller  # <-- Alias added here
)
from database import get_contacts_collection
router = APIRouter()

templates =  Jinja2Templates(directory="templates")

@router.get("/")
async def home_page_route(request:Request, collection: AsyncIOMotorCollection =Depends(get_contacts_collection)):
    return await home_page(request,collection)

@router.get("/")
@router.get("/contacts")  # Add this decorator to your existing function
async def home_page_route(request:Request,collection:AsyncIOMotorCollection=Depends(get_contacts_collection)):
    return await home_page(request,collection)
@router.get("/add-contact") # This route is for the HTML form
async def add_contact_page_route(request:Request, collection: AsyncIOMotorCollection=Depends(get_contacts_collection)):
    return await add_contact_page(request,collection) 

@router.get("/update-contact/{id}")
async def update_contact_page_route(request:Request,id:str,collection:AsyncIOMotorCollection=Depends(get_contacts_collection)):
    return await update_contact_page(request,collection,id)

@router.get("/show-contact/{id}")
async def show_contact_page_route(request:Request,id:str,collection:AsyncIOMotorCollection=Depends(get_contacts_collection)):
    return await show_contact_page(request,collection,id)

@router.get("/delete-contact/{id}")
async def delete_contact_page_route(request:Request,id:str,collection:AsyncIOMotorCollection=Depends(get_contacts_collection)):
    return await delete_contact_redirect(request,collection,id)

@router.post("/add-contact") # This route handles the form submission
# Renamed to avoid recursion
async def add_contact_redirect_route(request:Request,collection:AsyncIOMotorCollection=Depends(get_contacts_collection)):
    # Now correctly calls the imported controller function
    return await add_contact_redirect_controller(request,collection)

@router.post("/update-contact/{id}")
async def update_contact_redirect_route(request:Request,id:str,collection:AsyncIOMotorCollection=Depends(get_contacts_collection)):
    return await update_contact_redirect(request,collection,id)