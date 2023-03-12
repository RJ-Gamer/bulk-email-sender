"""
Email Thread to send many emails at once
"""
import logging
from concurrent.futures import ThreadPoolExecutor
from django.core.mail import EmailMultiAlternatives
from common import constants

log = logging.getLogger(__name__)


class EmailThread:
    """
    Email Thread to send many emails at once
    """

    def __init__(self, subject: str, body: str, from_email=None, attachments=None):
        """
        initialize email thread
        """
        self.subject = subject
        self.body = body
        self.from_email = from_email
        self.attachments = attachments

    def send_one_email(self, to_email: str):
        """
        Sends the same email to a single recipient using EmailMultiAlternatives.

        Args:
            to_email (str): The email address to send the email to.
        """
        email = EmailMultiAlternatives(
            subject=self.subject,
            body=self.body,
            from_email=self.from_email,
            to=[to_email],
        )
        email.content_subtype = "html"
        email.attach_alternative(self.body, "text/html")
        if self.attachments:
            for attachment in self.attachments:
                email.attach_file(attachment)
        try:
            email.send()
            log.info(constants.LOG_EMAIL_SENT.format(to_email))
            return constants.EMAIL_SENT
        except Exception as error:
            log.error(constants.LOG_EMAIL_NOT_SENT.format(to_email, error))
            return constants.EMAIL_FAILED

    def send_emails(self, receiver_list: list[str], num_threads: int = 10):
        """
        Sends the same email to multiple recipients in parallel using a thread pool.

        Args:
            to_emails (List[str]): A list of email addresses to send the email to.
            num_threads (int): The number of threads to use for sending emails in parallel.

        Returns:
            A tuple containing the number of successful emails and the number of failed emails.
        """
        success_count, failed_count = 0, 0

        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            tasks = [
                executor.submit(self.send_one_email, email) for email in receiver_list
            ]
            for task in tasks:
                if task.result() == constants.EMAIL_SENT:
                    success_count += 1
                else:
                    failed_count += 1
        return success_count, failed_count
