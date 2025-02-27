""" Email service with mailjet rest api """

from mailjet_rest import Client
from app.core.config import settings

class EmailService:
    """ Email service with mailjet rest api """
    def __init__(self):
        """ Initialize mailjet client """
        self.mailjet = Client(auth=(settings.MAILJET_API_KEY, settings.MAILJET_SECRET_KEY) , version='v3.1')
        self.sender_email = settings.MAILJET_EMAIL
    
    async def __send_email(self, to, subject, template_id, variables):
        """ Send email using mailjet api """
        print("*********************  SENDING EMAIL *********************")
        try:
            data = {
            'Messages': [
                {
                    "From": {
                        "Email": self.sender_email,
                        "Name": "BTG"
                    },
                    "To": [
                        {
                            "Email": to,
                            "Name": "User"
                        }
                    ],
                    "TemplateID": template_id,
                    "TemplateLanguage": True,
                    "Subject": subject,
                    "Variables": variables
                }
            ]
        }
            result = self.mailjet.send.create(data=data)
            return result.status_code
        except Exception as _e:
            print("*********************  ERROR SENDING EMAIL *********************")
            print(_e)
            return 400
    
    
    async def transaction_creation_email(self, to, data ):
        """ Send email to user when transaction is created """
        print("*********************  SENDING TRANSACTION EMAIL  DEF *********************")
        subject = "Transaction Created"
        data["subject"] = subject
        
        template_id = settings.MAILJET_TEMPLATE_TRANSACTION
        return self.__send_email(to, subject, template_id, data)