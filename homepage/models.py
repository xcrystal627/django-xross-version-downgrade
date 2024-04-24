from django.db import models



class CustomerVoice(models.Model):
    class Meta:
        verbose_name = '利用者の声'


    GENDER_CHOICES = (
        ("male", '男性'),
        ("female", '女性'),
    )

    name = models.CharField(max_length=10,  verbose_name = '名前')
    gender = models.CharField(max_length=10,  choices=GENDER_CHOICES, default="male",  verbose_name = '性別')
    age = models.CharField(max_length=5,  verbose_name = '年齢')
    job = models.CharField(max_length=20,  verbose_name = '職業')
    description = models.CharField(max_length=255,  verbose_name = '内容')



class RecruitmentExample(models.Model):

    class Meta:
        verbose_name = '求人例'

    title = models.CharField(max_length=255, verbose_name='タイトル')
    company_name = models.CharField(max_length=255, verbose_name='会社名')
    business_content = models.CharField(max_length=255, verbose_name='業務内容')
    position = models.CharField(max_length=255, verbose_name='募集ポジション')
    location = models.CharField(max_length=255, verbose_name='勤務地')
    applicant_age = models.CharField(max_length=255, verbose_name='応募想定年齢')
    annual_fee = models.CharField(max_length=255, verbose_name='理論年収')
    picture = models.ImageField(upload_to='./media/', max_length=255, verbose_name='添付画像', default="")



class Consultation(models.Model):
    
    class Meta:
        verbose_name = '相談'

    title = models.CharField(max_length=200)
    description = models.TextField()
    time = models.DateTimeField()
