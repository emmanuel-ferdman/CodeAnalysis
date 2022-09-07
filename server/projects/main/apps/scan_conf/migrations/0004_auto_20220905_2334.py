# Generated by Django 3.1.14 on 2022-09-05 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scan_conf', '0003_auto_20220518_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(choices=[('cpp', 'C/C++'), ('java', 'Java'), ('js', 'JavaScript'), ('oc', 'Objective-C'), ('php', 'PHP'), ('python', 'Python'), ('cs', 'C#'), ('ruby', 'Ruby'), ('kotlin', 'Kotlin'), ('Go', 'Go'), ('Lua', 'Lua'), ('swift', 'Swift'), ('html', 'Html'), ('css', 'Css'), ('ts', 'TypeScript'), ('scala', 'Scala'), ('visualbasic', 'Visual Basic'), ('plsql', 'PL/SQL'), ('cobol', 'COBOL'), ('abap', 'ABAP'), ('tsql', 'T-SQL'), ('flex', 'Flex'), ('rpg', 'RPG'), ('apex', 'Apex'), ('pli', 'PL/I'), ('xml', 'XML'), ('dart', 'Dart'), ('shell', 'Shell'), ('protobuf', 'Protocol Buffers'), ('sql', 'SQL'), ('wasm', 'WebAssembly'), ('rust', 'Rust')], help_text='程序语言', max_length=32, null=True),
        ),
    ]