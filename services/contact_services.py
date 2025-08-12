from fastapi import Request
from models.contact_model import Contact
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection
 
#------------------------------------convert 
def convert_object_is_to_str(contact:dict):
    contact['_id'] = str(contact['_id'])
    return contact

#--------------------get all contact-------------------------------------------------
async def get_contact(request:Request,collection:AsyncIOMotorCollection):
    contacts = await collection.find().to_list(1000)
    return [convert_object_is_to_str(contact) for contact in contacts]

#---------get contact by id---------------------------------------------------
async def get_contact_by_id(request:Request,collection:AsyncIOMotorCollection,id:str):
    contact = await collection.find_one({"_id":ObjectId(id)})
    return convert_object_is_to_str(contact)

#-------------------------------add contact------------------------------
async def add_contact(request:Request,collection:AsyncIOMotorCollection):
    data = await request.form()
    contact = Contact(
        first_name=data["first_name"],
        last_name=data["last_name"],
        email=data["email"],
        phone=data["phone"],
        address=data["address"]
    )
    contact_dict = contact.model_dump()
    new_contact_result = await collection.insert_one(contact_dict)
    inserted_document = await collection.find_one({"_id": new_contact_result.inserted_id})
    return convert_object_is_to_str(inserted_document)

#---------------------------------update contact
# Before
# async def update_contact(request:Request,collection:AsyncIOMotorCollection):

# After (Corrected)
async def update_contact(request:Request,collection:AsyncIOMotorCollection, id: str):
    # The 'id' parameter is now correctly passed to the function.
    # The code inside can then use this 'id' to find the document.
    ...
    data = await request.form()
    contact = Contact(first_name=data["first_name"],last_name=data["last_name"],email=data["email"],phone=data["phone"],address=data["address"])
    contact_dict = contact.model_dump()
    await collection.update_one({"_id":ObjectId(id)},{"$set":contact_dict})
    return {"message": "Contact updated successfully"} # Or return the updated contact

#-------------------------delete contact
async def delete_contact(request:Request,collection,id:str):
    await collection.delete_one({"_id":ObjectId(id)})
    # The success message or redirect should be handled by the controller.
    return {"status": "success"} # Return a simple status or nothing