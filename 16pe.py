# names = ["ali","reza","sara" ]
# title_cace = list(map(lambda x : x.title(), names))
# print(title_cace)
# 20.	پروژه کوچک: مدیریت لیست دانشجویان:
# o	یک لیست دو-بعدی از دانشجویان و نمراتشان بسازید: students = [["پریسا", 85], ["کیان", 92], ["آریا", 78]].
# o	دانشجوی جدید ["مریم", 95] را با append به لیست اضافه کنید.
# o	لیست را بر اساس نمره (عنصر دوم هر لیست داخلی) به صورت نزولی (از بیشترین نمره) مرتب کنید. (نیاز به lambda دارد).
# o	در نهایت، با استفاده از enumerate، لیست نهایی را به صورت یک رتبه‌بندی شکیل چاپ کنید. مثال: رتبه 1: مریم با نمره 95.


students = [["aria", 78], ["kian", 92], ["parisa", 85]]
students.append(["maryam", 95])
students.sort(key=lambda item: item[1], reverse=True)
for rank, student in enumerate(students, start=1):
    name, score = student
    print(f"rank {rank} {name} with score, {score}")
