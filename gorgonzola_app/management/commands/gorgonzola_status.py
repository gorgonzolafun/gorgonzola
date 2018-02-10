from gorgonzola_app.models import Log
from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import re


URL = "https://www.facebook.com/PORTAMI-VIA-128458703849924/"
PATTERN = re.compile( r'gorgonzola', re.IGNORECASE)


class Command(BaseCommand):
    help = 'Get Gorgonzola status and save it in Database'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        result = requests.get(URL)
        if result.status_code != 200:
            raise CommandError('Incorrect status code: {status}'.format(
                status=result.status_code)
            )

        soup = BeautifulSoup(result.content, 'html.parser')
        # Find last user posted menu
        element = soup.find_all("div", "userContent")[1]

        # Find Timestamp of menu
        timestamps = [
            item["data-utime"] for item in element.parent.find_all() if "data-utime" in item.attrs
        ]
        if len(timestamps) == 0:
            raise Exception('No timestamp found in webpage')
        unix_time = timestamps[0]
        posted_time = datetime.fromtimestamp(int(unix_time))
        now = datetime.utcnow()

        if posted_time.date() == now.date():
            result = PATTERN.search(element.text)
            if result:
                msg = "Today there is gorgonzola :)"
                status = True
            else:
                msg = "No gorgonzola today :("
                status = False

            last_log = Log.objects.order_by('-id').first()
            if not last_log or last_log.created_on.date() < now.date():
                log = Log()
                log.status = status
                log.save()

                self.stdout.write(self.style.SUCCESS("Stored new Log"))
        else:
            msg = "No posted yet: last menu {} hours ago".format(
                (now-posted_time).total_seconds()//3600
            )
            status = False

        self.stdout.write(self.style.SUCCESS(msg))
