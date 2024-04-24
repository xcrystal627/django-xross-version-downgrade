from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from homepage.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):
            
        for i in range(5):
            recruitment_item = RecruitmentExample(
                title = '購買・調達（マネージャー経験者）',
                company_name = '株式会社日立プラントサービス',
                business_content = '事業部門の経営課題・調達課題を見出し、その解決に向けて調達プロセスの改革を提案実行していただきます。',
                position = '調達マネージャー', 
                location = '東京都豊島区 ',
                applicant_age = '28～60歳 ',
                annual_fee = '450万円～650万円',
                picture = 'default.png'
            )
            recruitment_item.save()

            gender = 'male'
            if i % 2 == 0:
                gender = 'female'

            customer_item = CustomerVoice(
                name = '●●',
                gender = gender,
                age = '30代',
                job = '不動産営業',
                description = '転職を迷っている時に相談することで、自分のキャリアや目標を明確にすることができました。また、求人情報や面接対策など、転職活動に必要なサポートが充実していたので、安心して活動することができました。'
            )

            customer_item.save()

            self.stdout.write(self.style.SUCCESS('Customer Voice and Recruitment Example adding...'))

        
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))