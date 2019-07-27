from django.db import models


# 创建题目的类型
class QuestionsType(models.Model):
    # 类型名
    src_name = models.CharField(db_column='src_name', max_length=50, verbose_name='题目类型')
    # 类型描述
    src_dec = models.TextField(db_column='src_dec', verbose_name='类型描述')

    def to_dict(self):
        dic = {
            'title': self.src_name,
            'desc': self.src_dec
        }
        return dic

    def __str__(self):
        return self.src_name

    class Meta:
        db_table = 'QuestionsType'
        verbose_name = '题目类型'
        verbose_name_plural = verbose_name


# 上传输入文件
def input_file_name(instance, filename):
    return "Files/{title}/input/{file}".format(instance.id, title=instance.title, file=filename)


# 上传输出文件
def out_file_name(instance, filename):
    return "Files/{title}/out/{file}".format(instance.id, title=instance.title, file=filename)


# 创建题库数据库实例
class Questions(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, verbose_name='id')
    # 题的名称
    title = models.CharField(db_column='title', unique=True, blank=True, null=True, default=None, max_length=50,
                             verbose_name='题名')
    # 题的描述
    src = models.TextField(db_column='src', verbose_name='题目内容')
    # 题目类型，外键关联
    question = models.ForeignKey(QuestionsType, verbose_name='题目类型', on_delete=models.CASCADE)
    # 输出样例展示
    show_example = models.TextField(db_column='show_example', verbose_name='样例说明')
    # 输入样例的数据和结果
    # 输入文件夹和输出的文件夹
    InputTextFile = models.FileField(upload_to=input_file_name, blank=False, verbose_name='输入文件')

    OutputTextFile = models.FileField(upload_to=out_file_name, blank=False, verbose_name='输出文件')
    # example = models.ForeignKey(ExampleR, verbose_name='测试样例', on_delete=models.CASCADE)
    # 难度系数
    difficult = models.IntegerField(db_column='difficult', verbose_name='难度系数')
    # 限时
    time = models.IntegerField(db_column='time', verbose_name='时限毫秒')
    # 限内存
    memory = models.IntegerField(db_column='memory', verbose_name='内存k单位')

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Questions"
        verbose_name = '题库'
        verbose_name_plural = verbose_name
