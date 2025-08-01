from fastapi import APIRouter
from twilio.rest import Client

router = APIRouter()

@router.post("/send-alert")
def send_alert(phone: str, msg: str):
    client = Client("TWILIO_SID", "TWILIO_AUTH")
    message = client.messages.create(
        body=msg,
        from_="+1234567890",
        to=phone
    )
    return {"status": "SMS sent", "sid": message.sid}